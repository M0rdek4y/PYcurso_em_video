"""pessoas = {'nome': 'Alan', 'idade': 20, 'sexo': 'M'}
del pessoas['sexo']
pessoas['nome'] = 'Jão'
pessoas['peso'] = '70'
for k, v in pessoas.items():
    print(f'{k} = {v}')
"""
"""brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k}: {v}')
    for v in e.values():
        print(v)
