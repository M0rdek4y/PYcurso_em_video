#\033[0;33;44m
"""
style:
0 None
1 Bold
4 Underline
7 Negative
text:
30 a 37
back:
40 a 47
"""
nome = str(input('Diga seu nome: ')).strip()
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[34m', nome,  '\033[m'))
