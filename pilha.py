
#Push --> Insere elementos ao final
#Pop --> Retira o ultimo elemento
#Peek --> Vê o elemento do topo
#FILO --> First In, Last Out

class Pilha:
    
    
    def __init__(self):
        self.pilha = []
        self.len_stack = 0
        
        
        
    def push(self, e):
        self.pilha.append(e)
        self.len_stack += 1
        
    def pop(self):
        if not self.empty:
            self.pilha.pop(self.len_stack - 1)
            self.len_stack -= 1
        
        
    def Peek(self): #Peek, olha o ultimo elemento que foi colocado
        if self.empty:
            return None
            
        return self.pilha[-1]
    
    
    def empty(self):
        if self.len_stack == 0:
            return True
        else: 
            return False
        
        
    def length(self):
        return self.len_stack