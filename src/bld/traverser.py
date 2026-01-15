# BLD Traverser - Execute structures by traversal
#
# Cost(traverse) = B_visit + D_elements * L_step
#
# The traverser visits boundaries, links, dimensions in order,
# executing semantic annotations as primitive operations.
#
# Primitive semantics (what the interpreter understands):
#   - emit(value)           Write value to output
#   - emit_byte(byte)       Write single byte to output
#   - emit_bytes(...)       Write multiple bytes
#   - set(name, value)      Set state variable
#   - get(name)             Get state variable
#   - pattern(expr)         Pattern match (returns bool)
#   - text_match(text)      String comparison
#   - label(name)           Define label at current position
#   - jmp(label)            Jump to label (for linking)
#   - call(structure)       Call another structure (uses=...)
#
# Everything else (x86 encoding, ELF format, etc.) is defined
# IN BLD and composed from these primitives.

from dataclasses import dataclass, field
from typing import Any, Optional, Callable
from .parser import ParsedStructure, Boundary, Link, Dimension, Semantic


@dataclass
class State:
    """Traversal state - holds variables and output buffer."""
    variables: dict[str, Any] = field(default_factory=dict)
    output: bytearray = field(default_factory=bytearray)
    labels: dict[str, int] = field(default_factory=dict)
    relocations: list[tuple[int, str]] = field(default_factory=list)
    structures: dict[str, ParsedStructure] = field(default_factory=dict)

    def emit(self, value: Any):
        """Emit value to output."""
        if isinstance(value, int):
            # Single byte
            self.output.append(value & 0xFF)
        elif isinstance(value, bytes):
            self.output.extend(value)
        elif isinstance(value, bytearray):
            self.output.extend(value)
        elif isinstance(value, str):
            self.output.extend(value.encode('utf-8'))

    def emit_byte(self, byte: int):
        """Emit single byte."""
        self.output.append(byte & 0xFF)

    def emit_bytes(self, *args):
        """Emit multiple bytes."""
        for b in args:
            if isinstance(b, int):
                self.output.append(b & 0xFF)
            elif isinstance(b, (bytes, bytearray)):
                self.output.extend(b)

    def emit_u16(self, value: int):
        """Emit 16-bit little-endian."""
        self.output.extend(value.to_bytes(2, 'little'))

    def emit_u32(self, value: int):
        """Emit 32-bit little-endian."""
        self.output.extend(value.to_bytes(4, 'little'))

    def emit_u64(self, value: int):
        """Emit 64-bit little-endian."""
        self.output.extend(value.to_bytes(8, 'little'))

    def emit_i32(self, value: int):
        """Emit signed 32-bit little-endian."""
        self.output.extend(value.to_bytes(4, 'little', signed=True))

    def label(self, name: str):
        """Define label at current position."""
        self.labels[name] = len(self.output)

    def reloc(self, name: str):
        """Record relocation for later linking."""
        self.relocations.append((len(self.output), name))
        # Emit placeholder
        self.emit_u32(0)

    def resolve(self):
        """Resolve all relocations."""
        for offset, name in self.relocations:
            if name in self.labels:
                target = self.labels[name]
                # rel32 is relative to end of instruction
                rel = target - (offset + 4)
                self.output[offset:offset + 4] = rel.to_bytes(4, 'little', signed=True)

    def set(self, name: str, value: Any):
        """Set state variable."""
        self.variables[name] = value

    def get(self, name: str, default: Any = None) -> Any:
        """Get state variable."""
        return self.variables.get(name, default)


