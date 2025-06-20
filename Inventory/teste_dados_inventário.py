from inventario import *
from DADOS_pycharm import *

def pausar():
    input("\nPressione ENTER para continuar...")

def menu_dados():
    while True:
        print("\n--- MENU DO SISTEMA DE DADOS ---")
        print("1. Rolar um dado")
        print("2. Ver histórico de rolagens")
        print("3. Voltar ao menu principal")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == "1":
            escolher_dado()

        elif escolha == "2":
            mostrar_historico()
            pausar()

        elif escolha == "3":
            break

        else:
            print("Opção inválida! Escolha um número de 1 a 3.")

def escolher_dado():
    while True:
        print("\n--- ESCOLHA O TIPO DE DADO ---")
        print("1 - D4")
        print("2 - D6")
        print("3 - D8")
        print("4 - D10")
        print("5 - D12")
        print("6 - D20")
        print("7 - Voltar ao menu de dados")

        escolha = input("Escolha o dado (1-7): ")

        if escolha == "1":
            jogar_d4()
            pausar()
        elif escolha == "2":
            jogar_d6()
            pausar()
        elif escolha == "3":
            jogar_d8()
            pausar()
        elif escolha == "4":
            jogar_d10()
            pausar()
        elif escolha == "5":
            jogar_d12()
            pausar()
        elif escolha == "6":
            jogar_d20()
            pausar()
        elif escolha == "7":
            break
        else:
            print("Opção inválida! Escolha de 1 a 7.")

def menu_inventario():
    while True:
        print("\n--- MENU DO INVENTÁRIO ---")
        print("1. Ver inventário")
        print("2. Adicionar item manualmente")
        print("3. Aplicar kit da classe")
        print("4. Editar ouro")
        print("5. Ver capacidade de carga")
        print("6. Ver peso total dos itens")
        print("7. Remover item do inventário")
        print("8. Voltar ao menu principal")

        escolha = input("Escolha uma opção (1-8): ")

        if escolha == "1":
            mostrar_inventario()
            pausar()

        elif escolha == "2":
            nome = input("Nome do item: ")
            quantidade = input("Quantos: ")
            peso = input("Peso por unidade (kg): ")
            try:
                quantidade = int(quantidade)
                peso = float(peso)
                adicionar_item(nome, quantidade, peso)
            except ValueError:
                print("Quantia ou peso inválidos!")

        elif escolha == "3":
            add_kit()
            pausar()

        elif escolha == "4":
            quantia = input("Quanto ouro adicionar/remover? (use negativo para remover): ")
            try:
                quantia = int(quantia)
                editar_ouro(quantia)
            except ValueError:
                print("Valor inválido!")

        elif escolha == "5":
            capacidade = calcular_capacidade_peso()
            print(f"Capacidade de carga: {capacidade} Kg")
            pausar()

        elif escolha == "6":
            peso = calc_peso_itens()
            print(f"Peso total dos itens: {peso} Kg")
            pausar()

        elif escolha == "7":
            if not inventario["itens"]:
                print("Inventário vazio!")
                continue
            print("\nItens no inventário:")
            for idx, (item, info) in enumerate(inventario["itens"].items(), start=0):
                print(f"{idx}: {item} ({info['quantidade']} unidades, {info['peso']} Kg cada)")

            pos = input("Digite o número do item que deseja remover: ")
            if pos.isdigit():
                pos = int(pos)
                remover_item(pos)
            else:
                print("Entrada inválida!")

        elif escolha == "8":
            break

        else:
            print("Opção inválida! Escolha um número de 1 a 8.")

def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Sistema de Inventário")
        print("2. Sistema de Dados")
        print("3. Sair")

        escolha = input("Escolha uma opção (1-3): ")

        if escolha == "1":
            menu_inventario()
        elif escolha == "2":
            menu_dados()
        elif escolha == "3":
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("Opção inválida! Escolha de 1 a 3.")

if __name__ == "__main__":
    menu_principal()
