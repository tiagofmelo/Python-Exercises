'''
Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar:
a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 
'''

print('Qual o valor total do espetaculo')
total=float(input())
print('Qual o valor de cada convite')
ingresso=float(input())

quantidade = int (total / ingresso)
restodivisao = (total % ingresso)

if restodivisao > 0: quantidadereal = round(quantidade + 0.5)
else: quantidadereal = quantidade

lucro = (total * 1.23)
convitelucro = (lucro / ingresso)
restodivisaolucro = (lucro % ingresso)

if restodivisaolucro > 0: quantidadelucro = round(convitelucro + 0.5)
else: quantidadelucro = int (convitelucro)

print('Devera ser vendido',quantidadereal,'convites para cobrir o custo do espetaculo')
print('Devera ser vendido',quantidadelucro,'convites para ter 23 porcento de lucro')

'''
import math
custo = float (input ())
convite = float (input())
qtde = custo/convite
qtde23 = custo*1.23/convite
print (math.ceil(qtde))
print (math.ceil(qtde23))
'''