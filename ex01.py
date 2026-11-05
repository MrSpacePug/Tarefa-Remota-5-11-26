##############################################################################################
# Descrição: Realizar um programa que identifica o maior numero #
#
# Valores se entrada: N1 (primeiro numero inserido pelo usuario)
#                     N2 (segundo numero inserido pelo usuario)
#
# Valores de saida : Nmaior (numero maior entre os dois)
#
##############################################################################################

N1 = float(input('Insira um numero: '))
N2 = float(input('Insira outro numero: '))

if N1 > N2:
    Nmaior = N1
elif N2 > N1:
    Nmaior = N2

print(f'O maior valor é {Nmaior}')