def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: Parâmetro para mostrar o processor de calculo [True/False]
    :return: Retorna o valor fatorial n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
#print(fatorial(5, show=True))
help(fatorial)
