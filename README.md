# Assembler
a. Assembler: The test cases are divided into 3 sets:
i. ErrorGen: These tests are supposed to generate errors
ii. simpleBin: These are simple test cases that are supposed to generate a binary.
iii. hardGen: These are hard test cases that are supposed to generate a
binary.
00000 Addition Performs reg1 =
reg2 + reg3.
If the computation
overflows, then
the overflow flag
is set and 0 is
written in reg1

add reg1 reg2 reg3 A

00001 Subtraction Performs reg1 =
reg2- reg3. In
case reg3 > reg2,
0 is written to
reg1 and overflow
flag is set.

sub reg1 reg2 reg3 A

00010 Move
Immediate

Performs reg1 =
$Imm
where Imm is a 7
bit value.

mov reg1 $Imm B

00011 Move
Register

Move content of
reg2 into reg1.

mov reg1 reg2 C

00100 Load Loads data from
mem_addr into
reg1.

ld reg1 mem_addr D

00101 Store Stores data from
reg1 to mem_addr.

st reg1 mem_addr D

00110 Multiply Performs reg1 =
reg2 x reg3. If
the computation
overflows, then
the overflow flag
is set and 0 is
written in reg1

mul reg1 reg2 reg3 A

00111 Divide Performs
reg3/reg4. Stores
the quotient in R0
and the remainder
in R1. If reg4 is
0 then overflow
flag is set and
content of R0 and
R1 are set to 0

div reg3 reg4 C

01000 Right Shift Right shifts reg1
by $Imm, where
$Imm is a 7 bit
value.

rs reg1 $Imm B

01001 Left Shift Left shifts reg1
by $Imm, where
$Imm is a 7 bit
value.

ls reg1 $Imm B

01010 Exclusive
OR

Performs bitwise
XOR of reg2 and
reg3. Stores the
result in reg1.

xor reg1 reg2 reg3 A

01011 Or Performs bitwise
OR of reg2 and
reg3. Stores the
result in reg1.

or reg1 reg2 reg3 A

01100 And Performs bitwise
AND of reg2 and
reg3. Stores the
result in reg1.

and reg1 reg2 reg3 A

01101 Invert Performs bitwise
NOT of reg2.
Stores the result
in reg1.

not reg1 reg2 C

01110 Compare Compares reg1 and
reg2 and sets up
the FLAGS
register.

cmp reg1 reg2 C

01111 Uncondition
al Jump

Jumps to mem_addr,
where mem_addr is
a memory address.

jmp mem_addr E

11100 Jump If
Less Than

Jump to mem_addr
if the less than
flag is set (less
than flag = 1),
where mem_addr is
a memory address.

jlt mem_addr E

11101 Jump If
Greater
Than

Jump to mem_addr
if the greater
than flag is set
(greater than flag
= 1), where
mem_addr is a
memory address.

jgt mem_addr E

11111 Jump If
Equal

Jump to mem_addr
if the equal flag
is set (equal flag
= 1), where
mem_addr is a
memory address.

je mem_addr E

11010 Halt Stops the machine
from executing
until reset

hlt F

where reg(x) denotes register, mem_addr is a memory address (must be an 7-bit binary
number), and Imm denotes a constant value (must be an 7-bit binary number). The ISA has 7
general purpose registers and 1 flag register. The ISA supports an address size of 7 bits, which
is double byte addressable. Therefore, each address fetches two bytes of data. This results in
a total address space of 256 bytes. This ISA only supports whole number arithmetic. If the
subtraction results in a negative number; for example “3 - 4”, the reg value will be set to 0 and
overflow bit will be set. All the representations of the number are hence unsigned. The registers
in assembly are named as R0, R1, R2, ... , R6 and FLAGS. Each register is 16 bits.
Note: “mov reg $Imm”: This instruction copies the Imm(7bit) value in the register’s lower 7
bits. The upper 9 bits are zeroed out.

