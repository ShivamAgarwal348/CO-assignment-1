hltflag = False
text_file = open("input1.txt","w")
def Input2():
    #text_file = open("input1.txt","w")
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
            Input(x)
            x1=x.split()

            i+=1
            if(len(x)!=0):
                Line = Line + x1
    
    #print(Line)
    if (Line.count("hlt")>1):
        hltflag = True
            
    #text_file.writelines(Line)

def Input(x):
    #text_file = open("input1.txt","w")
    #complete_input = sys.stdin.read("input1.txt","w"

    x = x + " \n"
    text_file.writelines(x)
    #text_file.close
    return

#text_file = open("input1.txt","w")
#Input2()
text_file.close