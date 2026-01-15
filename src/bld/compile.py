#!/usr/bin/env python3
"""BLD Compiler - compile .bld files to native executables.

Usage:
    python -m bld.compile hello.bld -o hello
    ./hello
"""

import argparse
import os
import sys

from .parser import parse
from .traverser import Traverser
from .elf import emit_elf64


def compile_bld(source: str) -> bytes:
    """Compile BLD source to native x86-64 code."""
    structure = parse(source)
    traverser = Traverser()
    code = traverser.traverse(structure)

    if isinstance(code, bytes):
        return code
    elif code is None:
        # No output from traversal - return empty
        return b''
    else:
        return bytes(code)


def compile_to_elf(source: str) -> bytes:
    """Compile BLD source to ELF executable."""
    code = compile_bld(source)
    return emit_elf64(code)


def main():
    parser = argparse.ArgumentParser(description='Compile BLD to native executable')
    parser.add_argument('input', help='Input .bld file')
    parser.add_argument('-o', '--output', help='Output executable (default: input name without .bld)')
    parser.add_argument('-c', '--code-only', action='store_true', help='Output raw code without ELF wrapper')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()

    # Read input
    with open(args.input) as f:
        source = f.read()

    if args.verbose:
        print(f"Compiling {args.input}...")

    # Compile
    if args.code_only:
        result = compile_bld(source)
    else:
        result = compile_to_elf(source)

    # Determine output filename
    output = args.output
    if not output:
        output = os.path.splitext(args.input)[0]
        if not args.code_only:
            # Don't add extension for ELF
            pass

    # Write output
    with open(output, 'wb') as f:
        f.write(result)

    # Make executable
    if not args.code_only:
        os.chmod(output, 0o755)

    if args.verbose:
        print(f"Wrote {len(result)} bytes to {output}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
