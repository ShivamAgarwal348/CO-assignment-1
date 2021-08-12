#machine code,type(already stores num of operands),num of operands
#How do I account for registers or immediate operands?
#How do i account for 2 mov
opcode ={"add":("00000","A",3),
"sub":("00001","A",3),
"mov":(("00010","B",2),("00011","C",2)),
"ld":("00100","D",2),
"st":("00101","D",2),
"mul":("00110","A",3),
"div":("00111","C",2),
"rs":("01000","B",2),
"ls":("01001","B",2),
"xor":("01010","A",3),
"or":("01011","A",3),
"and":("01100","A",3),
"not":("01101","C",2),
"cmp":("01110","C",2),
"jmp":("01111","E",2),
"jlt":("10000","E",2),
"jgt":("10001","E",2),
"je":("10010","E",2),
"hlt":("10011","F",0)}

registers = {"R0":"000","R1":"001",
"R2":"010","R3":"011","R4":"100",
"R5":"101","R6":"110","FLAGS":"111",}