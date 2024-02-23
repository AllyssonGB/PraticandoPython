#Jogo adivinhaçao
from random import randint
from time import sleep
n1 = randint(0, 10)
contador = 0
print('\033[31m-=-=-' * 13)
print('\033[30m        Estou pensando em 1 numero tente adivinha qual')
print('\033[31m-=-=-' * 13)
c = int(input('\033[32mDigite o numero que estou pensando: '))
if c == n1:
    contador += 1
while c != n1:
    c = int(input('\033[31mVoce errou tente mais 1 vez: '))
    if c != n1:
        contador += 1
print('\033[30mParabens vocé acertou o numero {} mais demorou {} tentativas!!!'.format(n1, contador))


