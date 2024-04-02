#calculo do valor do desconto

preco = float(input('Preço do produto: '))
cond = int(input('Condição de pagamento: '))

if cond == 1:
    preco = preco * 9/10
if cond == 2:
    preco = preco * 17/20
if cond == 4:
    preco = preco * 11/10

print('Valor a pagar: {:.2f}'.format(preco))

