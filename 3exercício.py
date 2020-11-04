#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M -
#Masculino, Sexo Inválido.

resposta = input("Diga qual é o seu sexo, M ou F:")
if resposta == "M":
    print("Você é do sexo masculino")
elif resposta == "F":
    print("Você é do sexo feminino")
else:
    print("Porfavor digite novamente o seu sexo, M ou F")        