def leiaint():
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\33[0;31mERRO: O valor não é inteiro...\33[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mEntrada de dados interrompida pelo usuário.\33[m')
            return 0
        else:
            valor = a
            return valor


def leiafloat():
    while True:
        try:
            b = str(input('Digite um número real: ')).replace(',', '.').strip()
            b = float(b)
        except (ValueError, TypeError):
            print('\33[0;31mERRO! O valor não é real...\33[m')
        except KeyboardInterrupt:
            print(f'\n\33[31mEntrada de dados interrompida pelo usuário.\33[m')
            return 0
        else:
            valor = b
            return valor


# Programa principal
print(f'O valor inteiro digitado foi {leiaint()} e o real foi {leiafloat()}')
