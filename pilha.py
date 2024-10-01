
#Push --> Insere elementos ao final
#Pop --> Retira o ultimo elemento
#Peek --> Vê o elemento do topo
#FILO --> First In, Last Out

class Pilha:
    
    
    def __init__(self):
        self.pilha = []
        
        
        
    def push(self, e):
        self.stack.append(e)
        
    def pop(self):
        if self.empty:
            self.stack.pop(len(self.stack) - 1)
        
        
    def Peek(self): #Peek, olha o ultimo elemento que foi colocado
        if self.empty:
            return None
            
        return self.stack[-1]
    
    
    def empty(self):
        if len(self.stack) == 0:
            return True
        else: 
            return False
        
        
    def length(self):
        return len(self.stack)