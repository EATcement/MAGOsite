import os
import pickle
from gerar_pdf import gerar_pdf_sem_fundo  # Função para gerar PDF sem imagem de fundo

# Use raw string (r"") para evitar problemas com backslashes
PASTA_FICHAS = r"C:\Users\Isabelle\Documents\GitHub\MAGOsite\Modulo_criacao_de_fichas\Criacao_Fichas\fichas"
PASTA_PDFS = "pdfs"

def gerar_pdf_ficha_especifica():
    if not os.path.exists(PASTA_FICHAS):
        print(f"Pasta {PASTA_FICHAS} não encontrada.")
        return

    arquivos = [f for f in os.listdir(PASTA_FICHAS) if f.endswith(".pkl")]
    if not arquivos:
        print("Nenhuma ficha .pkl encontrada na pasta.")
        return

    print("Fichas disponíveis:")
    nomes_fichas = [arquivo.replace(".pkl", "") for arquivo in arquivos]
    for nome in nomes_fichas:
        print(f"- {nome}")

    escolha = input("Digite o nome da ficha que deseja visualizar: ").strip().lower().replace(" ", "_")

    # Procurar arquivo correspondente ao nome informado
    arquivo_escolhido = None
    for arquivo in arquivos:
        nome_arquivo = arquivo.replace(".pkl", "").lower().replace(" ", "_")
        if escolha == nome_arquivo:
            arquivo_escolhido = arquivo
            break

    if not arquivo_escolhido:
        print("Ficha não encontrada.")
        return

    caminho_pkl = os.path.join(PASTA_FICHAS, arquivo_escolhido)

    try:
        with open(caminho_pkl, "rb") as f:
            ficha = pickle.load(f)

        nome_ficha = ficha.get("nome", "sem_nome").lower().replace(" ", "_")

        os.makedirs(PASTA_PDFS, exist_ok=True)
        caminho_pdf = os.path.join(PASTA_PDFS, f"ficha_{nome_ficha}.pdf")

        # Gera o PDF sem imagem de fundo
        gerar_pdf_sem_fundo(caminho_pdf, ficha)

        print(f"PDF gerado com sucesso em: {caminho_pdf}")

    except Exception as e:
        print(f"Erro ao processar '{arquivo_escolhido}': {e}")

if __name__ == "__main__":
    gerar_pdf_ficha_especifica()
