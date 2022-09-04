con = s = ci = cm = cf = maiorid = 0
b = '-'*20

print(f'{b}\nCADASTRE UMA PESSOA\n{b}')
while con != 'N':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Tente novamente!')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maiorid += 1
    if sexo == 'F' and idade < 20:
        cf += 1
    if sexo == 'M':
        cm += 1
    con = str(input(f'{b}\nQuer continuar? [S/N]')).strip().upper()[0]
    while con not in 'SN':
        print('Tente novamente!')
        con = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if con == 'S':
        print(f'{b}\nCADASTRE UMA PESSOA\n{b}')
    else:
        break
print(f'Total de pessoas com mais de 18 anos: {maiorid}\nAo todo temos {cm} homens cadastrados\nE temos {cf} mulheres com menos de 20 anos')
