#pedir idade apenas em dias

dt = int(input('Diga sua idade em dias: '))

#cálculos
a = dt/365
m = (dt%365)/30
d = (dt%365)%30

print('Sua idade é {:.0f} anos, {:.0f} mêses e {:.0f} dias'.format(a,m,d))