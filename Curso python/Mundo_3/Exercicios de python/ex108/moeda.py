def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, a=0):
    p = (n/100) * a
    n = p + n
    return n


def diminuir(n=0, a=0):
    p = (n/100) * a
    n = n - p
    return f'{n:.2f}'


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
