from datetime import date
yn = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    ida = yn - ano
    if ida >= 21:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas, {1} são menor de idade e {0} são maior de idade.'.format(maior, menor))
