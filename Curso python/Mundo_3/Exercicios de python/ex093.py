nome = dict()
part = list()
nome['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {nome["nome"]} jogou? '))
for p in range(tot):
    part.append(int(input(f'Quantos gols na {p+1}º partida? ')))
nome['gols'] = part[:]
nome['total'] = sum(part)
print('-=' * 30)
print(nome)
print('-=' * 30)
for k, v in nome.items():
    print(f'O campo {k} tem o valor {v}. ')
print('-=' * 30)
print(f'O jogador {nome["nome"]} jogou {len(nome["gols"])} partidas.')
for i, v in enumerate(nome["gols"]):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {nome["gols"]}.')
