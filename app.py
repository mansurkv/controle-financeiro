import os 
import re
import sqlite3
from banco import conectar, criar_tabela

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
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO transacoes(descricao, valor, tipo, data)
        VALUES (?, ?, ?, ?)
    """, (descricao, valor, tipo, data))
    conexao.commit()
    conexao.close()
    print('\nTransação Adicionada com Sucesso.')
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
    print('\nDigite os Novos Valores\n')
    nova_descricao = input('Descrição: ')
    novo_valor = pedir_valor()
    novo_tipo = validar_tipo()
    nova_data = validar_data()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE transacoes
            SET descricao = ?, valor = ?, tipo = ?, data = ?
            WHERE id = ?
    """, (nova_descricao, novo_valor, novo_tipo, nova_data, indice))
    conexao.commit()
    conexao.close()
    print('\nTransação Atualizada com Sucesso.')
    voltar_menu()

def deletar_tr():
    os.system('cls')
    print('𝙳𝚎𝚕𝚎𝚝𝚊𝚛 𝚃𝚛𝚊𝚗𝚜𝚊𝚌̧𝚊̃𝚘\n')
    mostrar_tr()
    indice = validar_id()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM transacoes
        WHERE id = ?
    """, (indice,))
    transacao = cursor.fetchone()
    print('Deseja Deletar Esta Transação?\n')
    print(f"Descrição: {transacao[1]}")
    print(f"Valor: R${transacao[2]:.2f}")
    print(f"Tipo: {transacao[3]}")
    print(f"Data: {transacao[4]}")
    confirmacao = input('\n[S/N]: ').upper()
    if confirmacao == 'S':
        cursor.execute("""
        DELETE FROM transacoes
        WHERE id = ?
    """, (indice,))
        conexao.commit()
        print('\nTransação deletada com sucesso!')
    else:
        print('\nOperação cancelada.')
    conexao.close()
    voltar_menu()

def saldo():
    os.system('cls')
    print('𝚂𝚊𝚕𝚍𝚘\n')
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT data, valor, tipo FROM transacoes")
    transacoes = cursor.fetchall()
    conexao.close()
    print(f"{'𝙳𝚊𝚝𝚊:'.ljust(15)} | {'𝚅𝚊𝚕𝚘𝚛:'.ljust(15)} ")
    contador = 0
    for transacao in transacoes:
        data = transacao[0]
        valor = transacao[1]
        tipo = transacao[2]
        print(f'{data.ljust(15)} | R${valor:.2f}')
        if tipo == 'Entrada':
            contador += valor
        else:
            contador -= valor
    print(f'\nSeu saldo atual é: R${contador:.2f}')
    voltar_menu()

def validar_id():
    while True:
        try:
            indice = int(input('\nDigite o ID da Transação: '))
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT id FROM transacoes
                WHERE id = ?
            """, (indice,))
            transacao = cursor.fetchone()
            conexao.close()
            if transacao is None:
                print('ID Inválido!')
            else:
                return indice
        except ValueError:
            print('Digite um ID Válido.')

def mostrar_tr():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM transacoes")
    transacoes = cursor.fetchall()
    print(f"{'ID'.ljust(5)} | {'𝙳𝚎𝚜𝚌𝚛𝚒𝚌̧𝚊̃𝚘:'.ljust(15)} | {'𝚅𝚊𝚕𝚘𝚛:'.ljust(15)} | {'Tipo:'.ljust(15)} | {'𝙳𝚊𝚝𝚊:'.ljust(15)}")
    for transacao in transacoes:
        indice = transacao[0]
        descricao = transacao[1]
        valor = transacao[2]
        tipo = transacao[3]
        data = transacao[4]
        print(f"{f'{indice:03}'.ljust(5)} | {descricao.ljust(13)} | R${str(valor).ljust(13)} | {tipo.ljust(15)} | {data.ljust(15)}")
    conexao.close()

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
    
    criar_tabela()

    while True:     
        os.system('cls')
        menu()
        escolher_opcao()

if __name__ == '__main__':
    main()
