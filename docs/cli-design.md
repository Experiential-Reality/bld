# BLD CLI Design

## Command Structure

```
bld compile --from <sources> --to <targets> <input> <output>
```

## Examples

```bash
# Compile BLD to native Linux x86-64 ELF
bld compile --from bld --to linux,x86,elf cli.bld bin/bld

# Compile BLD to Python
bld compile --from bld --to python cli.bld cli.py

# Compile BLD to RISC-V Linux ELF
bld compile --from bld --to linux,riscv,elf cli.bld bin/bld-riscv

# Compile BLD to WebAssembly
bld compile --from bld --to wasm cli.bld cli.wasm
```

## Pipeline

The `--to` chain specifies the compilation pipeline:

```
--from bld --to linux,x86,elf

  bld structure
       ↓ (parse)
  ParsedStructure
       ↓ (linux.bld - entry, syscalls, args)
  Linux operations
       ↓ (x86.bld - instruction encoding)
  x86 machine code
       ↓ (elf.bld - binary format)
  ELF executable
```

Each step uses the corresponding .bld structure:
- `linux` → uses=Linux (entry point, syscall interface)
- `x86` → uses=X86 (instruction encoding)
- `elf` → uses=ELF64 (binary format)

## Structures as Pipeline Stages

| Stage | Structure | Input | Output |
|-------|-----------|-------|--------|
| parse | Parser | source text | ParsedStructure |
| linux | Linux | structure | Linux ops (argc, argv, syscalls) |
| x86 | X86 | operations | machine code bytes |
| riscv | RISCV | operations | machine code bytes |
| aarch64 | AArch64 | operations | machine code bytes |
| elf | ELF64 | code + data | ELF binary |
| python | Python | structure | Python source |

## Self-Hosting Path

For the binary to compile itself:

```bash
# Bootstrap (Python compiles BLD)
python -m bld_py compile --from bld --to linux,x86,elf cli.bld bin/bld

# Self-host (BLD compiles BLD)
bin/bld compile --from bld --to linux,x86,elf cli.bld bin/bld2

# Verify fixpoint
diff bin/bld bin/bld2
```

The binary needs to implement this CLI, which means compiling:
1. Argument parsing (--from, --to, input, output)
2. Pipeline dispatch based on --to chain
3. Each pipeline stage as composable structure
