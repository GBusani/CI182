
n = int(input('Digite um valor de 4 dígitos: '))

#Dezenas
d1 = n // 100
d2 = n % 100

#Dígitos de n
n1 = n % 10
n2 = (n // 10) % 10
n3 = (n // 100) % 10
n4 = n // 1000

#Teste 1
SomaDez = d1 + d2
Teste1 = (SomaDez)**2

#Soma dos dígitos de SomaDez
S1 = SomaDez % 10
S2 = SomaDez // 10
SomaN = n1 + n2 + n3 + n4

#Teste 2
Teste2 = S1 + S2

if n == Teste1 and SomaN == Teste2:
    print(n,' é especial!')
else:
    print(n, 'não é especial')