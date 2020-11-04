from time import sleep
tam=int(input('Digite o tamanho do arquivo em Mb: '))
vel=int(input('Quantos MB/s: '))
re=tam/vel
ree=re/60
if ree >= 60 :
    while ree >= 60 :
        print('O download demorará aproximadamente {:.2f} minutos.'.format(ree))
        sleep(60)
        ree-=1
if ree < 60:
    while ree < 60 and ree > 0 :
        print('O download demorará aproximadamente {:.2f} minutos.'.format(ree))
        sleep(1)
        ree -= 0.11
    print('Acabou!!!!!')
    