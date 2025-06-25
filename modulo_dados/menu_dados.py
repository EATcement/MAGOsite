from Inventory.DADOS_pycharm import jogar_dado, mostrar_historico

def menu_dados():
    print("\n=== MENU DE DADOS ===")
    print("1. Rodar dados")
    print("2. Histórico de dados")
    print("0. Sair")

def dados_menu():
    while True:
        menu_dados()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dado = input("Escolha um dado:\nD4\nD6\nD8\nD10\nD12\nD20\n").lower()
            while True:
                try:
                    quantia = int(input(f'Quantos {dado} deseja rolar?(Max 15)'))
                except ValueError:
                    print("Digite um numero inteiro positivo.")
                break
            jogar_dado(dado, quantia)
        elif opcao == "2":
            mostrar_historico()
        elif opcao == "0":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    dados_menu()