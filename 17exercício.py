tmm2 = float(input('Quantos metros quadrados vai ser pintada: '))
pr = 80.0
pr2 = 25.0
l = input('Você vai compra somente lata(s): ').capitalize()
if l == 'Sim' or l == 'S' or l == 'Yes' or l == 'Y':
    quantl = (tmm2/6)/18
    if quantl == 1:
        print('Você vai precisa de {:.0f} lata de tinta e vai sair por R$ {:.2f}'.format(quantl, quantl * pr))
    else:
        f = (tmm2 / 6) // 18
        if f == quantl:
            print('Você vai precisa de {:.0f} latas de tintas e vai sair por R$ {:.2f}'.format(quantl, quantl * pr))
        else:
            print('Você vai precisa de {:.1f} latas de tintas e vai sair por R$ {:.2f}'.format(quantl, quantl * pr))
else:
    l = input('Você vai compra somente galões: ').capitalize()
    if l == 'Sim' or l == 'S' or l == 'Yes' or l == 'Y':
        t = (tmm2 / 6) / 3.6
        if quantl == 1:
            print('Você vai precisa de {:.0f} galão de tinta e vai sair por R$ {:.2f}'.format(quantl, quantl * pr2))
        else:
            f = (tmm2/ 6) // 3.6
            if f == quantl:
                print('Você vai precisa de {:.0f} galões de tintas e vai sair por R$ {:.2f}'.format(quantl, quantl * pr2))
            else:
                print('Você vai precisa de {:.1f} galões de tintas e vai sair por R$ {:.2f}'.format(quantl, quantl * pr2))
    else:
        ga = float(input('Quantos galõe(s) vai ser: '))
        la = float(input('Quantos lata(s) vai ser: '))
        pa = ga * pr2
        pl = la * pr
        ta = (((pa+pl)*10)/100)+pa+pl
        print('Vai ser {:.1f} lata(s) e {:.1f} galões que vai sair por R$ {:.2f} \nAviso cada litro é seis metros quadrados,ou seja , uma lata é 108 metros quadrados e um galão é 21.6 metros quadrados'.format(la, ga,ta))

