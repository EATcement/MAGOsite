from historico import gerar_pdf_ficha_especifica
from edicao import editar_ficha
from excluir import excluir_ficha
from inventario import menu_inventario

def menu_ficha_personagem():
    print("\n=== MENU FICHA DE PERSONAGEM ===")
    print("1. Histórico de ficha de personagem")
    print("2. Edição de ficha")
    print("3. Inventário de personagem")
    print("4. Excluir ficha")
    print("0. Sair")

def main():
    while True:
        menu_ficha_personagem()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            gerar_pdf_ficha_especifica()
        elif opcao == "2":
            editar_ficha()
        elif opcao == "3":
            menu_inventario()
        elif opcao == "4":
            excluir_ficha()
        elif opcao == "0":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
