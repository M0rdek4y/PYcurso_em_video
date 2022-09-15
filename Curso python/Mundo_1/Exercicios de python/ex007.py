from stylefont import aze, ved, azc, res

n1 = float(input('{}Digite a primeira nota: '.format(aze)))
n2 = float(input('Agora digite a segunda nota: {}'.format(res)))
print('{3}A média entre {5}{0:.1f}{3} e {5}{1:.1f}{3} é igual a {4}{2:.1f}{3}!{6}'.format(n1, n2, (n1+n2)/2, aze, ved, azc, res))
