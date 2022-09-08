maioridade = 0
menoridade = 0
mediaidade = 0
maisvelho = str
for c in range(0+1, 5):
    print('{}{}ª PESSOA {}'.format('-'*5, c, '-'*5))
    nome = str(input('Nome: '.format(c)))
    idade = int(input('Idade: '.format(c)))
    sexo = str(input('Sexo=[1]Masculino/[2]Feminino: '.format(c))).lower()
    if idade > maioridade and sexo == 'masculino' or idade > maioridade and sexo == 'm' or idade > maioridade and sexo == '1':
        maioridade = idade
        maisvelho = nome
    elif idade <= 20 and sexo == 'feminino' or idade <= 20 and sexo == 'f' or idade <= 20 and sexo == '2':
        menoridade += 1
    mediaidade += idade
print("""A idade média do temp é de: {} anos;
      O nome do homem mais velho tem {} anos e se chama {};
      Ao todo são {} mulheres com menos de 20 anos.""".format(mediaidade/4, maioridade, maisvelho, menoridade))
