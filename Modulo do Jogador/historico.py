import os
import pickle
from gerar_pdf import gerar_pdf_com_visual

PASTA_FICHAS = "C:/Users/Isabelle/Documents/GitHub/MAGOsite/fichas"
IMAGEM_FUNDO = "C:/Users/Isabelle/Documents/GitHub/MAGOsite/Modulo do Jogador/Ficha Personagem 3.jpg"
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

    # Procura o arquivo correspondente ao nome informado
    arquivo_escolhido = None
    for arquivo in arquivos:
        nome_sem_ext = arquivo.replace(".pkl", "").lower().replace(" ", "_")
        if escolha == nome_sem_ext:
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
        gerar_pdf_com_visual(caminho_pdf, ficha, IMAGEM_FUNDO)
        print(f"PDF gerado: {caminho_pdf}")
    except Exception as e:
        print(f"Erro ao processar {arquivo_escolhido}: {e}")

if __name__ == "__main__":
    # Para gerar todos os PDFs, descomente:
    # gerar_todos_pdfs()

    # Para gerar PDF de ficha específica por nome:
    gerar_pdf_ficha_especifica()
