from pitii.lib.interface import *
from pitii.lib.arquivo import *
from time import sleep

arq= 'produtos.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Produto', 'Listar Produto', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de cadastrar um novo Produto.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        quant = leiaInt('Quantidade: ')
        cadastrar(arq, nome, quant)
    elif resposta == 2:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
