primeiro = int(input('Primeiro elemento: '))
razao = int(input('Digite a razão: '))
ultimo = primeiro + (10-1)*razao
ultimo = ultimo + 1
for var in range(primeiro, ultimo, razao):
    print(var, end=' →')
print('FIM!')
