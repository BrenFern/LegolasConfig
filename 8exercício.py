#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo
#que a decisão é sempre pelo mais barato.
prod1 = float(input("Digite o preço do primeiro produto:"))
prod2 = float(input("Digite o preço do segundo produto:"))
prod3 = float(input("Digite o preço do terceiro produto:"))
menor = prod1
if prod2 < prod1 and prod2 < prod3:
    menor = prod2
if prod3 < prod1 and prod3 < prod2:
    menor = prod3
print("Você deve comprar o produto que custa R$ {}".format(menor))