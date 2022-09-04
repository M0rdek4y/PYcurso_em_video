from random import randint
from time import sleep

# banco de dados

line = '—=—' * 20
t = 'Vou pensar em um npumero entre 0 e 5. Tente adivinhar...'
p = 'PROCESSANDO...'
print("""{}
{}
{}""".format(line, t, line))
esc = int(input('Em que número eu pensei?\n'))
sor = randint(0, 5)
if esc == sor:
    print(p)
    sleep(2)
    print('\nPARABÉNS! Você conseguiu me vencer!')
else:
    print(p)
    sleep(2)
    print('\nGANHEI! Eu pensei no número {} e não no {}!'.format(esc, sor))
