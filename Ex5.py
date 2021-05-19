'''
Faça um programa em Python que solicite a quantidade de alunos de uma turma. 
Após esta informação, o usuário deve digitar a média de cada aluno da turma, e o programa apresentará a mensagem PARABÉNS VOCÊ ESTÁ APROVADO aos alunos com média maior ou igual a 6.0.
O programa deve calcular e mostrar, no final da entrada de dados, a média geral da turma. 
Obs.: Caso a quantidade informada de alunos da turma for igual a zero, o programa deve emitir a seguinte mensagem: NÃO HOUVE PROCESSAMENTO.
'''

print('Entre com a quantidade total de alunos que tem na turma')
alunos = int (input())

contagem = 0
soma = 0

while alunos > 0:
    if contagem == alunos:
        break
    print('DIGITE AS NOTAS DOS ALUNOS')
    notas = float (input())
    if notas >= 6:
        print('PARABENS, VOCE ESTA APROVADO')
    soma = soma + notas
    contagem = contagem + 1
if alunos == 0:
    print('NAO HOUVE PROCESSAMENTO')
else:
    print('A MEDIA TOTAL DA SALA E =', soma/alunos)