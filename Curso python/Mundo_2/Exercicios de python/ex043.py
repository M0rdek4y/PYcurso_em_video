altu = float(input('Digite a altura(M) da pessoa: '))
peso = float(input('Digite o peso(Kg) da pessoa: '))
imc = peso/(altu**2)
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso!'.format(imc))
elif 24.9 >= imc >= 18.5:
    print('Seu IMC é {:.1f}, você está no peso ideal!'.format(imc))
elif 29.9 >= imc >= 25:
    print('Seu IMC é {:.1f}, você está com sobrepeso!'.format(imc))
elif 39.9 >= imc >= 30:
    print('Seu IMC é {:.1f}, você está com obesidade!'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com obesidade mórbida!'.format(imc))
