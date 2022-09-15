primeiro = int(input('Primeiro elemento: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
while c <= 10:
    print('{}'.format(termo), end=' →')
    termo += razao
    c += 1
print('FIM!')
