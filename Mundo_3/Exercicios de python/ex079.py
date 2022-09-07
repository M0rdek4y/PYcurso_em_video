lista = list()
c = 0

while True:
    valor = int(input('Digite um valor'))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    c = str(input('Quer continuar? [S/N]')).strip().upper()
    if c == 'N':
        break
print('=-'*30)
print(f'\n Você digitou os valores: {sorted(lista)}')
