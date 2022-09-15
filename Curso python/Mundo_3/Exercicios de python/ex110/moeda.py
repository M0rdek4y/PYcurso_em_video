def aumentar(n=0, taxa=0, formato=False):
    """
    -> Transforma o valor com aumento de uma porcentagem.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor mais o valor da porcentagem.
    """
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    """
    -> Transforma o valor com diminuição de uma porcentagem.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor menos o valor da porcentagem.
    """
    res = n - (n * taxa / 100)
    return f'{res:.2f}' if formato is False else moeda(res)


def dobro(n=0, formato=False):
    """
    -> Transforma o valor no seu dobro.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor no seu dobro formatado ou não.
    """
    res = n * 2
    return res if not formato else moeda(res)


def metade(n=0, formato=False):
    """
    -> Transforma o valor na sua metade.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor em sua metade formatado ou não.
    """
    res = n / 2
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    """
    -> Formata o valor em padrão da moeda BR (R$) como padrão
    :param n: Recebe o valor a ser formatado
    :param moeda: Recebe o tipo de moeda a ser formatado
    :return: Retorna o valor digitado no padrão BR
    """
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(n)}')
    print('-' * 30)
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(n, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(n, taxar, True)}')
    print('-' * 30)