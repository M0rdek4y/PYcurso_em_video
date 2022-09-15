"""teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
"""
"""
galera = [['João', 19], ['Ana', 33], ['Joaquin, 33'], ['Maria', 45]]
for p in galera:
    print(p)
"""
galera = list()
dado = list()
totmaior = totmenor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade.\nTemos {totmenor} menores de idade.')
