vum = float(input('Digite o 1º número: '))
vdo = float(input('Digite o 2º número: '))
c = 0
while c != 5:
    c = int(input("""Qual operação deseja realizar:
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa"""))
    if c == 1:
        print('A soma de {} mais {} é igual a {}.'.format(vum, vdo, vum + vdo))
    elif c == 2:
        print('A soma de {} mais {} é igual a {}.'.format(vum, vdo, vum * vdo))
    elif c == 3:
        if vum > vdo:
            print('O número {} é maior do que o número {}.'.format(vum, vdo))
        elif vum < vdo:
            print('O número {} é maior do que o número {}.'.format(vdo, vum))
        else:
            print('O número {} e o número {} são iguais.'.format(vdo, vum))
    elif c == 4:
        vum = float(input('Digite um novo valor para o 1º número: '))
        vdo = float(input('Digite um novo valor para o 2º número: '))
    elif c == 5:
        print('Você saiu do programa.')
    else:
        print('Número invalido!')
