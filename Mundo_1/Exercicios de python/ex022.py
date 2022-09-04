'''name = str(input('Digite seu nome completo: ')).strip()
nlist = name.split()
njoin = (''.join(nlist))
fn = nlist[0]

print("""
O seu nome maiúsculo: {}
O seu nome minúsculo: {}
Seu nome sem os espaços tem: {} Letras
Seu primeiro nome tem: {} Letras
""".format(name.upper(), name.lower(), len(njoin), len(fn)))
'''

# correção

name = str(input('Digite seu nome comprelo: ')).strip()
print("""
O seu nome maiúsculo: {}
O seu nome minúsculo: {}
Seu nome sem os espaços tem: {} Letras
Seu primeiro nome tem: {} Letras
""".format(name.upper(), name.lower(), len(name) - name.count(' '), name.find(' ')))
