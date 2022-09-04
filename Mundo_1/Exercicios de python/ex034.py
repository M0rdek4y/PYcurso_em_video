s = float(input('Qual é o salário do funcionário: R$'))
if s > 1250.00:
    p = s * 10/100
    print('O sálario de R${:.2f} , recebe aumento de 10% e fica: {:.2f}\nO aumento foi de: R${}'.format(s, s+p, p))
else:
    p = s * 15/100
    print('O sálario de R${:.2f} , recebe aumento de 15% e fica: {:.2f}\nO aumento foi de: R${}'.format(s, s+p, p))
