##############################################################################################
# Descrição: Realizar um programa que identifica se um numero é positivo ou negativo
#
# Valores se entrada: N (um numero inserido pelo usuario)
#
#
# Valores de saida : apenas a resposta se o numero é positivo ou negativo
#
##############################################################################################

N = float(input('Insira um numero: '))

if N > 0:
    print('N é um numero positivo')
elif 0 > N:
    print('N é um numero negativo')
else:
    print('N é um numero nulo')
