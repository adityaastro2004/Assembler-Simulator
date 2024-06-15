# Assembler for Custom ISA

This repository contains an assembler for a custom Instruction Set Architecture (ISA) as described below. The assembler reads assembly instructions from an input text file and outputs the corresponding machine code in binary format. If any syntax or semantic errors are encountered in the input, the assembler generates appropriate error messages.

## Features

- Supports all instructions defined in the ISA.
- Handles labels and variables.
- Checks for various syntax and semantic errors.
- Generates readable error messages for all error conditions.
- Outputs the machine code in a binary format.

## ISA Overview

The custom ISA supports the following instructions and registers. Each instruction is 16 bits long and falls into one of six types: A, B, C, D, E, and F.

### Instructions

| Opcode | Instruction   | Description                                                                                             | Type |
|--------|---------------|---------------------------------------------------------------------------------------------------------|------|
| 00000  | add           | Adds reg2 and reg3, stores result in reg1. Sets overflow flag if overflow occurs.                        | A    |
| 00001  | sub           | Subtracts reg3 from reg2, stores result in reg1. Sets overflow flag if reg3 > reg2.                      | A    |
| 00010  | mov           | Moves immediate value to reg1.                                                                          | B    |
| 00011  | mov           | Moves value of reg2 to reg1.                                                                             | C    |
| 00100  | ld            | Loads data from memory address into reg1.                                                               | D    |
| 00101  | st            | Stores data from reg1 to memory address.                                                                | D    |
| 00110  | mul           | Multiplies reg2 and reg3, stores result in reg1. Sets overflow flag if overflow occurs.                  | A    |
| 00111  | div           | Divides reg3 by reg4, stores quotient in R0 and remainder in R1. Sets overflow flag if reg4 is 0.        | C    |
| 01000  | rs            | Right shifts reg1 by immediate value.                                                                   | B    |
| 01001  | ls            | Left shifts reg1 by immediate value.                                                                    | B    |
| 01010  | xor           | Bitwise XOR of reg2 and reg3, stores result in reg1.                                                    | A    |
| 01011  | or            | Bitwise OR of reg2 and reg3, stores result in reg1.                                                     | A    |
| 01100  | and           | Bitwise AND of reg2 and reg3, stores result in reg1.                                                    | A    |
| 01101  | not           | Bitwise NOT of reg2, stores result in reg1.                                                             | C    |
| 01110  | cmp           | Compares reg1 and reg2, sets FLAGS register.                                                            | C    |
| 01111  | jmp           | Unconditional jump to memory address.                                                                   | E    |
| 11100  | jlt           | Jump to memory address if less than flag is set.                                                        | E    |
| 11101  | jgt           | Jump to memory address if greater than flag is set.                                                     | E    |
| 11111  | je            | Jump to memory address if equal flag is set.                                                            | E    |
| 11010  | hlt           | Halts the machine.                                                                                      | F    |

### Registers

The ISA has 7 general-purpose registers (R0-R6) and 1 FLAGS register. Each register is 16 bits wide.

### Flags

- **Overflow (V):** Set by `add`, `sub`, `mul`, `div` when the result overflows.
- **Less than (L):** Set by `cmp` if reg1 < reg2.
- **Greater than (G):** Set by `cmp` if reg1 > reg2.
- **Equal (E):** Set by `cmp` if reg1 = reg2.

### Instruction Formats

- **Type A:** 3 register type
  ```
  Opcode (5 bits) | Unused (2 bits) | reg1 (3 bits) | reg2 (3 bits) | reg3 (3 bits)
  ```

- **Type B:** Register and immediate type
  ```
  Opcode (5 bits) | Unused (1 bit) | reg1 (3 bits) | Immediate Value (7 bits)
  ```

- **Type C:** 2 register type
  ```
  Opcode (5 bits) | Unused (5 bits) | reg1 (3 bits) | reg2 (3 bits)
  ```

- **Type D:** Register and memory address type
  ```
  Opcode (5 bits) | Unused (1 bit) | reg1 (3 bits) | Memory Address (7 bits)
  ```

- **Type E:** Memory address type
  ```
  Opcode (5 bits) | Unused (4 bits) | Memory Address (7 bits)
  ```

- **Type F:** Halt
  ```
  Opcode (5 bits) | Unused (11 bits)
  ```

## Error Handling

The assembler checks for the following errors:

- **Syntax errors:** Typos in instruction names or register names.
- **Semantic errors:** Use of undefined variables or labels, illegal use of FLAGS register, illegal immediate values, misuse of labels as variables or vice-versa, variables not declared at the beginning, missing `hlt` instruction, and `hlt` not being the last instruction.
- **General Syntax Error:** Any other illegal usage.

## Usage

### Input Format

The input assembly file can contain:

- Empty lines (ignored).
- Labels (e.g., `label:`).
- Instructions (e.g., `add R1 R2 R3`).
- Variable definitions (e.g., `var xyz`).

Variables must be declared at the beginning of the program.

### Output

The assembler outputs either:

- A text file with the machine code in binary format (each line is a 16-bit binary number).
- An error message with the line number on which the error was encountered.

### Running the Assembler

To run the assembler, execute the following command:

```bash
python assembler.py input_file.asm output_file.bin
```

### Example

```assembly
var a
var b
add R1 R2 R3
mov R0 $13
jmp end
label1:
sub R1 R2 R3
end:
hlt
```

## License

This project is licensed under the MIT License.

---

Feel free to contribute by opening issues or submitting pull requests.
