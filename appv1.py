import os 
import re

transacoes = [{'descricao':'Salário','valor':1500.00, 'tipo':'Entrada','data':'05/05/2025'}]

def menu():
    print('𝙱𝚊𝚗𝚌𝚘 - 𝙲𝚘𝚗𝚝𝚛𝚘𝚕𝚎 𝙵𝚒𝚗𝚊𝚗𝚌𝚎𝚒𝚛𝚘\n')
    print('1- Adicionar Transação')
    print('2- Listar Transações')
    print('3- Atualizar Transação')
    print('4- Deletar Transação')
    print('5- Ver Saldo')
    print('6- Sair\n')

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 1:
            adicionar_tr()
        elif opcao == 2:
            listar_tr()
        elif opcao == 3:
            atualizar_tr()
        elif opcao == 4:
            deletar_tr()
        elif opcao == 5:
            saldo()
        elif opcao == 6:
            fechar_prog()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def adicionar_tr():
    os.system('cls')
    print('𝙰𝚍𝚒𝚌𝚒𝚘𝚗𝚊𝚛 𝚃𝚛𝚊𝚗𝚜𝚊𝚌̧𝚊̃𝚘\n')
    descricao = input('Descrição: ')
    valor = pedir_valor()
    tipo = validar_tipo()
    data = validar_data()
    dados_transacoes = {'descricao':descricao, 'valor':valor, 'tipo':tipo, 'data':data}
    transacoes.append(dados_transacoes)
    voltar_menu()

def listar_tr():
    os.system('cls')
    print('𝙻𝚒𝚜𝚝𝚊𝚛 𝚃𝚛𝚊𝚗𝚜𝚊𝚌̧𝚘̃𝚎𝚜\n')
    mostrar_tr()
    voltar_menu()

def atualizar_tr():
    os.system('cls')
    print('𝙰𝚝𝚞𝚊𝚕𝚒𝚣𝚊𝚛 𝚃𝚛𝚊𝚗𝚜𝚊𝚌̧𝚊̃𝚘\n')
    mostrar_tr()
    indice = validar_id()
    transacao = transacoes[indice - 1]
    print('Digite os Novos Valores')
    nova_descricao = input('Descrição: ')
    novo_valor = pedir_valor()
    novo_tipo = validar_tipo()
    nova_data = validar_data()
    transacao['descricao'] = nova_descricao
    transacao['valor'] = novo_valor
    transacao['tipo'] = novo_tipo
    transacao['data'] = nova_data
    print('\nTransação Atualizada com Sucesso.')
    voltar_menu()

def deletar_tr():
    os.system('cls')
    print('𝙳𝚎𝚕𝚎𝚝𝚊𝚛 𝚃𝚛𝚊𝚗𝚜𝚊𝚌̧𝚊̃𝚘\n')
    mostrar_tr()
    indice = validar_id()
    transacao = transacoes[indice -1]
    print('Deseja Deletar Esta Transação?\n')
    print(f"Descrição: {transacao['descricao']}")
    print(f"Valor: R${transacao['valor']}")
    print(f"Tipo: {transacao['tipo']}")
    print(f"Data: {transacao['data']}")
    confirmacao = input('\n[S/N]: ').upper()
    if confirmacao == 'S':
        transacoes.pop(indice - 1)
        print('\nTransação deletada com sucesso!')
    else:
        print('\nOperação cancelada.')
    voltar_menu()

def saldo():
    os.system('cls')
    print('𝚂𝚊𝚕𝚍𝚘\n')
    print(f"{'𝙳𝚊𝚝𝚊:'.ljust(15)} | {'𝚅𝚊𝚕𝚘𝚛:'.ljust(15)} ")
    contador = 0
    for transacao in transacoes:
        data = transacao['data']
        valor = transacao['valor']
        print(f'{data.ljust(15)} | R${valor:.2f}')
        if transacao['tipo'] == 'Entrada':
            contador += valor
        else:
            contador -= valor
    print(f'\nSeu saldo atual é: R${contador:.2f}')
    voltar_menu()

def validar_id():
    while True:
        try:
            indice = int(input('\nDigite o ID da Transação: '))
            if indice <1 or indice > len(transacoes):
                print('ID Inválido!')
            else:
                return indice
        except ValueError:
            print('Digite um ID Válido.')

def mostrar_tr():
    print(f"{'ID'.ljust(5)} | {'𝙳𝚎𝚜𝚌𝚛𝚒𝚌̧𝚊̃𝚘:'.ljust(15)} | {'𝚅𝚊𝚕𝚘𝚛:'.ljust(15)} | {'Tipo:'.ljust(15)} | {'𝙳𝚊𝚝𝚊:'.ljust(15)}")
    for indice,transacao in enumerate(transacoes, start=1):
        descricao = transacao['descricao']
        valor = transacao['valor']
        tipo = transacao['tipo']
        data = transacao['data']
        print(f'{str(indice).ljust(5)} | {descricao.ljust(13)} | R${str(valor).ljust(13)} | {tipo.ljust(15)} | {data.ljust(15)}')

def pedir_valor():
    while True:
        try:
            valor = float(input('Valor: '))
            return valor
        except ValueError:
            print('Digite um Valor válido.')

def validar_tipo():
    while True:
        tipo = input('Tipo [Entrada/Saída]: ').capitalize()
        if tipo in ['Entrada','Saída']:
            return tipo
        print('Tipo Inválido!')

def fechar_prog():
    print('Encerrando Programa!')
    exit()

def opcao_invalida():
    print('\nOpção Inválida!')
    voltar_menu()

def validar_data():
    while True:
        data = input('Data [DD/MM/AAAA]: ')
        padrao = r'^\d{2}/\d{2}/\d{4}$'
        if re.match(padrao,data):
            return data
        print('Data Inválida!')

def voltar_menu():
    input('\nDigite uma tecla para voltar ao Menu: ')
    
def main():
    while True:     
     os.system('cls')
     menu()
     escolher_opcao()

if __name__ == '__main__':
    main()
