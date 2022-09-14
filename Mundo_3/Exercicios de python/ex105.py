def notas(*n, sit=False):
    """
    ->Função para analizar notas de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param sit: Valor opcional. Indica se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total: '] = len(n)
    r['maior: '] = max(n)
    r['menor: '] = min(n)
    r['média: '] = sum(n)/len(n)
    if sit:
        if r['média: '] >= 7:
            r['situação'] = 'BOA'
        elif r['média: '] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
