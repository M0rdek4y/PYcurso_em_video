from time import sleep


def line():
    print('=-'*15)


def title(txt):
    lin = (len(txt) // 2) + 4
    print('=-' * lin, f'\n{txt}')
    print('=-' * lin)


def contador():
    line()
    c = 1
    print('Contagem de 1 até 10 de 1 em 1')
    for v in range(0, 10):
        print(c, end=' ')
        c += 1
        sleep(0.3)
    print('FIM!')
    line()
    c = 10
    print('Contagem de 10 até 0 de 2 em 2')
    for v in range(10, -1, -2):
        print(c, end=' ')
        c -= 2
        sleep(0.3)
    print('FIM!')
    line()
    print('Agora é sua vez de personalizar a contagem!')
    a = int(input('Início: '))
    b = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo > 0:
        if b > a:
            for a in range(a, b, passo):
                print(a, end=' ')
                sleep(0.3)
        elif a > b:
            passoalt = passo - passo * 2
            for a in range(a, b-passo, passoalt):
                print(a, end=' ')
                sleep(0.3)
    elif passo == 0:
        passo = 1
        if b > a:
            for a in range(a, b, passo):
                print(a, end=' ')
                sleep(0.3)
        elif a > b:
            passoalt = passo - passo * 2
            for a in range(a, b-passo, passoalt):
                print(a, end=' ')
                sleep(0.3)
    else:
        if a > b:
            for a in range(a, b+passo, passo):
                print(a, end=' ')
                sleep(0.3)
    print('FIM!')


# Programa principal
title(' CONTADOR ')
contador()
