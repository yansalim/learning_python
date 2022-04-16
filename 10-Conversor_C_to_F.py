print('Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.')

C = float (input('insira o Valor em Celsius para ser convertido: '))

F = (C*1.8) + 32
F = round(F,2)

print('A temperatura em Fahrenheit é: ', F)