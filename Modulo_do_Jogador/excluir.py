import os

def excluir_ficha():
    pasta_fichas = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Modulo_criacao_de_fichas", "Criacao_Fichas", "fichas"))
    pasta_pdfs = "pdfs"       # pasta onde estão os PDFs gerados

    # Verifica se a pasta de fichas existe
    if not os.path.exists(pasta_fichas):
        print(f"❌ A pasta '{pasta_fichas}' não foi encontrada.")
        return

    # Lista os arquivos .pkl da pasta
    arquivos = [f for f in os.listdir(pasta_fichas) if f.endswith(".pkl")]
    if not arquivos:
        print(f"⚠️ Nenhum arquivo .pkl encontrado na pasta '{pasta_fichas}'.")
        return

    print("\n📋 Fichas disponíveis para exclusão:")
    for arq in arquivos:
        nome_sem_ext = arq[:-4]  # tira o '.pkl'
        print(f" - {nome_sem_ext}")

    id_excluir = input("\nDigite o nome da ficha que deseja excluir: ").strip()

    # Verifica se arquivo existe
    nome_arquivo_pkl = f"{id_excluir}.pkl"
    if nome_arquivo_pkl not in arquivos:
        print("⚠️ Ficha não encontrada.")
        return

    confirmar = input(f"Tem certeza que deseja excluir a ficha '{id_excluir}'? (s/n): ").strip().lower()
    if confirmar != 's':
        print("❌ Exclusão cancelada.")
        return

    # Remove o arquivo .pkl
    caminho_pkl = os.path.join(pasta_fichas, nome_arquivo_pkl)
    try:
        os.remove(caminho_pkl)
        print(f"🗑️ Ficha '{nome_arquivo_pkl}' excluída.")
    except Exception as e:
        print(f"❌ Erro ao excluir arquivo .pkl: {e}")
        return

    # Remove o PDF correspondente
    nome_pdf = os.path.join(pasta_pdfs, f"ficha_{id_excluir}.pdf")
    if os.path.exists(nome_pdf):
        try:
            os.remove(nome_pdf)
            print(f"🗑️ PDF '{nome_pdf}' excluído.")
        except Exception as e:
            print(f"⚠️ Erro ao excluir PDF: {e}")
    else:
        print("⚠️ Nenhum PDF correspondente encontrado para excluir.")

    print("✅ Exclusão concluída com sucesso.")
