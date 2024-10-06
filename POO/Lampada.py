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



    
    
class Abajur(Lampada):
    def __init__(self, modelo):
        super().__init__()
        self.modelo = modelo
        self.preco = 1000

    
    def minha_marca(self):
        print("Minha marca é: " + str(self.modelo))
        
    def acoes(self):
        super().acoes()
        print("Meu método de ações é top")
    


meu_abajur = Abajur("LG")
meu_abajur.mostrar_status()
meu_abajur.minha_marca()
meu_abajur.acoes()
meu_abajur.mostrar_status()



    

            
    
        