import os
import pickle
from .menu_monstro import menu_monstros
from Inventory.DADOS_pycharm import mostrar_historico, jogar_dado
from Modulo_do_Jogador.historico import gerar_pdf_ficha_especifica
from Inventory import DADOS_pycharm
from modulo_mestre.menu_jogador_mestre import menu_mestre_personagem


def menu_mestre():
    print("\n=== MENU MESTRE ===")
    print("1. Acessar Menu de Monstros")
    print("2. Acessar Menu *MESTRE* DE PERSONAGENS")
    print("3. Rolar dado")
    print("4. Histórico rolagem de dados")
    print("0. Sair.")

def mestre_menu():
    while True:
        menu_mestre()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_monstros()
        elif opcao == "2":
            menu_mestre_personagem()
        elif opcao == "3":
            dado = input("Escolha um dado:\nD4\nD6\nD8\nD10\nD12\nD20\n")
            while True:
                try:
                    quantia = int(input(f'Quantos {dado} deseja rolar?(Max 15)'))
                except ValueError:
                    print("Digite um numero inteiro positivo.")
                break
            jogar_dado(dado, quantia)
        elif opcao == "4":
            mostrar_historico()
        elif opcao == "0":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    mestre_menu()