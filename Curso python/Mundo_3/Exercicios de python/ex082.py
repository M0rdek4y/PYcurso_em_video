lista = list()
listap = list()
listai = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Quer continuar? [S/N]')).strip()
    if c in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        listap.append(c)
    else:
        listai.append(c)
print('=-'*30)
print(f'Você digitou os valores: {lista}')
print(f'Os valores pares são: {listap}')
print(f'Os valores impares são: {listai}')
