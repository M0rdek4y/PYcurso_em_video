from datetime import date

yr = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if yr == 0:
    yr = date.today().year
if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(yr))
else:
    print('O ano {} não é BISSEXTO!'.format(yr))
