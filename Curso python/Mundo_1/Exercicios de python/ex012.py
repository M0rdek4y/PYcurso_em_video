v = float(input('Qual é o preço do produto? R$'))
d = 5/100
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.1f}'.format(v,v-(d*v)))
