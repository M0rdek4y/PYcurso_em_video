lista = list()
c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Quer continuar? [S/N]')).strip()
    if c in 'Nn':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é:\n{lista}')
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado')
