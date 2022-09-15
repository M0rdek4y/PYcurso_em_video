nome = str(input('Qual é seu nome: ')).strip()
nt = nome
if nt.upper() == 'GUSTAVO':
    print('Mas que belo nome!\n'.format(nome))
elif nt.upper() == 'PEDRO' or nt.upper() =='PAULO' or nt.upper() == 'MARIA':
    print('Seu nome é bem popular no Brasil.')
elif nt.upper() in 'ALAN':
    print('Maneiro!!')
print('Tenha um bom dia {}!'.format(nome))
