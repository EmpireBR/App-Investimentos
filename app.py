from utilidades import apresentar_programa, verde, vermelho, azul, amarelo, separar_por_linha
import json
from pathlib import Path
from playsound import playsound


# Salvar as alterações feitas no arquivo JSON
def salvar_alteracoes(investimentos):
    investimento_json = json.dumps(investimentos)
    Path('investimentos.json').write_text(investimento_json)

def criar_investimentos_inciais():
    lista_de_investimentos = [
        {
            "id": 1,
            "nome": "celular",
            "valor": 1500
        },
        {
            "id": 2,
            "nome": "geladeira",
            "valor": 1300
        },
        {
            "id": 3,
            "nome": "notebook",
            "valor": 3500
        },
        {
            "id": 4,
            "nome": "IPhone",
            "valor": 7000
        },
        {
            "id": 5,
            "nome": "Placa de Video",
            "valor": 1200
        },
        {
            "id": 6,
            "nome": "PS5",
            "valor": 4999
        }

    ]
    salvar_alteracoes(lista_de_investimentos)


def ler_investimentos_existentes():
    investimentos_json = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentos_json)
    return investimentos


def exibir_investimento_total():
    # Armazena os investimentos em uma variável
    investimentos = ler_investimentos_existentes()
    total = 0
    for investimento in investimentos:
        # Calcula o total de todos os investimentos
        total = investimento['valor'] + total
    verde('O total investido até o momento foi de: ' + 'R$' + str(total))


def listar_investimentos(exibir_todos=False):
    from tabulate import tabulate
    investimentos = ler_investimentos_existentes()
    lista_de_investimentos = []
    # Mostrar os 5 primeiros investimentos
    if exibir_todos == False:
        for investimento in investimentos[0:5]:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']])
        print(tabulate(lista_de_investimentos,
                       headers=['id', 'nome', 'valor']))
    # Mostrar todos os investimentos
    else:
        for investimento in investimentos:
            lista_de_investimentos.append(
                [investimento['id'], investimento['nome'], investimento['valor']])
        print(tabulate(lista_de_investimentos,
                       headers=['id', 'nome', 'valor']))


def apresentar_menu():
    separar_por_linha()
    verde('1 - Listar todos investimentos')
    amarelo('2 - Editar investimento existente')
    vermelho('3 - Excluir um investimento')
    verde('4 - Criar investimento')
    azul('5 - Sair')
    opcao = input('Digite uma opção: ')
    separar_por_linha()
    return opcao


def editar_investimento_existente(investimento_id):
    investimentos = ler_investimentos_existentes()
    nome = input('Digite o novo nome: ')
    valor = input('Digite o novo valor: ')
    for investimento in investimentos:
        if investimento['id'] == int(investimento_id):
            if nome != '':
                investimento.update({'nome': nome})
            if valor != '':
                investimento.update({'valor': int(valor)})
            salvar_alteracoes(investimentos)
            verde('O investimento foi alterado com sucesso!')


def excluir_investimento(investimento_id):
    investimentos = ler_investimentos_existentes()
    for indice, item in enumerate(investimentos):
        if item['id'] == int(investimento_id):
            item_a_excluir = item['nome']
            vermelho(f'O investimento {item_a_excluir} foi excluído com sucesso!')
            del investimentos[indice]
            salvar_alteracoes(investimentos)


def obter_ultimo_id(investimentos):
    # descobrir qual foi o útlimo investimento criado
    # 1 - ler o útlimo investimento
    ultimo_investimento = investimentos[-1:]
    # 2 - Extrair a propriedade id
    ultimo_id = ultimo_investimento[0]['id']
    # 3 - Adicionar 1 ao último id
    ultimo_id += 1
    return ultimo_id


def criar_novo_investimento(nome, valor):
    # saber quais são os investimentos existentes
    investimentos = ler_investimentos_existentes()
    ultimo_id = obter_ultimo_id(investimentos)

    novo_investimento = {'id': ultimo_id, 'nome': nome, 'valor': valor}
    investimentos.append(novo_investimento)
    salvar_alteracoes(investimentos)
    investimento_a_ser_criado = novo_investimento['nome']
    verde(f'O investimento {investimento_a_ser_criado} acaba de ser criado!')


if __name__ == '__main__':
    playsound('1. Ghost Town.wav', block=False)
    apresentar_programa()
    exibir_investimento_total()
    listar_investimentos()
    # Listar todos, editar, excluir e criar
    while True:
        opcao = apresentar_menu()
        if opcao == '1':
            listar_investimentos(exibir_todos=True)
        if opcao == '2':
            investimento_id = input('Qual investimento deseja alterar: ')
            editar_investimento_existente(investimento_id)
        if opcao == '3':
            investimento_id = input('Digite o id do investimento a excluir: ')
            excluir_investimento(investimento_id)
        if opcao == '4':
            nome = input('Nome do investimento: ')
            valor = int(input('Valor do investimento: '))
            criar_novo_investimento(nome, valor)
        if opcao == '5':
            verde('OBRIGADO! VOLTE SEMPRE')
            break

# criar_investimentos_iniciais()


