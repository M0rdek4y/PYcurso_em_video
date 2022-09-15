n1 = float(input('Digite a primeira nota:\n'))
n2 = float(input('Digite a segunda nota:\n'))
m = (n1+n2)/2
print('Sua nota foi {:.1f} !'.format(m))
if m > 7:
    print('Você passou!')
elif m == 7:
    print('Parabéns, você passou!')
else:
    print('Sinto muito! Estude mais da proxima vez!')
