import symbol_table
import opcode_table
import binary
import input
import errors

input.Input()


text_file = open("input1.txt",'r')
Lines = text_file.readlines()

Symbol_table = symbol_table.symbols(Lines)

for line in Lines :
    
    l = list(errors.identifyE(line,Symbol_table))
    if (len(l) == 0):
        continue

    elif l[0] == True and len(l)!=0 :
        print(l[1])
        continue

    
    words = line.split()
    
    if (len(words) == 0):
        continue
    
    output = ""

    if words[0] in opcode_table.opcode:
        output = opcode_table.opcode[words[0]][0]

        if (words[0] == "mov"):
            if (words[2][0] == "$"):
                output = "00010" + opcode_table.registers[words[1]] + binary.binary(int(words[2][1:]))
            else :
                output = "0001100000" + opcode_table.registers[words[1]] + opcode_table.registers[words[2]]

        else :
            Type = opcode_table.opcode[words[0]][1] 

            if (Type == 'A'):
                output = output + "00" + opcode_table.registers[words[1]] + opcode_table.registers[words[2]] + opcode_table.registers[words[3]]

            elif(Type == 'B'):
                output = output + opcode_table.registers[words[1]] + binary.binary(int(words[2][1:]))
        
            elif(Type == 'C'):
                output = output + "00000" + opcode_table.registers[words[1]] + opcode_table.registers[words[2]]

            elif(Type == 'D'):
                output = output + opcode_table.registers[words[1]] + Symbol_table[words[2]][1]

            elif(Type == 'E'):
                output = output + "000" + Symbol_table[words[1]][1]

            elif(Type == 'F'):
                output = output + "00000000000"
    elif(words[0][-1] == ':') :
        output = opcode_table.opcode[words[1]][0]

        if (words[1] == "mov"):
            if (words[3][0] == "$"):
                output = "00010" + opcode_table.registers[words[2]] + binary.binary(int(words[3][1:]))
            else :
                output = "00011" + opcode_table.registers[words[2]] + opcode_table.registers[words[3]]

        else :
            Type = opcode_table.opcode[words[1]][1] 

            if (Type == 'A'):
                output = output + "00" + opcode_table.registers[words[2]] + opcode_table.registers[words[3]] + opcode_table.registers[words[4]]

            elif(Type == 'B'):
                output = output + opcode_table.registers[words[2]] + binary.binary(int(words[3][1:]))
        
            elif(Type == 'C'):
                output = output + "00000" + opcode_table.registers[words[2]] + opcode_table.registers[words[3]]

            elif(Type == 'D'):
                output = output + opcode_table.registers[words[2]] + Symbol_table[words[3]][1]

            elif(Type == 'E'):
                output = output + "000" + Symbol_table[words[2]][1]

            elif(Type == 'F'):
                output = output + "00000000000"

        
    print(output)

