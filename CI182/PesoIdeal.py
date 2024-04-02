#calcular peso ideal

altura = float(input('Coloque o valor de sua altura em metros:'))
sexo = (input('Coloque o valor de seu sexo biológico (M/F):'))

if sexo == 'M' or sexo == 'm':
    x = (72.7 * altura) - 58
if sexo == 'F' or sexo == 'f':
    x = (62.1 * altura) - 44.7

print('O seu peso ideal é {:.2f}'.format(x))
