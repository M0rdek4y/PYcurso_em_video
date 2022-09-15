d = float(input('Diga a distancia da sua viagem: '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(d))
if d <= 200:
    print('O valor da sua passagem é de R${:.2f}'.format(d*0.50))
else:
    print('O valor de passagem será de R${:.2f}'.format(d*0.45))
