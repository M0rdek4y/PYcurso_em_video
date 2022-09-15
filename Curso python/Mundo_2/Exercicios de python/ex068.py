import random

lista = random.randrange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = s = 0

print('=-'*12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*12)
while True:
    comp = random.choice(lista)
    n = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? {P/I} ')).strip().upper()[0]
    s = n + comp
    print('-'*24)
    if pi == 'P':
        if s % 2 == 0:
            print(f'Você jogou {n} e o computador {comp}. Total de {s} DEU PAR')
            print('-' * 24, '\nVocê VENCEU!\nVamos jogar novamente...')
            c += 1
        else:
            print(f'Você jogou {n} e o computador {comp}. Total de {s} DEU ÍMPAR')
            print('-' * 24, '\nVocê PERDEU!\n', '=-'*12, f'\nGAME OVER! Você venceu {c} vezes.')
            break

    elif pi == 'I':
        if s % 2 != 0:
            print(f'Você jogou {n} e o computador {comp}. Total de {s} DEU ÍMPAR')
            print('-' * 24, '\nVocê VENCEU!\nVamos jogar novamente...')
            c += 1
        else:
            print(f'Você jogou {n} e o computador {comp}. Total de {s} DEU PAR')
            print('-' * 24, '\nVocê PERDEU!\n', '=-'*12, f'\nGAME OVER! Você venceu {c} vezes.')
            break
    else:
        print('Digite um valor valido!')