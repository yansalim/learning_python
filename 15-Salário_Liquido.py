print(
    'Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:')
print('a)Salário Bruto:')
print('b)Quanto pagou ao INSS')
print('c)Quanto pagou ao sindicato')
print('d)O Salário liquido')
print('e)Calcule conforme a tabela abaixo: ')

print('+ Salário Bruto : R$')
print('- IR (11%) : R$')
print('- INSS (8%) : R$')
print('- Sindicato ( 5%) : R$')
print('= Salário Liquido : R$')

V = float(input('\n\n\nQual o valor da sua hora trabalhada ? '))
H = float(input('Quantas horas você trabalhou este mês? ' ))
S = bool(input('Deseja contribuir com o sindicato ? (digite s para sim ou n para não): '))

B= V*H
if B >2500:
    I= (B * (11/100))
else:
    I=0
print('+Seu salário bruto é : R$',B)
print('-IR (11%): R$',I)

