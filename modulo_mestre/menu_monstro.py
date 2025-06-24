from .editar_ficha_monstro import editar_ficha_monstro
from .gerar_pdf_monstro_script import carregar_ficha_monstro
from .excluir_ficha_monstro import excluir_ficha_monstro


def menu_monstros():
    while True:
        print("\n===== MENU DE MONSTROS =====")
        print("1. Editar ficha de monstro existente")
        print("2. Gerar PDF de ficha de monstro")
        print("3. Excluir ficha de monstro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            editar_ficha_monstro()
        elif opcao == "2":
            carregar_ficha_monstro()
        elif opcao == "3":
            excluir_ficha_monstro()
        elif opcao == "0":
            print("Saindo do menu de monstros...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_monstros()
