primeiro = int(input('Primeiro elemento: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
total = 0
n = 10
while n != 0:
    total = total + n
    while c <= total:
        print('{}'.format(termo), end=' → ')
        termo += razao
        c += 1
    print('PAUSA')
    n = int(input('\nQuantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
