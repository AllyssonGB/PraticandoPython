#Programa com Menu
from time import sleep
n3 = 4
while n3 == 4:
    print('-=-=-' * 5)
    n1 = int(input('\033[33mDigite um valor: '))
    n2 = int(input('\033[33mDigite outro valor: '))
    if n1 and n2 > 0:
        n3 = 10
    while n3 != 4:
        print('\033[31m-=-=-' * 5)
        print('\033[30m    [1] Somar')
        print('    [2] Multplicar')
        print('    [3] Maior')
        print('    [4] Novos Numeros')
        print('\033[30m    [5] Fecha programa')
        print('\033[31m-=-=-' * 5)
        n3 = int(input('Qual opção deseja escolher: '))
        sleep(2)
        if n3 == 1:
            n4 = n1 + n2
            print('\033[32mO resultado da soma entre {} é {} é igual a {}'.format(n1, n2, n4))
        if n3 == 2:
            n4 = n1 * n2
            print('\033[32mO Resultado da multplicaçao entre {} é {} é igual a {}'.format(n1, n2, n4))
        if n3 == 3:
            if n2 > n1:
                print('\033[32m{} e o Maior numero'.format(n2))
            else:
                print('\033[32m{} e o maior numero'.format(n1))
        if n3 == 5:
            print('\033[31mFinalizando Programa...')
            sleep(2)
            print('\033[32mAté a proxima')
            break