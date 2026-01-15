#!/usr/bin/env python3
"""Test the BLD interpreter."""

import sys
sys.path.insert(0, 'src')

from bld.parser import parse
from bld.traverser import Traverser, State


def test_parse_map():
    """Test parsing map.bld."""
    source = open('examples/functional/map.bld').read()
    structure = parse(source)

    print(f"Structure: {structure.name}")
    print(f"Boundaries: {[b.name for b in structure.boundaries]}")
    print(f"Links: {[l.name for l in structure.links]}")
    print(f"Dimensions: {[d.name for d in structure.dimensions]}")
    print(f"Returns: {structure.returns}")
    print()


def test_parse_bld_bld():
    """Test parsing the self-referential bld.bld."""
    source = open('bootstrap/bld.bld').read()
    structure = parse(source)

    print(f"Structure: {structure.name}")
    print(f"Boundaries ({len(structure.boundaries)}):")
    for b in structure.boundaries:
        print(f"  {b.name}: {' | '.join(p.name for p in b.partitions)}")
    print(f"Links ({len(structure.links)}):")
    for l in structure.links:
        print(f"  {l.name}: {l.source} -> {l.target}")
    print(f"Dimensions ({len(structure.dimensions)}):")
    for d in structure.dimensions:
        print(f"  {d.name}: {d.extent} {d.props}")
    print()


def test_parse_x86():
    """Test parsing x86.bld."""
    source = open('bootstrap/x86.bld').read()
    structure = parse(source)

    print(f"Structure: {structure.name}")
    print(f"Boundaries ({len(structure.boundaries)}):")
    for b in structure.boundaries:
        print(f"  {b.name}: {len(b.partitions)} partitions")
        for p in b.partitions[:3]:  # Show first 3
            print(f"    {p.name}: {p.semantics}")
    print()


def test_emit_bytes():
    """Test direct byte emission using traverser state."""
    state = State()

    # Emit a simple x86 program: ret (0xC3)
    state.emit_byte(0xC3)

    print(f"Emitted bytes: {state.output.hex()}")
    assert state.output == bytes([0xC3])
    print("test_emit_bytes: PASSED")
    print()


def test_emit_prologue():
    """Test emitting function prologue."""
    state = State()

    # push rbp (0x55)
    state.emit_byte(0x55)

    # mov rbp, rsp (48 89 E5)
    state.emit_bytes(0x48, 0x89, 0xE5)

    print(f"Prologue bytes: {state.output.hex()}")
    assert state.output == bytes([0x55, 0x48, 0x89, 0xE5])
    print("test_emit_prologue: PASSED")
    print()


def test_emit_with_labels():
    """Test emitting code with labels and relocations."""
    state = State()

    # jmp skip
    state.emit_byte(0xE9)
    state.reloc('skip')

    # nop (filler)
    state.emit_byte(0x90)

    # skip:
    state.label('skip')

    # ret
    state.emit_byte(0xC3)

    # Resolve
    state.resolve()

    print(f"Code with labels: {state.output.hex()}")
    # JMP rel32 should point past the NOP to the RET
    # Offset at position 1-4, target at position 6
    # rel = 6 - (1 + 4) = 1
    expected = bytes([0xE9, 0x01, 0x00, 0x00, 0x00, 0x90, 0xC3])
    assert state.output == expected, f"Expected {expected.hex()}, got {state.output.hex()}"
    print("test_emit_with_labels: PASSED")
    print()


def test_traverse_simple():
    """Test traversing a simple structure."""
    source = """
structure Test

D input: N [input]
D output: M [output]

B mode: a | b
  a -> emit_byte(0x41)
  b -> emit_byte(0x42)

L process: input -> output (deps=1)

returns: output
"""
    structure = parse(source)
    traverser = Traverser()
    result = traverser.traverse(structure)

    print(f"Traversal result: {result.hex() if result else 'None'}")
    # Should emit 0x41 (A) and 0x42 (B) from the boundary partitions
    assert result == bytes([0x41, 0x42]), f"Expected 4142, got {result.hex()}"
    print("test_traverse_simple: PASSED")
    print()


if __name__ == '__main__':
    print("=== BLD Interpreter Tests ===\n")

    test_parse_map()
    test_parse_bld_bld()
    test_parse_x86()
    test_emit_bytes()
    test_emit_prologue()
    test_emit_with_labels()
    test_traverse_simple()

    print("=== All tests passed! ===")
