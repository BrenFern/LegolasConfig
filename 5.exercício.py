#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
#alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

no1 = float(input("Digite a sua primeira nota:"))
no2 = float(input("Digite a sua segunda nota:"))
med = (no1 + no2) /2
if med >= 7 and med < 10:
    print("A sua média é {}".format(med) + " e você foi aprovado !!!")
elif med == 10:
    print("A sua média é {}".format(med) + " e você foi aprovado com distinção !!!")
elif med > 10:
    print("Porfavor verifique a suas notas, a média limite é 10 !!!")
else:
    print("A sua média é {}".format(med)+ " e você foi reprovado")
    print("kkk")