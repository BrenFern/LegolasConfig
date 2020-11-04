#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
# ,utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura:"))
sexo = input("Digite o seu sexo:")
if sexo == "masculino":
    peso = float((72.7* altura)) - 58
    print("O seu sexo é "+ sexo +" e o seu peso ideal é {}".format(peso))
elif sexo == "feminino":
    peso = float((62.1* altura)) - 44.7
    print("O seu sexo é "+ sexo +" e o seu peso ideal é {}".format(peso))
else:
     print("Porfavor digite o seu sexo novamente !!!(masculino ou feminino)")      
    