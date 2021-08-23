def Inputsim():
    text_file = open("inputsim.txt","w")
    #complete_input = sys.stdin.read("input1.txt","w")
    Line = []
    Lineno = 0
    i=0
    while(i<256):
        try:         
            x = input()
        except EOFError:
            x

        finally:
            '''
            if x == "":
                continue
            '''
            #x1=x.split()

            i+=1
            if (x=="1001100000000000"):
                #Line.append("hlt \n")
                x=x+" \n"
                Line.append(x)
                Lineno+=1
                break
            x = x + " \n"
            Line.append(x)
            Lineno+=1
    text_file.writelines(Line)
    dump = []
    while(i<256):
        x="0000000000000000"
        x = x + " \n"
        dump.append(x)
        i+=1

    text_file.writelines(dump)
    text_file.close
    return

