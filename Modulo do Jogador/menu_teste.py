from Modulo_criacao_de_fichas.Criacao_Fichas.Fichas_jogador import criar_ficha, exibir_ficha, salvar_ficha, obter_caminho_fichas
from Inventory.inventario_modulo import (
    carregar_ficha_personagem,
    add_kit,
    mostrar_inventario,
    adicionar_item,
    remover_item,
    editar_ouro,
    inventario,
    definir_ficha,
    salvar_inventario

)
def menu_inventario(ficha):
    add_kit(ficha)
    while True:
        print("\n--- MENU DE INVENTÁRIO ---")
        print("1. Mostrar inventário")
        print("2. Adicionar item")
        print("3. Remover item")
        print("4. Editar ouro")
        print("5. Finalizar e salvar inventário")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_inventario()
        elif escolha == "2":
            nome = input("Nome do item: ")
            quantidade = input("Quantidade: ")
            peso = input("Peso por unidade (kg): ")
            adicionar_item(nome, quantidade, peso)
        elif escolha == "3":
            mostrar_inventario()
            pos = input("Digite o número do item para remover: ")
            remover_item(int(pos) - 1)
        elif escolha == "4":
            valor = input("Quantidade de ouro a adicionar/remover: ")
            editar_ouro(valor)
        elif escolha == "5":
            salvar_inventario(ficha["nome"])
            print("Inventário salvo e sessão finalizada.")
            break
        else:
            print("Opção inválida.")

def main():
    while True:
        print("\n===== MENU MESTRE =====")
        print("1. Criar novo personagem")
        print("2. Acessar inventário de uma ficha existente")
        print("3. Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            ficha = criar_ficha()
            exibir_ficha(ficha)
            salvar_ficha(ficha)
            definir_ficha(ficha)
            salvar_inventario(ficha["nome"])
            print("\nFicha criada com sucesso! Acessando inventário...")
            menu_inventario(ficha)


        elif op == "2":
            nome = input("Nome do personagem: ")
            ficha = carregar_ficha_personagem(nome)
            if ficha:
                definir_ficha(ficha)
                print(f"Ficha de {nome} carregada com sucesso.")
                menu_inventario(ficha)
            else:
                print("Ficha não encontrada.")

        elif op == "3":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()