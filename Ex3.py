'''
Faça um programa em Python para resolver o seguinte problema:
O programa deve receber um número inteiro, digitado pelo usuário, e apresentar uma mensagem:
- se o número que o usuário digitou for divisível por 3 e por 5 ao mesmo tempo, a mensagem será: O número é divisível por 3 e 5.
- se o número que o usuário digitou não for divisível por 3 e por 5 ao mesmo tempo, a mensagem será: O número não é divisível por 3 e 5. 
'''

print('Digite um numero')
numero = int(input())

resto1 = (numero % 3)
resto2 = (numero % 5)

if ((resto1) == 0) and ((resto2) == 0):
    print('O numero e divisivel por 3 e 5')
else:
    print('O numero nao e divisivel por 3 e 5')