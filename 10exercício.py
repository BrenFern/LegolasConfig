#10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-
#Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite qual é o seu turno, M para matutino ou V para vespertino ou N para Noturno: ")
if turno == "M":
    print("Tenha um bom dia !!!")
elif turno == "V":
    print("Tenha uma boa tarde !!!")
elif turno == "N":
    print("Tenha uma boa noite !!!")
else:
    print("Valor Inválido, por favor digite o seu turno novamente !!!")
