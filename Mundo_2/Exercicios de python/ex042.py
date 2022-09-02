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
    if a == b == c:
        print('O triângulo é equilátero!')
    elif a == b or a == c or c == b:
        print('O triângulo é isósceles!')
    else:
        print('O triângulo é escaleno!')
else:
    print('As retas não formam um triangulo!')
