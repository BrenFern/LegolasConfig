#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo .
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.

n1int = int(input("Digite o primeiro número inteiro:"))
n2int = int(input("Digite o segundo número inteiro:"))
nreal = float(input("Digite um número real:"))
a = (n1int * 2) * (n2int/2)
b = (n1int * 3) + (nreal)
c = nreal ** 3 
print(a)
print(b)
print(c)