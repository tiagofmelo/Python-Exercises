'''
Escreva um programa em Python que leia um número inteiro, entre 0 e 10, e mostre a tabuada deste número multiplicado de 1 até 10.
O valor de entrada dever ser validado, pois o programa somente aceitará números entre 0 e 10 (inclusive). 
Caso o valor de entrada esteja fora do intervalo, o programa emitirá a mensagem VALOR INVÁLIDO e solicitará a entrada desse dado até que ela seja válida.
'''
def escreve (text):
    print(text, end="")

while(True):
    numero = int(input())
    if (numero < 0) or (numero > 10):
        print('VALOR INVÁLIDO')
    else:
        for n in range (1,11):
            num = numero * n
            escreve(numero)
            escreve('x')
            escreve(n)
            escreve('=')
            escreve(num)
            escreve('\n')
            num + 1
        break
'''
Elabore um programa em Python que leia um número inteiro e positivo, calcule e apresente os divisores deste número, separados por um espaço em branco.
O valor de entrada dever ser validado, pois o programa somente aceitará números positivos. Caso o valor de entrada esteja fora do intervalo, o programa emitirá a mensagem VALOR INVÁLIDO e solicitará a entrada desse dado até que ela seja válida.
A saída de dados serão os divisores do número de entrada, apresentados um ao lado do outro, separados por um espaço, conforme caso de teste.
'''
def escreve (text):
    print(text, end=" ")

while(True):
    numero = int(input())
    if (numero <= 0):
        print('VALOR INVÁLIDO')
    else:
        for n in range (1,numero + 1):
            num = numero % n
            if num == 0:
                escreve(n)
        break