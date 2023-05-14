registers = ['000', '001', '010', '011', '100', '101', '110', '111']
reg = 'R'
reg_name = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'flag']
opcode_info = {'add': ['0000000', 'A'],    'sub': ['0000100', 'A'],    'mul': ['0011000', 'A'],    'xor': ['0101000', 'A'],    'or': ['0101100', 'A'],    'and': ['0110000', 'A'],    'mov': ['000100', 'B'],    'rs': ['010000', 'B'],    'ls': ['010010', 'B'],    'div': ['0011100000', 'C'],    'not': ['0110100000', 'C'],    'cmp': ['0111000000', 'C'],    'ld': ['001000', 'D'],    'st': ['001010', 'D'],    'jmp': ['011110000', 'E'],    'jlt': ['111000000', 'E'],    'jgt': ['111010000', 'E'],    'je': ['111110000', 'E'],    'hlt': ['1101000000000000', 'F'] }

b_inst = ['jmp', 'jlt', 'jgt', 'je']
f = open('txt1.txt', 'r')
stdin_list = f.readlines()
f.close()
for i in range(len(stdin_list)):
    d = stdin_list[i].strip().split()
    stdin_list[i] = d

error = 0
var = 0
no_of_ops = 0
n_of_vars = 0
n_of_labels = 0
var_list = []
labels = []
lbl_name = []
lbls = []
d_labels = {}
binary_list = []

for k in range(len(stdin_list)):
    for l in range(len(stdin_list[k])):
        in_list = list(''.join(stdin_list[k][l]))
        if 'var' == stdin_list[k][l]:
            var += 1
        if ':' in in_list:
            i_l = in_list.index(':')
            lbl_name.append(''.join(in_list[0:i_l + 1]))
            lbls.append(''.join(in_list[0:i_l]))
            d_labels.update({''.join(in_list[0:i_l]): k-var})
    else:
        no_of_ops += 1

no_of_ops = no_of_ops - var

for i in range(len(stdin_list)):
    binary = ''
    for j in range(len(stdin_list[i])):
        operation = stdin_list[i][j]
        if 'var' == operation:
            if i < var and 'var' in stdin_list[i]:
                n_of_vars += 1
                ind_var = stdin_list[i].index('var')
                var_list.append(stdin_list[i][ind_var + 1])
                continue
            else:
                error += 1
                print('Error: Variables not declared in the beginning')
                break

        elif stdin_list[i].index(operation) != 0 and stdin_list[i][stdin_list[i].index(operation) - 1] == 'var':
            continue

        elif operation in b_inst and stdin_list[i][1] not in lbls:
            if stdin_list[i][1] in var_list:
                error += 1
                print('Error: variable treated as label')
                break

        elif operation in ['ld', 'st'] and (stdin_list[i][2] not in var_list):
            if stdin_list[i][2] in lbls:
                error += 1
                print('Error: label treated as variable')
                break
            error += 1
            print('Error: Undefined variable')
            break

        elif i >= var and 'var' in stdin_list[i]:
            error += 1
            print('Error: Variables not declared in the beginning')

        elif operation in opcode_info.keys():
            opcode = opcode_info[operation][0]
            op_type = opcode_info[operation][1]

            if opcode == '000100' and ('$' not in list("".join(stdin_list[i]))):
                binary += '0001100000'
                op_type = 'C'
            elif operation in b_inst:
                if stdin_list[i][1] in lbls:
                    n_of_labels += 1
                    ind_label = stdin_list[i].index(operation)                              # labels and branch instructions
                    binary += opcode
                else:
                    error += 1
                    print('Error: Undefined Label')
                    break

            else:
                binary += opcode
            continue

        elif operation in lbls:
            label_value = bin(d_labels[operation])[2:]                                  # add a case for labels
            if len(label_value) <= 7:                                                   # add extra zeros in binary
                n_of_zero3 = 7 - len(label_value)
            else:
                error += 1
                print('Error: General syntax error')
                break
            binary += n_of_zero3 * '0'
            binary += str(label_value)

        elif operation in lbl_name:
            continue

        elif operation in reg_name:
            ind = reg_name.index(operation)
            if ind == 7:
                print('Error: Illegal use of FLAGS register')
                error += 1
                break
            else:
                binary += registers[ind]

        elif '$' in operation:
            num = int(operation[1:])  # immediate value
            bin_num = bin(num)
            bin_num = bin_num[2:]
            if len(bin_num) <= 7:  # add extra zeros in binary
                n_of_zero = 7 - len(bin_num)
            else:
                error += 1
                print('Error: Decimal value more than 127')
                break
            binary += n_of_zero * '0'
            binary += str(bin_num)

        elif operation in var_list:
            var_value = bin(no_of_ops + var_list.index(operation))[2:]              # variable value allocation
            if len(var_value) <= 7:                                                 # add extra zeros in binary
                n_of_zero2 = 7 - len(var_value)
            else:
                error += 1
                print('Error: General Syntax Error')
                break
            binary += n_of_zero2 * '0'
            binary += str(var_value)
        else:
            error += 1
            print('Error: Command/Instruction/Register/Memory not found (Check for Typos)')
            break

    if binary == '':
        continue

    if len(binary) != 16:
        error += 1
        print('Error: General Syntax Error')
        break

    if 'hlt' in stdin_list[i] and i < no_of_ops + var - 1:
        error += 1
        print("Error: Halt not the last instruction")

    if 'hlt' in stdin_list[i]:
        binary_list.append('1101000000000000')
        break

    if i == no_of_ops + var -1 and 'hlt' not in stdin_list[i]:
        error += 1
        print('Error: Missing halt instruction')
        break

    if error >= 1:
        break

    else:
        binary_list.append(binary)

if error == 0:
    for i in range(len(binary_list)):
        print(binary_list[i])
