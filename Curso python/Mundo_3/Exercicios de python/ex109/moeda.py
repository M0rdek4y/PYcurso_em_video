def metade(n=0, formato=False):
    """
    -> Transforma o valor na sua metade.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor em sua metade formatado ou não.
    """
    res = n / 2
    return res if formato is False else moeda(n)


def dobro(n=0, formato=False):
    """
    -> Transforma o valor no seu dobro.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor no seu dobro formatado ou não.
    """
    res = n / 2
    return res if formato is False else moeda(n)


def aumentar(n=0, a=0, formato=False):
    """
    -> Transforma o valor com aumento de uma porcentagem.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor mais o valor da porcentagem.
    """
    p = (n/100) * a
    res = p + n
    return res if formato is False else moeda(n)


def diminuir(n=0, a=0, formato=False):
    """
    -> Transforma o valor com diminuição de uma porcentagem.
    :param n: Recebe o valor.
    :param formato: Formata o valor em moeda BR [True/False].
    :return: Retorna o valor menos o valor da porcentagem.
    """
    p = (n/100) * a
    res = n - p
    return f'{res:.2f}' if formato is False else moeda(n)


def moeda(n=0, moeda='R$'):
    """
    -> Formata o valor em padrão da moeda BR (R$) como padrão
    :param n: Recebe o valor a ser formatado
    :param moeda: Recebe o tipo de moeda a ser formatado
    :return: Retorna o valor digitado no padrão BR
    """
    return f'{moeda}{n:.2f}'.replace('.', ',')
