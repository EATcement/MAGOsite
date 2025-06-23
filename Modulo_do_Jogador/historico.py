import os
import pickle
from gerar_pdf import gerar_pdf_sem_fundo  

PASTA_FICHAS = os.path.join(os.path.dirname(__file__), "fichas")
PASTA_PDFS = "pdfs"

def gerar_pdf_ficha_especifica():
    if not os.path.exists(PASTA_FICHAS):
        print(f"Pasta {PASTA_FICHAS} não encontrada.")
        return

    # Lista só arquivos de ficha, ignorando inventários
    arquivos = [f for f in os.listdir(PASTA_FICHAS) 
                if f.endswith(".pkl") and not f.endswith("_inventario.pkl")]
    if not arquivos:
        print("Nenhuma ficha .pkl encontrada na pasta.")
        return

    print("Fichas disponíveis:")
    nomes_fichas = [arquivo.replace(".pkl", "") for arquivo in arquivos]
    for nome in nomes_fichas:
        print(f"- {nome}")

    escolha = input("Digite o nome da ficha que deseja visualizar: ").strip().lower().replace(" ", "_")

    arquivo_escolhido = None
    for arquivo in arquivos:
        nome_arquivo = arquivo.replace(".pkl", "").lower().replace(" ", "_")
        if escolha == nome_arquivo:
            arquivo_escolhido = arquivo
            break

    if not arquivo_escolhido:
        print("Ficha não encontrada.")
        return

    caminho_ficha = os.path.join(PASTA_FICHAS, arquivo_escolhido)
    nome_ficha = arquivo_escolhido.replace(".pkl", "").lower().replace(" ", "_")
    caminho_inventario = os.path.join(PASTA_FICHAS, f"{nome_ficha}_inventario.pkl")

    try:
        # Carrega ficha
        with open(caminho_ficha, "rb") as f:
            ficha = pickle.load(f)

        # Tenta carregar inventário correspondente, se existir
        inventario = {}
        if os.path.exists(caminho_inventario):
            with open(caminho_inventario, "rb") as f:
                inventario = pickle.load(f)

        os.makedirs(PASTA_PDFS, exist_ok=True)
        caminho_pdf = os.path.join(PASTA_PDFS, f"ficha_{nome_ficha}.pdf")

        # Passa ficha e inventário para o gerador de PDF (modifique gerar_pdf_sem_fundo para aceitar inventario)
        gerar_pdf_sem_fundo(caminho_pdf, ficha, inventario)

        print(f"PDF gerado com sucesso em: {caminho_pdf}")

    except Exception as e:
        print(f"Erro ao processar '{arquivo_escolhido}': {e}")

if __name__ == "__main__":
    gerar_pdf_ficha_especifica()
