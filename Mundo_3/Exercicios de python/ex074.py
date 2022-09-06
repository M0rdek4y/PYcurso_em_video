from random import randint

lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {lista}')
print(f'O maior valor foi {max(lista)}\n'
      f'O menor valor foi {min(lista)}')
