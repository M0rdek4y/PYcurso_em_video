from stylefont import aze, ved, azc

num = int(input('{}Digite um valor: '.format(aze)))
b = ('–'*16)
print('{}{}'.format(ved, b))
for c in range(1, 10+1):
    print('{3}{0}{4} x {1} = {5}{2}'.format(num, c, num*c, azc, aze, ved))
print('{}{}'.format(ved, b))
