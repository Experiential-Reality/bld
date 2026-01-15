# BLD - Boundary/Link/Dimension Language Interpreter
#
# This is the MINIMAL Python implementation. Everything else is BLD.
#
# The interpreter does three things:
#   1. Parse .bld text into structure
#   2. Traverse structures, executing semantic annotations
#   3. Basic I/O (read files, write bytes)
#
# BLD structure of this interpreter:
#
#   structure Interpreter
#   B element: structure | boundary | link | dimension | semantic
#   B semantic_op: emit | set | branch | loop | call
#   D source: N [input]
#   D state: M [sequential]
#   L parse: source -> structure (deps=1)
#   L traverse: structure -> state (deps=1)
#   L execute: semantic -> state (deps=1)

from .parser import parse, ParsedStructure, Boundary, Link, Dimension
from .traverser import Traverser, State
from .elf import emit_elf64, emit_exit_program, emit_hello_world

__all__ = [
    'parse', 'ParsedStructure', 'Boundary', 'Link', 'Dimension',
    'Traverser', 'State',
    'emit_elf64', 'emit_exit_program', 'emit_hello_world',
]

def main():
    """Entry point for bld command."""
    from .compile import main as compile_main
    compile_main()