class Traverser:
    """BLD structure traverser - executes structures by traversal."""

    def __init__(self):
        self.state = State()
        self.builtins = self._init_builtins()

    def _init_builtins(self) -> dict[str, Callable]:
        """Initialize builtin semantic handlers."""
        return {
            # Output primitives
            'emit': self._emit,
            'emit_byte': self._emit_byte,
            'emit_bytes': self._emit_bytes,
            'emit_u16': self._emit_u16,
            'emit_u32': self._emit_u32,
            'emit_u64': self._emit_u64,
            'emit_i32': self._emit_i32,

            # State primitives
            'set': self._set,
            'get': self._get,

            # Control flow
            'label': self._label,
            'reloc': self._reloc,
            'jmp': self._jmp,
            'jcc': self._jcc,

            # x86 encoding helpers (could be moved to x86.bld)
            'rex': self._rex,
            'modrm': self._modrm,
            'sib': self._sib,

            # Pattern matching
            'pattern': self._pattern,
            'text_match': self._text_match,

            # Utilities
            'order': self._order,
            'foreach': self._foreach,
            'uses': self._uses,
            'deps': self._deps,
        }

    def traverse(self, structure: ParsedStructure, input_data: Any = None) -> Any:
        """Traverse a structure, executing it."""
        # Register structure for later calls
        self.state.structures[structure.name] = structure

        # Set input if provided
        if input_data is not None:
            self.state.set('input', input_data)

        # Visit dimensions first (set up iteration bounds)
        for dim in structure.dimensions:
            self._visit_dimension(dim)

        # Visit boundaries (dispatch structure)
        for boundary in structure.boundaries:
            self._visit_boundary(boundary)

        # Visit links in dependency order
        sorted_links = self._sort_links(structure.links)
        for link in sorted_links:
            self._visit_link(link)

        # Resolve relocations
        self.state.resolve()

        return bytes(self.state.output) if self.state.output else self.state.get('result')

    def _visit_dimension(self, dim: Dimension):
        """Visit a dimension declaration."""
        extent = dim.extent
        # Try to evaluate extent
        if extent.isdigit():
            self.state.set(f'dim_{dim.name}', int(extent))
        elif extent == 'N':
            # Dynamic - will be set from input
            pass
        else:
            self.state.set(f'dim_{dim.name}', extent)

        # Store dimension metadata
        self.state.set(f'dim_{dim.name}_props', dim.props)

    def _visit_boundary(self, boundary: Boundary):
        """Visit a boundary declaration and its partitions."""
        # For each partition, execute its semantics
        for partition in boundary.partitions:
            for semantic in partition.semantics:
                self._execute_semantic(semantic)

    def _visit_link(self, link: Link):
        """Visit a link declaration."""
        # Check for 'uses' attribute - means call another structure
        if 'uses' in link.attrs:
            struct_name = link.attrs['uses']
            if struct_name in self.state.structures:
                sub_struct = self.state.structures[struct_name]
                # Recursive traversal
                self.traverse(sub_struct)

    def _sort_links(self, links: list[Link]) -> list[Link]:
        """Sort links by dependency order (deps attribute)."""
        def get_deps(link):
            deps = link.attrs.get('deps', '0')
            try:
                return int(deps)
            except ValueError:
                return 0

        return sorted(links, key=get_deps)

    def _execute_semantic(self, semantic: Semantic):
        """Execute a semantic annotation."""
        handler = self.builtins.get(semantic.name)
        if handler:
            handler(*semantic.args)
        else:
            # Unknown semantic - could be a no-op or log warning
            pass

    # === Builtin semantic handlers ===

    def _emit(self, *args):
        for arg in args:
            self.state.emit(self._eval_arg(arg))

    def _emit_byte(self, arg):
        self.state.emit_byte(self._eval_arg(arg))

    def _emit_bytes(self, *args):
        self.state.emit_bytes(*[self._eval_arg(a) for a in args])

    def _emit_u16(self, arg):
        self.state.emit_u16(self._eval_arg(arg))

    def _emit_u32(self, arg):
        self.state.emit_u32(self._eval_arg(arg))

    def _emit_u64(self, arg):
        self.state.emit_u64(self._eval_arg(arg))

    def _emit_i32(self, arg):
        self.state.emit_i32(self._eval_arg(arg))

    def _set(self, name, value):
        self.state.set(name, self._eval_arg(value))

    def _get(self, name):
        return self.state.get(name)

    def _label(self, name):
        self.state.label(name)

    def _reloc(self, name):
        self.state.reloc(name)

    def _jmp(self, label):
        # Emit JMP rel32
        self.state.emit_byte(0xE9)
        self.state.reloc(label)

    def _jcc(self, condition, label):
        # Emit Jcc rel32
        conditions = {
            'e': 0x84, 'ne': 0x85, 'z': 0x84, 'nz': 0x85,
            'l': 0x8C, 'ge': 0x8D, 'le': 0x8E, 'g': 0x8F,
        }
        cc = conditions.get(condition, 0x84)
        self.state.emit_bytes(0x0F, cc)
        self.state.reloc(label)

    def _rex(self, w=0, r=0, x=0, b=0):
        """Emit REX prefix if needed."""
        w = self._eval_arg(w)
        r = self._eval_arg(r)
        x = self._eval_arg(x)
        b = self._eval_arg(b)
        if w or r or x or b:
            rex = 0x40 | (w << 3) | (r << 2) | (x << 1) | b
            self.state.emit_byte(rex)

    def _modrm(self, mod, reg, rm):
        """Emit ModR/M byte."""
        mod = self._eval_arg(mod)
        reg = self._eval_arg(reg)
        rm = self._eval_arg(rm)
        modrm = ((mod & 3) << 6) | ((reg & 7) << 3) | (rm & 7)
        self.state.emit_byte(modrm)

    def _sib(self, scale, index, base):
        """Emit SIB byte."""
        scale = self._eval_arg(scale)
        index = self._eval_arg(index)
        base = self._eval_arg(base)
        sib = ((scale & 3) << 6) | ((index & 7) << 3) | (base & 7)
        self.state.emit_byte(sib)

    def _pattern(self, *args):
        # Pattern matching - for now just return True
        return True

    def _text_match(self, text):
        # Text matching
        return self.state.get('current_text') == text

    def _order(self, n):
        self.state.set('_order', self._eval_arg(n))

    def _foreach(self, what):
        self.state.set('_foreach', what)

    def _uses(self, name):
        self.state.set('_uses', name)

    def _deps(self, n):
        self.state.set('_deps', self._eval_arg(n))

    def _eval_arg(self, arg) -> Any:
        """Evaluate a semantic argument."""
        if isinstance(arg, int):
            return arg
        if not isinstance(arg, str):
            return arg

        arg = arg.strip()

        # Hex literal
        if arg.startswith('0x'):
            return int(arg, 16)

        # Binary literal
        if arg.startswith('0b'):
            return int(arg, 2)

        # Decimal literal
        if arg.isdigit() or (arg.startswith('-') and arg[1:].isdigit()):
            return int(arg)

        # Byte literal like b'x' or b'\n'
        if arg.startswith("b'") and arg.endswith("'"):
            inner = arg[2:-1]
            if inner.startswith('\\'):
                escapes = {'n': ord('\n'), 't': ord('\t'), 'r': ord('\r'), '0': 0}
                return escapes.get(inner[1], ord(inner[1]))
            return ord(inner)

        # String literal
        if arg.startswith('"') and arg.endswith('"'):
            return arg[1:-1]

        # Variable reference
        if arg.startswith('$'):
            return self.state.get(arg[1:])

        # Raw string/identifier
        return arg
