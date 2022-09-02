# biblioteca de importações
from random import choice
from stylefont import rox, ama, res, aze, vem, ved, azc, fazc, fpre
from time import sleep
# listas e objetos
lst = ['pedra', 'papel', 'tesoura']
pc = choice(lst)
line = '—=—'*5
# titlo do jogo
print("""{5}{1}{3}{2}
{5}{0}####JOKENPÔ####{2}
{5}{1}{3}{2}""".format(rox, ama, res, line, fazc, fpre))
# inicio de game
sleep(0.5)
print('{0}Vamos jogar!!!{1}'.format(ama, res))
sleep(0.5)
player = str(input('{}ESCOLHA:{}\nPedra(1)\nPapel(2)\nTesoura(3)\n{}'.format(aze, azc, res))).strip().lower()
if player.lower() == '1' or player.lower() == 'pedra':
    player = 'pedra'.lower()
    if pc == lst[0]:
        print('{5}Você jogou {3}{1}{5}! Eu joguei {3}{0}{5}! {3}Nós empatamos!{4}'.format(pc, player, aze, ama, res, azc))
    elif pc == lst[1]:
        print('{3}Você jogou {1}! {5}Eu joguei {0}! {2}E {5}{0} {2}enrola {3}{1}{2}! {3}Você perdeu!{4}'.format(pc, player, aze, vem, res, ved))
    else:
        print('{3}Você jogou {1}! {5}Eu joguei {0}! {2}E {3}{1} {2}quebra {5}{0}{2}! {3}Você ganhou!{4}'.format(pc, player, aze, ved, res, vem))
elif player.lower() == '2' or player.lower() == 'papel':
    player = 'papel'.lower()
    if pc == lst[1]:
        print('{5}Você jogou {3}{1}{5}! Eu joguei {3}{0}{5}! {3}nós empatamos!{4}'.format(pc, player, aze, ama, res, azc))
    elif pc == lst[2]:
        print('{3}Você jogou {1}! {5}Eu joguei {0}! {2}E {5}{0} {2}corta {3}{1}{2}! {3}Você perdeu!{4}'.format(pc, player, aze, vem, res, ved))
    else:
        print('{3}Você jogou {1}! {5}Eu joguei {0}! {2}E {3}{1} {2}enrola {5}{0}{2}! {3}Você ganhou!{4}'.format(pc, player, aze, ved, res, vem))
elif player.lower() == '3' or player.lower() == 'tesoura':
    player = 'tesoura'.lower()
    if pc == lst[2]:
        print('{5}Você jogou {3}{1}{5}! Eu joguei {3}{0}{5}! {3}Nós empatamos!{4}'.format(pc, player, aze, ama, res, azc))
    elif pc == lst[0]:
        print('{3}Você jogou {1}! {5}Eu joguei {0}! {2}E {5}{0} {2}amassa {3}{1}{2}! {3}Você perdeu!{4}'.format(pc, player, aze, vem, res, ved))
    else:
        print('{3}Você jogou {1}! {5}Eu joguei {0}! {2}E {3}{1} {2}corta {5}{0}{2}! {3}Você ganhou!{4}'.format(pc, player, aze, ved, res, vem))
else:
    player = '0'
    print('{3}O caractere {0}{1}{3} é {0}invalido!!!{2}'.format(vem, player, res, aze))
