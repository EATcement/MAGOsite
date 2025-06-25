from Inventory.DADOS_pycharm import mostrar_historico, jogar_dado
from .menu_funcionalidades import menu_gerador_nomes
def menu_mestre():
    print("\n=== MENU de Funcionalidades ===")
    print("1. Rodar dados")
    print("2. Histórico rolagem de dados")
    print("3. Gerador de Nomes de Fantasia")
    print("0. Sair.")

def menu_funcionalidades():
    while True:
        menu_mestre()
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

        elif opcao == "3":
            menu_gerador_nomes()
        elif opcao == "0":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
 menu_funcionalidades()