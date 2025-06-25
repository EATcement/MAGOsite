from .menu_monstro import menu_monstros
from modulo_mestre.menu_jogador_mestre import menu_mestre_personagem



def menu_mestre():
    print("\n=== MENU MESTRE ===")
    print("1. Acessar Menu de Monstros")
    print("2. Acessar Menu *MESTRE* DE PERSONAGENS")
    print("0. Sair.")

def mestre_menu():
    while True:
        menu_mestre()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_monstros()
        elif opcao == "2":
            menu_mestre_personagem()
        elif opcao == "0":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    mestre_menu()