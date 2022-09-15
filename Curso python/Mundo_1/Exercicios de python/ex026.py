text = str(input('Escreva uma frase: ')).strip().upper()
print("""
A letra "A" aparece: {} Vezes
A posição da primeira letra "A" é: {}
A ultima vez que a letra "A" aparece é: {}
""".format(text.count('A'), text.find('A') + 1, text.rfind('A') + 1))
