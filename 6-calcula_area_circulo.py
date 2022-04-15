print('Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.')

import math


print('Calcula área de um cículo')

r = input('insira o raio do circulo \n')
r = float(r)

a = math.pi * r**2
a = float(a)

print('a área do círculo de raio', r, 'é de ', a)
