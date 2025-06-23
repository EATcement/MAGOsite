import os
import pickle
from gerar_pdf import gerar_pdf_sem_fundo

PASTA_FICHAS = r"C:\Users\Isabelle\Documents\GitHub\MAGOsite\Modulo_criacao_de_fichas\Criacao_Fichas\fichas"
PASTA_PDFS = "pdfs"

def editar_ficha():
    if not os.path.exists(PASTA_FICHAS):
        print(f"Pasta {PASTA_FICHAS} não encontrada.")
        return

    arquivos = [f for f in os.listdir(PASTA_FICHAS) if f.endswith(".pkl") and not f.endswith("_inventario.pkl")]
    if not arquivos:
        print("Nenhuma ficha .pkl encontrada.")
        return

    print("Fichas disponíveis:")
    for idx, arquivo in enumerate(arquivos, 1):
        print(f"{idx}. {arquivo.replace('.pkl', '')}")

    escolha = input("Digite o nome da ficha que deseja editar: ").strip().lower().replace(" ", "_") + ".pkl"
    caminho_ficha = os.path.join(PASTA_FICHAS, escolha)

    if not os.path.exists(caminho_ficha):
        print("Ficha não encontrada.")
        return

    with open(caminho_ficha, "rb") as f:
        ficha = pickle.load(f)

    print(f"\n--- Editando ficha de: {ficha.get('nome', 'Desconhecido')} ---")

    while True:
        print("\nO que deseja modificar?")
        print("1. Idade")
        print("2. Nível")
        print("3. HP")
        print("4. Atributos")
        print("0. Sair da edição")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nova_idade = input(f"Idade atual: {ficha.get('idade', '')} | Nova idade: ").strip()
            if nova_idade:
                ficha["idade"] = nova_idade

        elif opcao == "2":
            novo_nivel = input(f"Nível atual: {ficha.get('nível', '')} | Novo nível (1-20): ").strip()
            if novo_nivel.isdigit() and 1 <= int(novo_nivel) <= 20:
                ficha["nível"] = int(novo_nivel)
            else:
                print("Valor inválido.")

        elif opcao == "3":
            novo_hp = input(f"HP atual: {ficha.get('HP', '')} | Novo HP: ").strip()
            if novo_hp.isdigit():
                ficha["HP"] = int(novo_hp)
            else:
                print("Valor inválido.")

        elif opcao == "4":
            atributos = ficha.get("atributos", {})
            for atributo, valor in atributos.items():
                novo_valor = input(f"{atributo} atual: {valor} | Novo {atributo} (ou Enter para manter): ").strip()
                if novo_valor.isdigit() and 1 <= int(novo_valor) <= 20:
                    atributos[atributo] = int(novo_valor)
            ficha["atributos"] = atributos

        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Salvar .pkl atualizado
    with open(caminho_ficha, "wb") as f:
        pickle.dump(ficha, f)
    print("Ficha atualizada com sucesso!")

    # Atualizar PDF
    os.makedirs(PASTA_PDFS, exist_ok=True)
    nome_ficha = ficha.get("nome", "sem_nome").lower().replace(" ", "_")
    caminho_pdf = os.path.join(PASTA_PDFS, f"ficha_{nome_ficha}.pdf")
    gerar_pdf_sem_fundo(caminho_pdf, ficha)
    print(f"PDF também atualizado: {caminho_pdf}")


if __name__ == "__main__":
    editar_ficha()
