frase = str(input('Digite a frase:\n')).strip().upper()
palav = frase.split()
junto = ''.join(palav)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('O inverso de "{}" é "{}"\nA frase digitada é um palíndromo!'.format(junto, inverso))
else:
    print('O inverso de "{}" é "{}"\nA frase digitada não é um palíndromo!'.format(junto, inverso))


