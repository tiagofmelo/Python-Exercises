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