while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite um número: '))
        r = a / b
    except (ValueError, TypeError):
        print('ERRO! Os dados digitados foram inválidos ...')
    except ZeroDivisionError:
        print(f'ERRO! Impossivel dividir {a} por {b}')
    except KeyboardInterrupt:
        print('ERRO! O usuário não informou os dados')
    except Exception as erro:
        print(f'ERRO! Causa do erro: {erro.__cause__}...')
    else:
        print(f'O resultado é {r:.2f}')
        break
    finally:
        print('Volte sempre! Muito obrigado!')
