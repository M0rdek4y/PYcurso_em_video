num = int(input('Digite um valor: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""
unidade: {}
dezena: {}
centena: {}
milhar:{}
""".format(u, d, c, m))
