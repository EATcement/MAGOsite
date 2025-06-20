from historico import historico_ficha_personagem
from edicao import editar_ficha
from inventario import abrir_inventario
from excluir import excluir_ficha

def menu_ficha_personagem():
    print("\n=== MENU FICHA DE PERSONAGEM ===")
    print("1. Histórico de ficha de personagem")
    print("2. Edição de ficha")
    print("3. Inventário de personagem")
    print("4. Excluir ficha")
    print("0. Sair")

while True:
    menu_ficha_personagem()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        historico_ficha_personagem()
    elif opcao == "2":
        editar_ficha()
    elif opcao == "3":
        abrir_inventario()
    elif opcao == "4":
        excluir_ficha()
    elif opcao == "0":
        print("Saindo do menu.")
        break
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
