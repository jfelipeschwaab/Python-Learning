class minhaClasseEstatica:
    __minha_variavel = 0
    
    
    @staticmethod
    def meu_metodo_estatico():
        return minhaClasseEstatica.__minha_variavel
    
    

import math

class Calculadora:
    @staticmethod
    def raiz_quadrada(n):
        return math.sqrt(n)
    
    
    
print(Calculadora.raiz_quadrada(16))
#Faz sentido ter um método estático raiz_quadrada, pois sua execução não depende de uma variável de instância