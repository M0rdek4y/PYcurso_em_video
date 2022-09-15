w = float(input('Digite a largura: '))
h = float(input('Digite a  altura: '))
a = w*h
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².\nPara pintar essa parede . você precisará de {:.1f}l de tinta'.format(w, h, a, (w*h)/2))
