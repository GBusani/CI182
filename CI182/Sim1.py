
x = int(input('Informe X: '))

if x > 1:
    y = x*x
elif x == 1:
    y = 0
else:
    y = x

print('Y = {:.0f}'.format(y))