print('João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.')

PESO = float(input('Qual o Peso do Peixe? '))

if PESO >= 50:
    base = round( PESO-50 ,2)
    multa = round( base * 4 ,2 )

    print('O peso excedente foi de: ',base,'E a multa será no valor de R$',multa)

else:
    print('UFA!!! VOCÊ NÃO FOI MULTADO !')
