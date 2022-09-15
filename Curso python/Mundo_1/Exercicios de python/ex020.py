# resolução 1

import random
al1 = str(input('Diga o nome do aluno: '))
al2 = str(input('Diga o nome do aluno: '))
al3 = str(input('Diga o nome do aluno: '))
al4 = str(input('Diga o nome do aluno: '))
sala = [al1, al2, al3, al4]
random.shuffle(sala)
print('A ordem das apresentações será: ')
print(sala)

# resolução 2

from random import shuffle
al1 = str(input('Diga o nome do aluno: '))
al2 = str(input('Diga o nome do aluno: '))
al3 = str(input('Diga o nome do aluno: '))
al4 = str(input('Diga o nome do aluno: '))
sala = [al1, al2, al3, al4]
shuffle(sala)
print('A ordem das apresentações será: ')
print(sala)
