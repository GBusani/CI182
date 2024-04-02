
n = int(input('Digite um valor de 3 dígitos: '))

d1 = n % 10
d2 = (n // 10) % 10
d3 = n // 100

soma = d1 + d2 + d3

if soma % 2 == 0:
    print('Soma par = {}'.format(soma))

else:
    produto = d1 *d2 * d3
    print('Soma impar. Produto = {}'.format(produto))