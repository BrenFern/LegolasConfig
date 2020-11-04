#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
#e o preço total.

tamm2 = float(input("Digite o tamanho em metros quadrados da área a ser pintada:"))
pr = 80.0
quantl = (tamm2/3) /18

if quantl == 1:
    print("Você vai precisa de {:.0f} lata de tinta e vai sair por R$ {:.2f}".format(quantl, quantl * 80))
else:
   f = (tamm2/3)//18
   if f == quantl:
       print("Você vai precisa de {:.0f} latas de tintas e vai sair por R$ {:.2f}".format(quantl, quantl * pr))
   else:
        print("Você vai precisa de {:.1f} latas de tintas e vai sair por R$ {:.2f}".format(quantl, quantl * pr))
