# pedir tempo em segundos

segs = int(input('Diga o tempo de duração em segundos: '))

#cálculos
h = segs//3600
m = (segs//60)
s = (segs%3600)%60

if m >= 60:
    m = m%60
    



print('A duração é {:.0f} horas, {:.0f} minutos e {:.0f} segundos'.format(h,m,s))