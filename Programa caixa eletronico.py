#Programa caixa eletronico
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
print('-=-=-' * 10)
print('                BANCO DO BRASIL')
print('-=-=-' * 10)
n1 = int(input('Digite o valor do saque: '))
while n1 > 49:
    n1 = n1 - 50
    cont50 = cont50 + 1
if n1 < 50:
    while n1 >19:
        n1 = n1 - 20
        cont20 = cont20 + 1
if n1 < 20:
    while n1 > 9:
        n1 = n1 - 10
        cont10 = cont10 + 1
if n1 < 10:
    while n1 != 0:
        n1 = n1 - 1
        cont1 = cont1 + 1
print('-=-=-' * 12)
print(f'''Você vai ter que retirar {cont50} Cédulas de R$50
Você vai ter que retirar {cont20} Cédulas de R$20
Você vai ter que retirar {cont10} Cédulas de R$10
Você vai ter que retirar {cont1} Cédulas de R$1''')
print('-=-=-' * 12)