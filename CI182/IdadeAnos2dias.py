#Pedir anos, mêses e dias

print('Diga sua idade em:')
a = int(input('Anos:'))
m = int(input('Mêses:'))
d = int(input('Dias:'))

#cáculos
d1 = a * 365
d2 = m * 30
d = d + d1 + d2

print('Você já viveu {:.0f} dias'.format(d))