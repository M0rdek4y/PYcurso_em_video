s = 0
cont = 0
for c in range(1, 500, 2):
    div = c % 3
    if div == 0:
        cont = cont + 1
        s += c
print(s, cont)
