import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))




from Modulo_criacao_de_fichas.Criacao_Fichas.menu_fichas import menu_principal as menu_criacao_fichas

def menu_principal():
    while True:
        print("\n===== SISTEMA DE RPG =====")
        print("1. Acessar módulo de criação de fichas")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_criacao_fichas()
        elif escolha == "2":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
