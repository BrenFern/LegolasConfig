#1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
maior = n1
if n2>n1:
    maior = n2
print("O maior número é {}".format(maior))