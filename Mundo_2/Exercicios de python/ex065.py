op = 'S'
s = c = menor = maior = 0
while op in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média foi {}'.format(c, s/c))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
