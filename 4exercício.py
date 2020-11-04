#. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra:")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or \
   letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
 print("A letra {}".format(letra + " é uma vogal"))
else:
    print("A letra {}".format(letra) + " é uma consoante")