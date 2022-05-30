print('Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a'
      ' seguinte fórmula: (72.7*altura) - 58')



A = float(input('insira a altura: '))
#B = int(input('insira outro numero inteiro: '))
#C = float(input('insira um número real: '))

print('O peso ideal para esta altura é: \n')

A = round((72.7*A)-58 ,2)
print(A)