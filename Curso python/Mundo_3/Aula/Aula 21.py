"""def contador(i, f, p):
    '''
    -> FAZ UMA CONTAGEM E MOSTRA NA TELA
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Alan Marques de Aguiar
    '''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


 # Programa principal
help(contador)
"""

"""def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


# Programa principal
somar(3, 2, 5)
somar(8, 4)
somar()
"""
"""def teste():
    x = 8
    print(f'Na função teste, n vale{n}')
    print(f'Na função teste, x vale{x}')


# Programa principal
n = 2
x = 0
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')
teste()
"""

"""def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa principal
a = 5
teste(a)
print(f'A fora vale {a}')"""

"""def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


# Programa principal

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os valores de soma foram {r1}, {r2} e {r3}.')"""


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# Programa principal
num = int(input('Digite um número: '))
print(par(num))
