# BLD Project Structure

## Directory Layout

```
bld/
├── bin/                    # Compiled binaries
│   ├── hello               # Hello world
│   └── bld                 # Compose CLI
├── docs/                   # Documentation
│   ├── bld-format.md       # Format reference
│   └── structure.md        # This file
└── src/                    # BLD source files
    ├── arch/               # Architecture definitions
    │   └── x86/            # x86-64
    │       ├── mov.bld     # MOV structure
    │       ├── rex.bld     # REX prefix
    │       ├── modrm.bld   # ModR/M byte
    │       ├── opcode/     # Opcode values
    │       └── abi/        # Calling conventions
    ├── format/             # Binary formats
    │   └── elf/            # ELF64
    │       ├── header.bld  # ELF header structure
    │       ├── phdr.bld    # Program header
    │       └── minimal.bld # Crystallized header
    ├── os/                 # OS interfaces
    │   └── linux/          # Linux syscalls
    ├── program/            # Programs
    │   ├── hello.bld       # Hello world
    │   ├── hello/code.bld  # Hello code
    │   ├── cli.bld         # Compose CLI
    │   └── cli/code.bld    # CLI code
    ├── b.bld               # Planck unit (0..1)
    ├── byte.bld            # 8 bits
    ├── compose.bld         # Algorithm spec
    └── rules.bld           # BLD rules
```

## File Categories

### Structure Files
Define B/L relationships. Compose by following paths.

Example: `mov.bld`
```
prefix: arch/x86/rex
opcode: arch/x86/opcode/mov
modrm: arch/x86/modrm
```

### Value Files
Define enumerated constants with field syntax.

Example: `os/linux/syscall.bld`
```
read: 0
write: 1
open: 2
close: 3
exit: 60
```

### Sequential Files
Position = value. No field names needed.

Example: `arch/x86/opcode/jcc.bld`
```
o
no
b
ae
e
ne
```

### Crystallized Files
Direct byte emission. Final compiled form.

Example: `program/hello/code.bld`
```
# mov rax, 1
0x48
0xC7
0xC0
0x01
0x00
0x00
0x00
# syscall
0x0F
0x05
```

### Composition Files
Link files together.

Example: `program/hello.bld`
```
format/elf/minimal
program/hello/code
```

## Building

Using Python bootstrap:
```bash
cd bld
PYTHONPATH=../bld-py/src python -m bld_py.compose compose program/hello bin/hello
chmod +x bin/hello
```

Using native CLI (once built):
```bash
bin/bld program/hello > bin/hello2
chmod +x bin/hello2
```

## Cost Analysis

Structure has cost: `Cost = B + D × L`

- **Crystallized** (e.g., `hello/code.bld`): High B, zero L → bytes inline
- **Composed** (e.g., `hello.bld`): Low B, high L → paths to files
- **Structure** (e.g., `mov.bld`): Medium B, medium L → reusable templates
