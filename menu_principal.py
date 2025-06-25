import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from modulo_diario.diario_aventura_editado import menu_diario
from modulo_funcionalidades.menu_funcs import menu_funcionalidades
from modulo_mestre.menu_mestre import mestre_menu as menu_ficha_mestre
from Modulo_criacao_de_fichas.Criacao_Fichas.menu_fichas import menu_principal as menu_criacao_fichas
from Modulo_do_Jogador.menu import main as menu_ficha_personagem_main

def menu_principal():
    while True:
        print("\n" + "=" * 37)
        print("      ✦✦ SISTEMA DE RPG ✦✦")
        print("=" * 37)
        print("1 - Criar ficha de personagem")
        print("2 - Módulo do jogador")
        print("3 - Módulo do mestre")
        print("4 - Diário de Aventura")
        print("5 - Funções extras")
        print("0 - Sair")
        print("=" * 37)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_criacao_fichas()
        elif escolha == "2":
            menu_ficha_personagem_main()
        elif escolha =="3":
            menu_ficha_mestre()
        elif escolha == "4":
            menu_diario()
        elif escolha == "5":
            menu_funcionalidades()
        elif escolha == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
