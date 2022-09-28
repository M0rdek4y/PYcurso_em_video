def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[0;31mERRO: O valor não é inteiro...\33[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mEntrada de dados interrompida pelo usuário.\33[m')
            return 0
        else:
            valor = n
            return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\33[33m{c}\33[m - \33[34m{i}\33[m')
        c += 1
    print(linha())
    opc = leiaint('\33[32mSua Opção:\33[m ')
    return opc
