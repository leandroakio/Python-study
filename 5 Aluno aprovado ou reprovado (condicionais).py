nome =  input('Digite o nome do aluno: ')
nota1 = float(input('Digite nota da prova 1: '))
nota2 = float(input('Digite nota da prova 2: '))
faltas = int(input('Digite o número de faltas do aluno: '))
media = (nota1+nota2)/2
assid = (20-faltas)/20

if assid>=0.7 and media >=0.6:
    resultado = 'Aprovado'
elif assid<0.7 and media <0.6:
    resultado = 'Reprovado por média e faltas'
elif assid<0.7:
    resultado = 'Reprovado por faltas'
elif media<0.6:
    resultado = 'Reprovado por média'

else:
    print('Erro')

print('Nome: ',nome)
print('Média:',media)
print('Assiduidade :',str(assid*100)+'%')
print('Resultado: ', resultado)

