#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))
#Maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#Menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))
