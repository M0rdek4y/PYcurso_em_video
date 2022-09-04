a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("""
O maior valor é: {}
O menor valor é: {}
""".format(maior, menor))