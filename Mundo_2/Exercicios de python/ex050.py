s = 0
for c in range(0+1, 7):
    n = int(input('Digite o {}º valor:'.format(c)))
    par = n % 2
    if par == 0:
        s += n
print(s)
