"""cont = n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
    cont += 1
print(cont, s)
"""
cont = n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont}Digitos e a soma deles é {s}')
