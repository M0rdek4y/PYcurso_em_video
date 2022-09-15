from stylefont import aze, ved, azc
inf = input('Digite algo: '.format(aze))
print('{9}O tipo primitivo desse valor é {8}{0}\n'
      '{9}Só tem espaços? {8}{1}\n'
      '{9}É um número? {8}{2}\n'
      '{9}É alfabético? {8}{3}\n'
      '{9}É alfanumérico? {8}{4}\n'
      '{9}Está em maiúsculas? {8}{5}\n'
      '{9}Está em minúsculas? {8}{6}\n'
      '{9}Está capitalizada? {8}{7}'.format(type(inf), inf.isspace(), inf.isnumeric(), inf.isalpha(), inf.isalnum(), inf.isupper(), inf.islower(), inf.istitle(), ved, azc))
