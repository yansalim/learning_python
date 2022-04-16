
print ('Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.')

F = float (input('Insira a temperatura em Fahrenheit: '))


C = (F - 32) * (5 / 9)
C = round(C, 2)


print ('A temperatura  em Celcius é: ', C)