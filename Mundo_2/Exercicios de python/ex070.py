c = con = s = nome = preco = maisq = nmb = vmb = 0
b = '-'*20

print(f'{b}\nLOJA SUPER BARATÂO\n{b}')
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    c += 1
    if c == 1 or preco < vmb:
        nmb = nome
        vmb = preco
    if preco > 1000:
        maisq += 1
    s += preco
    con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if con == 'N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'O total da compra foi R${s}\nTemos {maisq} produtos custando mais de R$1000\nO produto mais barato foi {nmb} que custa R${vmb}')
