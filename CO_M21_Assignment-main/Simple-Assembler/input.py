def Input():
    text_file = open("input1.txt","w")
    Line = []
    i=0
    while(i<256):
        try:         
            x = input()
        except EOFError:
            x

        finally:
            i +=1
            x = x + "\n"
            Line.append(x)
    text_file.writelines(Line)
    text_file.close()
    return
