print('Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.')

s = input('digite o valor da sua hora de trabalho: \n')
s = float(s)

h = input ('digite quantas horas você trabalha por mes: \n')


salario =  (s * h)


print('o seu salário mensal é de: \n', 'R$ ', salario)