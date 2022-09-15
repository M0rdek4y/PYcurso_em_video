import stylefont
from time import sleep

c = (stylefont.res,  # 0 - sem cores
     stylefont.fvem,  # 1 - vermelho
     stylefont.fved,  # 2 - verde
     stylefont.fama,  # 3 - amarelo
     stylefont.faze,  # 4 - azul
     stylefont.frox,  # 5 - roxo
     stylefont.sinv  # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)

    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDAR pyhelp', 2)
    comando = str(input(f'{stylefont.fama} {stylefont.pre}Função ou Biblioteca >')).strip()
    print(stylefont.res)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
