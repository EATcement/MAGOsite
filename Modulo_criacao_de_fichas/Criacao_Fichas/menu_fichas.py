
from Modulo_criacao_de_fichas.Criacao_Fichas.Fichas_jogador import main as menu_ficha_personagem
from Modulo_criacao_de_fichas.Criacao_Fichas.Fichas_Monstros import main as menu_ficha_monstro


def menu_principal():
    while True:
        print("\n===== MENU DE CRIAÇÃO DE FICHAS =====")
        print("1. Criar ficha de monstro")
        print("2. Criar ficha de personagem")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_ficha_monstro()
        elif escolha == "2":
             menu_ficha_personagem()
        elif escolha == "0":
            print("Saindo do criador de fichas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    menu_principal()
