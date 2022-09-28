from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastrados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Mostrar Cadastrados', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        # opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\33[31mERRO: Digite uma opção válida!\33[m')
    sleep(2)
