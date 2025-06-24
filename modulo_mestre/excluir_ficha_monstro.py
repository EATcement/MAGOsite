import os

def excluir_ficha_monstro():
    pasta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "monstros"))
    pdf_pasta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdfs", "monstros_pdf"))

    arquivos = [f for f in os.listdir(pasta) if f.endswith(".pkl")]

    if not arquivos:
        print("Nenhuma ficha de monstro encontrada.")
        return

    print("\nFichas de monstro disponíveis:")
    for idx, nome in enumerate(arquivos, 1):
        print(f"{idx}. {nome.replace('.pkl', '')}")

    while True:
        escolha = input("Digite o número da ficha a excluir: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(arquivos):
                nome_arquivo = arquivos[escolha - 1]
                break
        print("Opção inválida. Tente novamente.")

    nome_base = nome_arquivo.replace(".pkl", "")
    caminho_pkl = os.path.join(pasta, nome_arquivo)
    caminho_pdf = os.path.join(pdf_pasta, f"{nome_base.lower().replace(' ', '_')}.pdf")

    confirmacao = input(f"Tem certeza que deseja excluir '{nome_base}' e seu PDF? Digite \"sim\" para confirmar: ").lower()
    if confirmacao == "sim":
        if os.path.exists(caminho_pkl):
            os.remove(caminho_pkl)
            print(f"Arquivo {nome_arquivo} removido.")
        else:
            print(f"Arquivo .pkl não encontrado: {caminho_pkl}")

        if os.path.exists(caminho_pdf):
            os.remove(caminho_pdf)
            print(f"PDF {os.path.basename(caminho_pdf)} removido.")
        else:
            print(f"PDF não encontrado: {caminho_pdf}")
    else:
        print("\"sim\" não detectado, exclusão abortada.")

if __name__ == "__main__":
    excluir_ficha_monstro()
