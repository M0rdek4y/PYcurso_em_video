n = int(input('Diga o numero que deseja converter: '))
esc = int(input('Deseja converter o némero {} para BINÁRIO(1), OCTAL(2) ou HEXADECIMAL(3):'.format(n)))
if esc == 1:
    print('O número {} convertido em BINÁRIO é: {}'.format(n, bin(n)[2:]))
elif esc == 2:
    print('O número {} convertido em OCTAL é: {}'.format(n, bin(n)[2:]))
elif esc == 3:
    print('O número {} convertido em OCTAL é: {}'.format(n, bin(n)[2:]))
else:
    print('Opção invalida! Tente Novamente!')
