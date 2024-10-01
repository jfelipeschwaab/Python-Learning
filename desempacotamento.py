lista = [1,2,3]


a, b, c = lista

print(a)
print(b)
print(c)


tupla = (1,2,3)

a1, a2, a3 = tupla

print(a1)
print(a2)
print(a3)


nome = 'abc'

c1, c2, _ = nome

print(c1)
print(c2)


def func(x,y = 3):
    return x**2, y**2 #Posso retornar uma tupla de uma função


print(func(2,3))

r1, r2 = func(2,3) #Desempacotando essa tupla

print(r1)
print(r2)