from historico import gerar_pdf_ficha_especifica
from edicao import editar_ficha
from Inventory.inventario_modulo import inventario, salvar_inventario,  escolher_ficha, carregar_ficha_personagem, adicionar_item, mostrar_inventario, editar_ouro, remover_item, add_kit, calcular_capacidade_peso, calc_peso_itens
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
        gerar_pdf_ficha_especifica()
    elif opcao == "2":
        editar_ficha()
    elif opcao == "3":
        mostrar_inventario()
    elif opcao == "4":
        excluir_ficha()
    elif opcao == "0":
        print("Saindo do menu.")
        break
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
