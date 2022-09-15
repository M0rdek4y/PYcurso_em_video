def title(txt):
    print('-' * 30, f'\n{txt}')
    print('-' * 30)


def area():
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


# Programa principal
title(f'{"Controle de Terrenos":.^30}')
area()
