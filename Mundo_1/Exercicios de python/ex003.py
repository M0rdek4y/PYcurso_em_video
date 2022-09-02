from stylefont import aze, azc, rox

n1 = int(input('\033[34mDigite um valor: '))
n2 = int(input('Digite outro valor:\033[m '))
s = n1 + n2
print('\033[34m A soma entre {4}{0}{3} e {4}{1} {3}é igual a {5}{2}{3}!'.format(n1, n2, s, aze, rox, azc))