Example:
Suppose R0 has 1110_1010_1000_1110 stored, and mov R0 $13 is
executed. The final value of R0 will be 0000_0000_0000_1101.
FLAGS semantics
The semantics of the flags register are:
● Overflow (V): This flag is set by {add, sub, mul, div} when the result of the operation
overflows. This shows the overflow status for the last executed instruction.
● Less than (L): This flag is set by the “cmp reg1 reg2” instruction if reg1 < reg2
● Greater than (G): This flag is set by the “cmp reg1 reg2” instruction if the value of
reg1 > reg2
● Equal (E): This flag is set by the “cmp reg1 reg2” instruction if reg1 = reg2
The default state of the FLAGS register is all zeros. If an instruction does not set the
FLAGS register after the execution, the FLAGS register is reset to zeros.

Binary Encoding
The ISA has 6 types of instructions with distinct encoding styles. However, each
instruction is of 16 bits, regardless of the type.
● Type A: 3 register type
Opcode
(5 bits)

Unused
(2 bits)

reg1
(3 bits)

reg2
(3 bits)

reg3
(3 bits)
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

● Type B: register and immediate type
opcode
(5 bits)

Unused
(1 bit)

reg1
(3 bits)

Immediate Value
(7 bits)

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
● Type C: 2 registers type
Opcode
(5 bits)

Unused
(5 bits)

reg1
(3 bits)

reg2
(3 bits)
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

● Type D: register and memory address type
opcode
(5 bits)

Unused
(1 bit)

reg1
(3 bits)

Memory Address
(7 bits)

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
● Type E: memory address type
opcode
(5 bits)

unused
(4 bits)

Memory Address
(7 bits)

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
● Type F: halt
opcode
(5 bits)

unused
(11 bits)

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

Binary representation for the register are given as follows:-
Register Address
R0 000
R1 001
R2 010
R3 011
R4 100
R5 101
R6 110
FLAGS 111

Executable binary syntax
The machine exposed by the ISA starts executing the code provided to it in the following
format, until it reaches hlt instruction. There can only be one hlt instruction in the whole
program, and it must be the last instruction. The execution starts from the 0

th address. The ISA

follows von-neumann architecture with a unified code and data memory.
The variables must be allocated in the binary in the program order.

Program an assembler for the aforementioned ISA and assembly. The input to the
assembler is a text file containing the assembly instructions. Each line of the text file may be of
one of 3 types:
● Empty line: Ignore these lines
● A label
● An instruction
● A variable definition
Each of these entities have the following grammar:
● The syntax of all the supported instructions is given above. The fields of an instruction
are whitespace separated. The instruction itself might also have whitespace before it. An
instruction can be one of the following:
○ The opcode must be one of the supported mnemonic.
○ A register can be one of R0, R1, ... R6, and FLAGS.
○ A mem_addr in jump instructions must be a label.
○ A Imm must be a whole number <= 127 and >= 0.
○ A mem_addr in load and store must be a variable.
● A label marks a location in the code and must be followed by a colon (:). No spaces are
allowed between label name and colon(:)
● A variable definition is of the following format:

var xyz
which declares a 16 bit variable called xyz. This variable name can be used in
place of mem_addr fields in load and store instructions.
All variables must be defined at the very beginning of the assembly program.
The assembler should be capable of:
1) Handling all supported instructions
2) Handling labels
3) Handling variables
4) Making sure that any illegal instruction (any instruction (or instruction usage) which is not
supported) results in a syntax error. In particular you must handle:
a) Typos in instruction name or register name
b) Use of undefined variables
c) Use of undefined labels
d) Illegal use of FLAGS register
e) Illegal Immediate values (more than 7 bits)
f) Misuse of labels as variables or vice-versa
g) Variables not declared at the beginning
h) Missing hlt instruction
i) hlt not being used as the last instruction
You need to generate distinct readable errors for all these conditions. If you find any
other illegal usage, you are required to generate a “General Syntax Error”.
The assembler must print out all these errors.
5) If the code is error free, then the corresponding binary is generated. The binary file is a
text file in which each line is a 16bit binary number written using 0s and 1s in ASCII. The

assembler can write less than or equal to 128 lines.
Input/Output format:
● The assembler must read the assembly program as an input text file (stdin).
● The assembler must generate the binary (if there are no errors) as an output text file
(stdout).
● The assembler must generate the error notifications along with line number on which the
error was encountered (if there are errors) as an output text file (stdout). In case of
multiple errors, the assembler may print any one of the errors.
