def Input():
    text_file = open("input1.txt","w")
    #complete_input = sys.stdin.read("input1.txt","w")
    Line = []
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
            x1=x.split()

            i+=1
            if (x=="hlt" or "hlt" in x1):
                #Line.append("hlt \n")
                x=x+" \n"
                Line.append(x)
                break
            x = x + " \n"
            Line.append(x)
    text_file.writelines(Line)
    text_file.close
    while(i<256):
        x=""
        try:         
            x = input()
        except EOFError:
            x

        finally:
            '''
            if x == "":
                continue
            '''
            if(x=="hlt"):
                print("ERROR : More than 1 halt statements")
                exit(1)
            x1=x.split()
            
            i+=1
            if (len(x1)>1):
                print("ERROR : halt statement is in the middle")
                exit(1)
    return