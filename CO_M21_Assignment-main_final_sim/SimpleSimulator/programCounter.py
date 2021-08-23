import bina
class ProgramCounter:
    
    PC=0

    def __init__(self,PC):
        self.PC=PC

    def update(self,nextPC,FLAGS):
        arr=[]
        arr.append(nextPC[:5])
        arr.append(nextPC[8:])
        
        if(arr[0]=="01111" or (arr[0]=="10010" and FLAGS[15]=="1") or (arr[0]=="10001" and FLAGS[14]=="1") or (arr[0]=="10000" and FLAGS[13]=="1")):
            
            self.PC = int(arr[1],2)
        else:
            self.PC+=1
        
              
    def getPC(self):
        return self.PC