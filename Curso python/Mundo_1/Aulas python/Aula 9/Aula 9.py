from random import shuffle

frase = 'Curso em Video Python'
f2 = '   Aprenda Python '
print(len(frase), frase[0::2], end='<< >>')
print(frase.count('o'), end='<< >>')
print(frase.find('deo'), end='<< >>')
print(frase.find('Android'), end='<< >>')
print('Curso' in frase, end='<< >>')
print(frase.replace('Python', 'Android'), end='<< >>')
print(frase.upper(), end='<< >>')
print(frase.lower(), end='<< >>')
print(frase.capitalize(), end='<< >>')
print(frase.title(), end='<< >>')
print(f2.strip(), end='<< >>')
print(f2.rstrip(), '\n', end='<< >>')
print(f2.lstrip(), end='<< >>')
print(frase.split(), end='<< >>')
fr = frase.split()
print('-'.join(fr))
