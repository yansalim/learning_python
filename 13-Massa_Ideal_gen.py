
print('Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:')


print('a)Para homens: (72.7*h) - 58')
print('b)Para mulheres: (62.1*h) - 44.7')

A = float(input('insira a altura: '))
#B = int(input('insira outro numero inteiro: '))
#C = float(input('insira um número real: '))

H = round((72.7*A)-58,2)
M = round((62.1*A)-44.7,2)
print('O peso ideal para esta altura se for homem é: ', H,'\n')
print('O peso ideal para esta altura se for mulher é: ',M)

