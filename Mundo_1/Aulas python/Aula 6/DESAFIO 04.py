inf = input(
    'Digite algo: ')
print('O tipo primitivo desse valor é {}\n'
      'Só tem espaços? {}\n'
      'É um número? {}\n'
      'É alfabético? {}\n'
      'É alfanumérico? {}\n'
      'Está em maiúsculas? {}\n'
      'Está em minúsculas? {}\n'
      'Está capitalizada? {}'.format(type(inf), inf.isspace(), inf.isnumeric(), inf.isalpha(), inf.isalnum(), inf.isupper(), inf.islower(), inf.istitle()))
