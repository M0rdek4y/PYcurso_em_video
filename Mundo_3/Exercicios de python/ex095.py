nome = dict()
part = list()
time = list()
while True:
    nome.clear()
    nome['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {nome["nome"]} jogou? '))
    part.clear()
    for p in range(tot):
        part.append(int(input(f'Quantos gols na {p+1}º partida? ')))
    nome['gols'] = part[:]
    nome['total'] = sum(part)
    time.append(nome.copy())
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    while True:
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in nome.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=' * 30)
print('<< VOLTE SEMPRE >>')
