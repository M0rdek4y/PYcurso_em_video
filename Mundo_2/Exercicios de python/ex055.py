maior = 0
menor = 0
for p in range(0+1, 5):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg e o menor de {}Kg'.format(maior, menor))
