#Linked List

class Node:
    
    def __init__(self, label):
        self.label = label
        self.next_node = None

    def getLabel(self):
        return self.label
    
    def setLabel(self, label):
        self.label = label
        
        
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next):
        self.next_node = next
        
        
class LinkedList:
    
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.len_list = 0
        
        
    def push(self, label, index):
        
        if index >= 0:
            #cria o novo nó
            node = Node(label)
            
            
            if self.empty():
                self.first_node = node
                self.last_node = node
                
            
            else:
                if index == 0:
                    #Inserção no início
                    node.set_next_node(self.first_node)
                    self.first_node = node
                    
                elif index >= self.len_list:
                    #Inserção no final
                    self.last_node.set_next_node(node)
                    self.last_node = node
                    
                else: 
                    #Inserção no meio
                    prev_node = self.first_node
                    curr_node = self.first_node.get_next_node()
                    curr_index = 1
                    
                    while curr_node != None:
                        
                        if curr_index == index:
                            #Seta o curr_node como o próximo node
                            node.set_next_node(curr_node)
                            #Seta o node como próximo do prev_node
                            prev_node.set_next_node(node)
                            
                            break
                        
                        prev_node = curr_node
                        curr_node = curr_node.get_next_node()
                        curr_index += 1
                        
                        
                        
            self.len_list += 1
                        
                        
                        
    def pop(self, index):
        
        if not self.empty() and index >= 0 and index <self.len_list:
            flag_remove = False
            
            if self.first_node.get_next_node() == None:
                #Possui apenas um elemento
                self.first_node = None
                self.last_node = None
                flag_remove = True
                
            elif index == 0:
                #Remove do inicio, mas possui mais de um elemento
                self.first_node = self.first_node.get_next_node()
                if self.first_node is None:
                    self.last_node = None
                flag_remove = True
                
            else:
                
                '''
                Se chegou até aqui, o elemento a ser removido está no meio
                '''
                
                prev_node = self.first_node
                curr_node = self.first_node.get_next_node()
                curr_index = 1
                
                
                while curr_node != None:
                    if index == curr_index:
                        #O proximo do anterior tem que apontar para o próximo do nó atual
                        prev_node.set_next_node(curr_node.get_next_node())
                        
                        if curr_node.get_next_node() is None:
                            self.last_node = prev_node
                            
                        curr_node.set_next_node(None)
                        flag_remove = True
                        break
                    
                    prev_node = curr_node
                    curr_node = curr_node.get_next_node()
                    curr_index += 1
                    
                    
                    
            if flag_remove:
                self.len_list -= 1
                
                
    def empty(self):
        if self.first_node == None:
            return True
        
        else: 
            return False      
        
        
    def length(self):
        return self.len_list
    
    
    
    def show(self):
        
        curr_node = self.first_node
        
        while curr_node != None:
            print(curr_node.getLabel(), end = ' ')
            # print(str(curr_node.getLabel()) + " Aponta para:" + str(curr_node.get_next_node))
            curr_node = curr_node.get_next_node()
            
        print('')
        
        


lista = LinkedList()


# Teste de inserção
lista.push("Marcos", 0)
lista.show()
lista.push("Joao", 1)
lista.show()
lista.push("Yankee", 0)
lista.show()
lista.push("Catarina", 2)
lista.show()
lista.push("Lilica", 4)
lista.show()
lista.push("Sara", 2)
lista.show()
print("Tamanho da lista: %d\n" % lista.length())


#Teste de remoção
lista.pop(0)
lista.show()
lista.pop(2)
lista.show()
lista.pop(4)
lista.show()
lista.pop(3)
lista.show()
print("Tamanho da lista: %d\n" % lista.length())

        
                
                
                
                        
                    
                            
            
            
        
        