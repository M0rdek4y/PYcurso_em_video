ln = "—=—"*8
print("""
{}
Analisador de triangulos
{}
""".format(ln, ln))
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if (b + c > a) and (a + c > b) and (a + b > c):
    print('As retas formam um triangulo!')
else:
    print('As retas não formam um triangulo!')
