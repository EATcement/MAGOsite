import pickle
import os
from .gerar_pdf_monstro import gerar_pdf_monstro

def carregar_ficha_monstro():
    pasta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "monstros"))
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".pkl")]

    if not arquivos:
        print("Nenhuma ficha de monstro encontrada.")
        return

    print("\nFichas de monstro disponíveis:")
    for idx, nome in enumerate(arquivos, 1):
        print(f"{idx}. {nome.replace('.pkl', '')}")

    while True:
        escolha = input("\nDigite o número da ficha para gerar o PDF: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(arquivos):
                nome_arquivo = arquivos[escolha - 1]
                break
        print("Opção inválida. Tente novamente.")

    caminho_ficha = os.path.join(pasta, nome_arquivo)
    with open(caminho_ficha, "rb") as arq:
        monstro = pickle.load(arq)

    # Definir o caminho de saída do PDF
    nome_pdf = nome_arquivo.replace(".pkl", ".pdf")
    pasta_saida = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdfs", "monstros_pdf"))
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_pdf = os.path.join(pasta_saida, nome_pdf)

    # Gerar o PDF
    gerar_pdf_monstro(caminho_pdf, monstro)
    print(f"\nPDF gerado com sucesso: {caminho_pdf}")

if __name__ == "__main__":
    carregar_ficha_monstro()
