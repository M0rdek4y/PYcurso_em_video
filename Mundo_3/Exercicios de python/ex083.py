cont = 0

expr = str(input('DIgite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')
#((a+b)*(a*c)-2