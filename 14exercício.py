#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
#trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado
#de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um
#programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
#de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do
#programa com as mensagens adequadas.

peso = float(input("Digite o peso total de peixes: "))
if peso <= 50 :
    print("O peso total se encontra dentro do regulamento")
    print("Você pescou {}".format(peso) + " quilos de peixe")
else:
    excesso = peso -  50
    multa = excesso * 4
    print("Você pescou {}".format(peso) + " quilos de peixe")
    print("O seu excesso de peixe foi de {}".format(excesso) + " quilos de peixes")
    print("Devido ao excesso de quilos peixes o valor da sua multa é de: R$ {}".format(multa))