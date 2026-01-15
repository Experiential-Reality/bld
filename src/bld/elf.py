# ELF64 binary generator
#
# This module provides functions to wrap machine code in an ELF executable.
# The structure follows elf.bld - this is the Python implementation of
# the primitives that elf.bld's semantics call.

from .traverser import State


def emit_elf64(code: bytes, entry_offset: int = 0, base_addr: int = 0x400000) -> bytes:
    """Wrap machine code in an ELF64 executable.

    Args:
        code: Raw machine code bytes
        entry_offset: Offset within code to entry point (default: 0)
        base_addr: Virtual address base (default: 0x400000)

    Returns:
        Complete ELF64 executable bytes
    """
    state = State()

    # Calculate sizes and addresses
    ehdr_size = 64      # ELF header size
    phdr_size = 56      # Program header size
    code_offset = ehdr_size + phdr_size  # Code starts after headers
    file_size = code_offset + len(code)
    entry_addr = base_addr + code_offset + entry_offset

    # === ELF Header (64 bytes) ===

    # e_ident[0..4]: Magic number
    state.emit_bytes(0x7F, ord('E'), ord('L'), ord('F'))

    # e_ident[4]: Class (64-bit)
    state.emit_byte(0x02)

    # e_ident[5]: Data encoding (little endian)
    state.emit_byte(0x01)

    # e_ident[6]: Version
    state.emit_byte(0x01)

    # e_ident[7]: OS/ABI (SYSV)
    state.emit_byte(0x00)

    # e_ident[8..16]: Padding (8 bytes)
    for _ in range(8):
        state.emit_byte(0x00)

    # e_type: Executable
    state.emit_u16(0x0002)

    # e_machine: x86-64
    state.emit_u16(0x003E)

    # e_version
    state.emit_u32(0x00000001)

    # e_entry: Entry point address
    state.emit_u64(entry_addr)

    # e_phoff: Program header offset (64)
    state.emit_u64(ehdr_size)

    # e_shoff: Section header offset (0 - none)
    state.emit_u64(0)

    # e_flags
    state.emit_u32(0)

    # e_ehsize: ELF header size
    state.emit_u16(ehdr_size)

    # e_phentsize: Program header entry size
    state.emit_u16(phdr_size)

    # e_phnum: Number of program headers
    state.emit_u16(1)

    # e_shentsize: Section header entry size
    state.emit_u16(64)

    # e_shnum: Number of section headers
    state.emit_u16(0)

    # e_shstrndx: Section name string table index
    state.emit_u16(0)

    # === Program Header (56 bytes) ===

    # p_type: PT_LOAD
    state.emit_u32(0x00000001)

    # p_flags: PF_R | PF_X (readable + executable)
    state.emit_u32(0x00000005)

    # p_offset: File offset of segment
    state.emit_u64(0)

    # p_vaddr: Virtual address
    state.emit_u64(base_addr)

    # p_paddr: Physical address (same as vaddr)
    state.emit_u64(base_addr)

    # p_filesz: Size in file
    state.emit_u64(file_size)

    # p_memsz: Size in memory
    state.emit_u64(file_size)

    # p_align: Alignment
    state.emit_u64(0x1000)

    # === Code Section ===
    state.output.extend(code)

    return bytes(state.output)


def emit_exit_program(exit_code: int = 0) -> bytes:
    """Emit a minimal program that exits with the given code.

    Uses Linux syscall: exit(exit_code)
    """
    state = State()

    # mov rdi, exit_code  (argument 1)
    state.emit_bytes(0x48, 0xC7, 0xC7)  # mov rdi, imm32
    state.emit_u32(exit_code)

    # mov rax, 60  (sys_exit)
    state.emit_bytes(0x48, 0xC7, 0xC0)  # mov rax, imm32
    state.emit_u32(60)

    # syscall
    state.emit_bytes(0x0F, 0x05)

    return bytes(state.output)


def emit_hello_world() -> bytes:
    """Emit a program that prints 'Hello, BLD!' and exits."""
    state = State()

    # The string will be at a known offset after the code
    string_offset = 50  # We'll calculate this precisely

    # --- Code ---

    # mov rax, 1  (sys_write)
    state.emit_bytes(0x48, 0xC7, 0xC0)
    state.emit_u32(1)

    # mov rdi, 1  (stdout)
    state.emit_bytes(0x48, 0xC7, 0xC7)
    state.emit_u32(1)

    # lea rsi, [rip + offset]  (string address)
    state.emit_bytes(0x48, 0x8D, 0x35)  # lea rsi, [rip + disp32]
    # Offset from end of this instruction to string
    current_pos = len(state.output) + 4  # After the disp32
    state.emit_i32(string_offset - current_pos)

    # mov rdx, 12  (length of "Hello, BLD!\n")
    state.emit_bytes(0x48, 0xC7, 0xC2)
    state.emit_u32(12)

    # syscall
    state.emit_bytes(0x0F, 0x05)

    # mov rax, 60  (sys_exit)
    state.emit_bytes(0x48, 0xC7, 0xC0)
    state.emit_u32(60)

    # mov rdi, 0  (exit code)
    state.emit_bytes(0x48, 0xC7, 0xC7)
    state.emit_u32(0)

    # syscall
    state.emit_bytes(0x0F, 0x05)

    # Pad to string_offset
    while len(state.output) < string_offset:
        state.emit_byte(0x90)  # NOP

    # --- Data: "Hello, BLD!\n" ---
    state.output.extend(b"Hello, BLD!\n")

    return bytes(state.output)
