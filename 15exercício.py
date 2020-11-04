#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
#mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoh = float(input("Digite o quanto o você ganha por hora:"))
trabh = float(input("Digite a quantidade de horas trabalhadas no mês:"))
salb = ganhoh * trabh
descimpren = (salb * 11) /100
descinss = (salb * 8) /100
descsind = (salb * 5) /100
salliq = salb - descimpren - descinss - descsind

print("O seu salário bruto é de: R$ {}".format(salb))
print("O total a pagar ao imposto de renda foi de: R$ {}".format(descimpren))
print("O total a pagar ao INSS foi de: R$ {}".format(descinss))
print("O total a pagar ao sindicato foi de: R$ {}".format(descsind))
print("O seu salário liquido é de: R$ {}".format(salliq))
