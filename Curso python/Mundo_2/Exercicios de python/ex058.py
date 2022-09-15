from random import randint
from time import sleep

# banco de dados

line = '—=—' * 20
t = 'Vou pensar em um número entre 0 e 5. Tente adivinhar...'
p = 'PROCESSANDO...'
print("""{}
{}
{}""".format(line, t, line))
esc = int(input('Em que número eu pensei?\n'))
sor = randint(0, 10)
c = 1
while esc != sor:
    print(p)
    sleep(1)
    esc = int(input('você errou! Tente novamente:'))
    c = c + 1
if c == 1:
    print(p)
    sleep(1)
    print('\nPARABÉNS! Você conseguiu me vencer com {} tentativa'.format(c))
else:
    print(p)
    sleep(1)
    print('\nPARABÉNS! Você conseguiu me vencer com {} tentativas'.format(c))
