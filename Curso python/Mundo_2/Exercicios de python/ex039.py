from datetime import date

# objects database
da = date.today().year

yn = int(input('Diga o ano que nasceu: '))
ida = da - yn
if ida == 18:
    print('Você tem {} anos está na hora de se alistar'.format(ida))
elif ida > 18:
    print('Você tem {} anos, passou {} anos do prazo do seu alistamento'.format(ida, ida-18))
else:
    print('Você tem {} anos e faltam {} anos para o seu alistamento.'.format(ida, 18-ida))
