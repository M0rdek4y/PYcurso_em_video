def fatorial(n):
    """
    -> Calcula o fatorial de um número.
    :param n: Recebe o valor a ser calculado.
    :return: Retorna o fatorial
    """
    f = 1
    for n in range(1, n+1):
        f *= n
    return f


def dobro(n):
    """
    -> Calcula o dobro de um número
    :param n: Recebe o valor a ser dobrado
    :return: Retorna o dobro.
    """
    return n * 2


def triplo(n):
    """
    -> Calcula o triplo de um número
    :param n: Recebe o valor a ser triplicado
    :return: Retorna o triplo
    """
    return n * 3
