lista = list()
mai = men = 0
for c, p in enumerate(range(0, 5)):
    lista.append(int(input(f'DIgite o {c+1}º valor: ')))
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {max(lista)} nas posições ', end='')
for i, c in enumerate(lista):
    if lista[i] == max(lista):
        print(f'{i+1}... ', end='')
print(f'\nO menor valor foi {min(lista)} nas posições ', end='')
for i, c in enumerate(lista):
    if lista[i] == min(lista):
        print(f'{i+1}... ', end='')
