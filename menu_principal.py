import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))



from modulo_mestre.menu_mestre import mestre_menu as menu_ficha_mestre
from Modulo_criacao_de_fichas.Criacao_Fichas.menu_fichas import menu_principal as menu_criacao_fichas
from Modulo_do_Jogador.menu import main as menu_ficha_personagem_main   

def menu_principal():
    while True:
        print("\n===== SISTEMA DE RPG =====")
        print("1. Acessar módulo de criação de fichas")
        print("2. Acessar módulo do jogador")
        print("3. Acessar modulo do mestre")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_criacao_fichas()
        elif escolha == "2":
            menu_ficha_personagem_main()
        elif escolha =="3":
            menu_ficha_mestre()
        elif escolha == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
