#FIFO (First in, First Out)

#Push
#Pop

class Queue: 
    
    
    def __init__(self):
        self.queue = []
        self.len_queue = 0
        
        
        
    def enqueue(self, e): #Coloca no final da fila
        self.queue.append(e)
        self.len_queue += 1
        
    def dequeue(self): #Tira o primeiro da fila
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1
            
            
    def empty(self): #Ve se está vazia
        if self.len_queue == 0:
            return True
        return False
    
    
    def length(self): #Retorna o tamanho da fila
        return self.len_queue
    
    def front(self): #Retorna o primeiro da fila
        if not self.empty():
            return self.queue[0]
        
        
        
q = Queue()
q.enqueue(2)
q.enqueue(4)        
q.enqueue(3)
q.dequeue()
print(q.front())   #Outputs 4         