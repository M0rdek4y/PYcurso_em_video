from datetime import date

ya = date.today().year
identidade = dict()
identidade['nome'] = str(input('nome: '))
identidade['idade'] = int(input('ano de nascimento: '))
identidade['idade'] = ya - identidade['idade']
identidade['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if identidade['ctps'] != 0:
    identidade['contratação'] = int(input('Ano de contratação: '))
    identidade['salario'] = float(input('Salário: R$'))
    identidade['aposentar'] = identidade['idade'] + (35 - (ya - identidade['contratação']))
for k, v in identidade.items():
    print(f'{k} tem o valor {v}')
