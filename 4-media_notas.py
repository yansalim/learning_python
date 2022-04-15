print('Faça um Programa que peça as 4 notas bimestrais e mostre a média.')

print('Calculadora de notas anuais')


a = input ('insira a primeira nota: \n')
a = int(a)

b = input ('insira a segunda nota: \n')
b = int(b)

c = input ('insira a terceira nota: \n')
c = int(c)

d = input ('insira a quarta nota: \n')
d= int(d)

soma = a + b + c + d
media = (soma/4)
print('a nota total é: ' , soma , 'a média anual é: ' , media )

if media >= 6 :
    print('\n Aprovado')
else:

    print ('\n Reprovado')