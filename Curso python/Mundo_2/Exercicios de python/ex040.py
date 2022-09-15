from stylefont import rox, azc, aze, res, vem, ved, ama

# Objects DATABASE
sep = '—=—'*8

print(azc, sep)
print('  {}CALCULADOR DE MÉDIAS'.format(rox))
print(azc, sep)
n1 = float(input('{}Diga a primeira nota: '.format(aze)))
n2 = float(input('Diga a segunda nota: {}'.format(res)))
m = (n1+n2)/2
if 5 < m < 6.9:
    print('{}RECUPERAÇÃO'.format(ama))
elif m >= 7:
    print('{}APROVADO'.format(ved))
else:
    print('{}REPROVADO'.format(vem))
