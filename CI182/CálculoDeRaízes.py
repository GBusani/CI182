import math
#pedir os valores de a, b e c
a = float(input('Coloque o valor de a:'))
b = float(input('Coloque o valor de b:'))
c = float(input('Coloque o valor de c:'))

#cálculo
d = (b*b - 4*a*c)

if d < 0:
    print('Não há raízes reais, pois delta é negativo')
    exit()

#cálculos das raízes
delta = math.sqrt(d)
x1 = (-b + delta)/(2*a)
x2 = (-b - delta)/(2*a)

#duas raízes
if x1 != x2:
    print('As raízes da equação são {:.2f} e {:.2f}'.format(x1,x2))

#uma raiz
else:
    print('A raiz da equação é {:.2f}'.format(x1))