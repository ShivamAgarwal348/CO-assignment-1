def Input():
    text_file = open("input1.txt","w")
    Line = []
    i=0
    while(i<=256):
        x = input()
        if x == "":
            continue
        i+=1
        if (x=="hlt"):
            Line.append("hlt \n")
            break
        x = x + " \n"
        Line.append(x)
    text_file.writelines(Line)
    text_file.close()
    return
