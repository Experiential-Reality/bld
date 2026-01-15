#!/usr/bin/env python3
"""Test generating and running ELF executables."""

import os
import subprocess
import tempfile
import sys

sys.path.insert(0, 'src')

from bld.elf import emit_elf64, emit_exit_program, emit_hello_world


def test_exit_program():
    """Test generating a program that exits with code 42."""
    print("=== Test: Exit Program ===")

    # Generate code that exits with code 42
    code = emit_exit_program(42)
    print(f"Code bytes ({len(code)}): {code.hex()}")

    # Wrap in ELF
    elf = emit_elf64(code)
    print(f"ELF size: {len(elf)} bytes")

    # Write to temp file and run
    with tempfile.NamedTemporaryFile(delete=False, suffix='.elf') as f:
        f.write(elf)
        path = f.name

    try:
        os.chmod(path, 0o755)
        result = subprocess.run([path], capture_output=True)
        print(f"Exit code: {result.returncode}")
        assert result.returncode == 42, f"Expected 42, got {result.returncode}"
        print("test_exit_program: PASSED\n")
    finally:
        os.unlink(path)


def test_hello_world():
    """Test generating a program that prints 'Hello, BLD!'."""
    print("=== Test: Hello World ===")

    # Generate hello world code
    code = emit_hello_world()
    print(f"Code bytes ({len(code)}): {code[:40].hex()}...")

    # Wrap in ELF
    elf = emit_elf64(code)
    print(f"ELF size: {len(elf)} bytes")

    # Write to temp file and run
    with tempfile.NamedTemporaryFile(delete=False, suffix='.elf') as f:
        f.write(elf)
        path = f.name

    try:
        os.chmod(path, 0o755)
        result = subprocess.run([path], capture_output=True, text=True)
        print(f"Output: {repr(result.stdout)}")
        print(f"Exit code: {result.returncode}")
        assert result.stdout == "Hello, BLD!\n", f"Expected 'Hello, BLD!\\n', got {repr(result.stdout)}"
        assert result.returncode == 0
        print("test_hello_world: PASSED\n")
    finally:
        os.unlink(path)


def test_save_executable():
    """Save a hello world executable for inspection."""
    print("=== Saving hello.elf ===")

    code = emit_hello_world()
    elf = emit_elf64(code)

    with open('hello.elf', 'wb') as f:
        f.write(elf)

    os.chmod('hello.elf', 0o755)
    print("Saved hello.elf - run with: ./hello.elf")
    print(f"Size: {len(elf)} bytes\n")


if __name__ == '__main__':
    print("=== BLD Executable Generation Tests ===\n")

    test_exit_program()
    test_hello_world()
    test_save_executable()

    print("=== All executable tests passed! ===")
