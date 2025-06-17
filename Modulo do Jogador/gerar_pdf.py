import os
import pickle
from fpdf import FPDF

# Carregar o dicionário do arquivo .pkl
try:
    with open("dicionarios.pkl", "rb") as f:
        dicionarios = pickle.load(f)
except FileNotFoundError:
    print("Erro: Arquivo 'dicionarios.pkl' não encontrado. Rode 'salvar_dicionario.py' primeiro.")
    exit(1)

# Função para gerar o PDF
def gerar_pdf(nome_arquivo, data_dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for chave, valor in data_dict.items():
        texto = f"{chave}: {valor}" if not isinstance(valor, list) else f"{chave}:"
        pdf.cell(200, 10, txt=texto, ln=True)

        if isinstance(valor, list):
            for item in valor:
                pdf.cell(200, 10, txt=f"   - {item}", ln=True)

    pdf.output(nome_arquivo)

# Função para gerar o PDF de um dicionário específico
def gerar_pdf_especifico(id):
    if id not in dicionarios:
        print(f"Dicionário com id '{id}' não encontrado.")
        return

    data = dicionarios[id]
    output_dir = "pdfs/"
    os.makedirs(output_dir, exist_ok=True)

    nome_pdf = f"{output_dir}dicionario_{id}.pdf"
    gerar_pdf(nome_pdf, data)

    print(f"\n✅ PDF gerado com sucesso: {nome_pdf}")

# Mostra os IDs disponíveis
print("IDs disponíveis:")
for id_disponivel in dicionarios.keys():
    print(f" - {id_disponivel}")

# Solicita o ID ao usuário
id_usuario = input("\nDigite o ID desejado para gerar o PDF: ").strip()

# Gera o PDF com base no input
gerar_pdf_especifico(id_usuario)
