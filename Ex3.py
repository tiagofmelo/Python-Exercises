print('Digite um numero')
numero = int(input())

resto1 = (numero % 3)
resto2 = (numero % 5)

if ((resto1) == 0) and ((resto2) == 0):
    print('O numero e divisivel por 3 e 5')
else:
    print('O numero nao e divisivel por 3 e 5')