# resolução 1

import random
n1 = str(input('digite o nome do aluno: '))
n2 = str(input('digite o nome do aluno: '))
n3 = str(input('digite o nome do aluno: '))
n4 = str(input('digite o nome do aluno: '))
esc = [n1, n2, n3, n4]
sorteio = random.choice(esc)
print('Os Alunos são {}, {}, {} e {}.'.format(n1, n2, n3, n4))
print('O escolhido para limpar o quadro foi {}.'.format(sorteio))

# resolução 2

from random import choice
n1 = str(input('digite o nome do aluno: '))
n2 = str(input('digite o nome do aluno: '))
n3 = str(input('digite o nome do aluno: '))
n4 = str(input('digite o nome do aluno: '))
esc = [n1, n2, n3, n4]
sorteio = choice(esc)
print('O escolhido para limpar o quadro foi {}.'.format(sorteio))
