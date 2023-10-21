import json
import os


def adicionar(pessoas):
    nome = input('Digite o nome da pessoa que deseja adicionar: ')
    data = input('Digite a sua data de aniversario Ex.(02.10); ')
    pessoas[nome.title()] = data

def listar(pessoas):
    for chave, data in pessoas.items():
        print(f'{chave} - {data}')

def pesquisar_nome(pessoas):
    nome_pesquisa = input('Digite o nome: ')
    if pessoas.get(nome_pesquisa.title()) is None:
        print('Essa pessoas não está na lista')
    else:
        print(f'{nome_pesquisa.title()} faz aniversario dia {pessoas[nome_pesquisa.title()]}')

def ler(pessoas, caminho_arquivo):
    dados = {}
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(pessoas, caminho_arquivo)
    return dados

def salvar(pessoas, caminho_arquivo):
    dados = pessoas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO =  './listaraniversario.json'
aniversa = ler({}, CAMINHO_ARQUIVO)

os.system('clear')
while(True):
    print('\n---- Lista de Aniversário ----')
    print('1 - Adicionar Aniversariante')
    print('2 - Pesquisar pelo nome')
    print('3 - Listar Todos os aniversariantes')
    option = int(input('Digite uma opção: '))

    if option == 1:
        adicionar(aniversa)
    elif option == 3:
        print()
        os.system('clear')
        listar(aniversa)
    elif option == 2:
        os.system('clear')
        pesquisar_nome(aniversa)   
    salvar(aniversa, CAMINHO_ARQUIVO)
