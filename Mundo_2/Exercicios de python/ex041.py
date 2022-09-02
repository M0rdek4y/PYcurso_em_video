from datetime import date

aa = date.today().year

an = int(input('Em que ano o atleta nasceu: '))
ida = aa - an
if ida <= 9:
    print('O atleta tem {} anos e sua catêgoria é Mirim'.format(ida))
elif 10 <= ida <= 14:
    print('O atleta tem {} anos e sua catêgoria é Infantil'.format(ida))
elif 15 <= ida <= 19:
    print('O atleta tem {} anos e sua catêgoria é Junior'.format(ida))
elif ida == 20:
    print('O atleta tem {} anos e sua catêgoria é Sênior'.format(ida))
else:
    print('O atleta tem {} anos e sua catêgoria é MASTER'.format(ida))
