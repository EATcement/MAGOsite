import os
import pickle
from gerar_pdf import gerar_pdf_com_visual

def historico_ficha_personagem():
    try:
        with open("dicionarios.pkl", "rb") as f:
            dicionarios = pickle.load(f)
    except FileNotFoundError:
        print("❌ Erro: Arquivo 'dicionarios.pkl' não encontrado.")
        return

    print("\n📋 IDs de fichas disponíveis:")
    for id_disponivel in dicionarios.keys():
        print(f" - {id_disponivel}")

    id_usuario = input("\nDigite o ID desejado para gerar o PDF: ").strip()

    if id_usuario not in dicionarios:
        print(f"⚠️ ID '{id_usuario}' não encontrado.")
        return

    output_dir = "pdfs"
    os.makedirs(output_dir, exist_ok=True)
    nome_pdf = os.path.join(output_dir, f"ficha_{id_usuario}.pdf")

    caminho_imagem_fundo = "C:/Users/Isabelle/Documents/GitHub/MAGOsite/Modulo do Jogador/Ficha Personagem 3.jpg"

    gerar_pdf_com_visual(nome_pdf, dicionarios[id_usuario], imagem_fundo=caminho_imagem_fundo)

    print(f"\n✅ PDF gerado com sucesso: {nome_pdf}")
