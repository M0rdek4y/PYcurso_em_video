def title(txt):
    lin = len(txt) // 2
    print('=-' * lin, f'\n{txt}')
    print('=-' * lin)


def escreva(txt):
    tam = len(txt) + 4
    print('~'*tam, f'\n  {txt}')
    print('~'*tam)


# Programa principal
title('  ESCREVA UM TEXTO  ')
escreva('  Alan Marques  ')
escreva('  MUNDO_3 CURSO EM VIDEO  ')
escreva('  FUNÇÕES  ')
