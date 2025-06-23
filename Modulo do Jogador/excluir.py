import os
import pickle

def excluir_ficha():
    try:
        with open("dicionarios.pkl", "rb") as f:
            dicionarios = pickle.load(f)
    except FileNotFoundError:
        print("❌ Arquivo 'dicionarios.pkl' não encontrado.")
        return

    print("\n📋 IDs de fichas disponíveis:")
    for id_ficha in dicionarios:
        print(f" - {id_ficha}")

    id_excluir = input("\nDigite o ID da ficha que deseja excluir: ").strip()

    if id_excluir not in dicionarios:
        print("⚠️ ID não encontrado.")
        return

    # Confirmação
    confirmar = input(f"Tem certeza que deseja excluir a ficha '{id_excluir}'? (s/n): ").strip().lower()
    if confirmar != 's':
        print("❌ Exclusão cancelada.")
        return

    # Remove a ficha do dicionário
    del dicionarios[id_excluir]

    # Salva o novo dicionário no arquivo
    with open("dicionarios.pkl", "wb") as f:
        pickle.dump(dicionarios, f)

    # Caminho do PDF correspondente
    nome_pdf = os.path.join("pdfs", f"ficha_{id_excluir}.pdf")

    # Tenta remover o PDF se existir
    if os.path.exists(nome_pdf):
        os.remove(nome_pdf)
        print(f"🗑️ PDF '{nome_pdf}' excluído.")
    else:
        print("⚠️ Nenhum PDF correspondente encontrado para excluir.")

    print("✅ Ficha excluída com sucesso.")
