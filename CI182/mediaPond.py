#pedir 3 notas

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

nf = ((n1 * 2) + (n2 * 3) + (n3 * 5))/10

print('A média final é {:.2f}'.format(nf))