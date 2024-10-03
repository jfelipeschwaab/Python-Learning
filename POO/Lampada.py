class Lampada: 
    def __init__(self):
        self.__lampada = False
        self.__intensidade = 0
        
        
        
    def __liga_desliga_lampada(self):
        if self.__intensidade == 0:
            self.__lampada = False
            
        else: 
            self.__lampada = True
            
            
    def __controla_intensidade(self):
        if self.__intensidade == 4:
            self.__intensidade = 0
        else:
            self.__intensidade += 1
            
    def tocar_botao(self):
        return True
    
    
    def mostrar_status(self):
        print("Intensidade da lampada:" + str(self.__intensidade))
        print("Acesa: " + str(self.__lampada))
        
        
    def acoes(self):
        self.__liga_desliga_lampada()
        self.__controla_intensidade()
        
        
        
abajur1 = Lampada()

while True:
    abajur1.acoes()
    
    abajur1.mostrar_status()
    

            
    
        