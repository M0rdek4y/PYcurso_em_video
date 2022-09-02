from stylefont import res, aze, ved, azc, vem, ama
vlcs = float(input('{}Qual valor da casa que deseja comprar: {}R$'.format(aze, ved)))
sal = float(input('{}Por favor agora diga o valor do seu salário: {}R$'.format(aze, ved)))
tem = int(input('{}Diga em quantos anos deseja pagar o emprestimo: {}'.format(aze, res)))
pres = vlcs / (tem * 12)
poc = (sal*30)/100
if pres > sal+poc:
    print('{0}Sinto muito!{1} Mas o valor da prestação é de {4:.2f} excedeu {0}30%{1} do salário e seu emprestimo foi {2}NEGADO{1}!{3}'.format(ama, aze, vem, res, pres))
else:
    print('{0}Parabéns!{1} Seu empréstimo de {0}{4}{1} terá {0}{5}{1} prestações de {0}R${6}{1}, está dentro das normas e foi {2}APROVADO{1}!{3}'.format(azc, aze, ved, res, vlcs, tem, pres))
