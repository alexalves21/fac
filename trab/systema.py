from trab.lib.interface import *
from trab.lib.arquivo import *
from time import sleep

arq = 'arquivos.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Cadastrar Produto', 'Lista de Produtos', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de cadastrar um produto.
        cabeçalho('Cadastrar Produto')
        nome = str(input('Nome: '))
        quantidade = leiaInt('Quantidade: ')
        cadastrar(arq, nome, quantidade)
    elif resposta == 2:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)