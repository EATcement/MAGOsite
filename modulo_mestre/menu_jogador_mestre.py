from modulo_mestre.editar_ficha_mestre import editar_ficha_mestre

try:
    from fpdf import FPDF
except ImportError:
    import subprocess
    import sys
    print("Pacote 'fpdf2' não encontrado. Instalando automaticamente...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2"])
    from fpdf import FPDF  # Tenta importar novamente após instalação


# Agora pode importar normalmente os módulos que usam fpdf
from Modulo_do_Jogador.historico import gerar_pdf_ficha_especifica
from Modulo_do_Jogador.excluir import excluir_ficha
from Modulo_do_Jogador.inventario import menu_inventario


def menu_ficha_personagem():
    print("\n=== MENU DE PERSONAGENS *MESTRE*===")
    print("1. Gerar PDF de ficha")
    print("2. Edição *MESTRE* de ficha")
    print("3. Inventário de personagem")
    print("4. Excluir ficha")
    print("0. Sair")

def menu_mestre_personagem():
    while True:
        menu_ficha_personagem()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            gerar_pdf_ficha_especifica()
        elif opcao == "2":
            editar_ficha_mestre()
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
    menu_mestre_personagem()



