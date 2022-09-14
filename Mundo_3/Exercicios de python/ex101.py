def voto(ano):
    from datetime import date
    ano = date.today().year - ano
    if 18 <= ano < 65:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO.'
    elif ano < 18:
        return f'Com {ano} anos: NÃO VOTA.'
    elif ano > 65:
        return f'Com {ano} anos: VOTO OPCIONAL.'


# Programa principal
print('-'*40)
idade = int(input('Em que ano você nasceu? '))
voto(idade)
