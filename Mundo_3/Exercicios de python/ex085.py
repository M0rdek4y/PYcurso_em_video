grupo = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor.'))
    grupo.append(n)
    if n % 2 == 0:
        grupo[0].append(n)
    else:
        grupo[1].append(n)
print('-='*30)
print(f'Os vlaores pares digitados foram: {sorted(grupo[0])}\nOs valores ímpares digitados foram: {sorted(grupo[1])}')
