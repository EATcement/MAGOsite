import os
import pickle
from fpdf import FPDF

PASTA_DIARIOS = os.path.abspath(os.path.join(os.path.dirname(__file__), "diarios"))
os.makedirs(PASTA_DIARIOS, exist_ok=True)

def quebrar_palavras_longas(texto, limite=60):
    def forcar_quebra(palavra):
        if len(palavra) <= limite:
            return palavra
        return '\u200b'.join([palavra[i:i+limite] for i in range(0, len(palavra), limite)])
    return ' '.join(forcar_quebra(p) for p in texto.split())


def listar_diarios_existentes():
    arquivos = [f for f in os.listdir(PASTA_DIARIOS) if f.endswith("_diario.pkl")]
    if not arquivos:
        print("Nenhum diário encontrado.")
        return None
    print("\nDiários disponíveis:")
    for idx, f in enumerate(arquivos, 1):
        print(f"{idx}. {f.replace('_diario.pkl', '')}")

    while True:
        esc = input("Escolha o número do diário: ").strip()
        if esc.isdigit() and 1 <= int(esc) <= len(arquivos):
            return arquivos[int(esc)-1].replace("_diario.pkl", "")
        print("Opção inválida.")

def selecionar_personagem_com_ficha():
    return listar_diarios_existentes()

def criar_diario():
    pasta_fichas = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Modulo_criacao_de_fichas", "Criacao_Fichas", "fichas"))
    arquivos = [f for f in os.listdir(pasta_fichas) if f.endswith(".pkl") and not f.endswith("_inventario.pkl")]
    if not arquivos:
        print("Nenhuma ficha encontrada.")
        return None

    print("\nPersonagens disponíveis:")
    for idx, f in enumerate(arquivos, 1):
        print(f"{idx}. {f.replace('.pkl', '')}")

    while True:
        esc = input("Escolha o número do personagem: ").strip()
        if esc.isdigit() and 1 <= int(esc) <= len(arquivos):
            nome = arquivos[int(esc)-1].replace(".pkl", "")
            break
        print("Opção inválida.")

    caminho = os.path.join(PASTA_DIARIOS, f"{nome.lower()}_diario.pkl")
    if os.path.exists(caminho):
        print("Esse personagem já tem um diário.")
        return
    diario = {"personagem": nome, "entradas": []}
    with open(caminho, "wb") as f:
        pickle.dump(diario, f)
    print(f"Diário criado para {nome}!")

def adicionar_entrada():
    nome = selecionar_personagem_com_ficha()
    if not nome:
        return
    caminho = os.path.join(PASTA_DIARIOS, f"{nome.lower()}_diario.pkl")
    if not os.path.exists(caminho):
        print("Esse personagem ainda não tem um diário.")
        return

    with open(caminho, "rb") as f:
        diario = pickle.load(f)

    print("\nTipos de entrada:")
    tipos = ["Encontro", "Batalha", "Lugares", "Descobertas", "Pensamentos"]
    for i, t in enumerate(tipos, 1):
        print(f"{i}. {t}")

    while True:
        tipo = input("Escolha o tipo de entrada: ").strip()
        if tipo.isdigit() and 1 <= int(tipo) <= len(tipos):
            tipo = tipos[int(tipo) - 1]
            break
        print("Escolha inválida.")

    titulo = input("Título da entrada (opcional): ").strip()
    data = input("Data da entrada (ex: 24/06/2025): ").strip()
    texto = input("Digite o conteúdo da entrada:\n").strip()

    entrada = {"tipo": tipo, "data": data, "titulo": titulo, "texto": texto}
    diario["entradas"].append(entrada)

    with open(caminho, "wb") as f:
        pickle.dump(diario, f)

    print("Entrada adicionada com sucesso!")

def gerar_pdf_diario():
    nome = selecionar_personagem_com_ficha()
    if not nome:
        return
    caminho = os.path.join(PASTA_DIARIOS, f"{nome.lower()}_diario.pkl")
    if not os.path.exists(caminho):
        print("Esse personagem não tem um diário ainda.")
        return

    with open(caminho, "rb") as f:
        diario = pickle.load(f)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Fundo bege estilo pergaminho
    pdf.set_fill_color(245, 240, 225)
    pdf.rect(0, 0, pdf.w, pdf.h, 'F')

    # Moldura simples
    pdf.set_draw_color(150, 130, 100)
    pdf.rect(5, 5, pdf.w - 10, pdf.h - 10)

    # Título principal (sem símbolos especiais)
    pdf.set_text_color(101, 67, 33)
    pdf.set_font("Times", "B", 20)
    pdf.cell(0, 15, "--- Diario de Aventura ---", ln=True, align="C")
    pdf.set_font("Times", "I", 14)
    pdf.cell(0, 10, f"Personagem: {diario['personagem']}", ln=True, align="C")
    pdf.ln(10)

    for entrada in diario["entradas"]:
        tipo = entrada['tipo'].upper()
        data = entrada['data']
        titulo = entrada.get('titulo', '').strip()
        cabecalho = f"* [{tipo}]"
        if titulo:
            cabecalho += f" {titulo} -"
        cabecalho += f" {data}"

        # Cabeçalho da entrada
        pdf.set_text_color(120, 60, 30)
        pdf.set_font("Times", "B", 13)
        pdf.multi_cell(0, 8, cabecalho)
        pdf.ln(2)

        # Corpo do texto
        pdf.set_text_color(40, 40, 40)
        pdf.set_font("Times", "", 12)
        texto_formatado = quebrar_palavras_longas(entrada["texto"])
        pdf.multi_cell(0, 8, texto_formatado)
        pdf.ln(5)

        # Linha de separação entre entradas
        pdf.set_draw_color(180, 160, 120)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), pdf.w - 10, pdf.get_y())
        pdf.ln(5)

    # Salvar PDF
    pasta_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdfs", "diarios_pdf"))
    os.makedirs(pasta_pdf, exist_ok=True)
    nome_pdf = f"diario_{nome.lower()}.pdf"
    caminho_pdf = os.path.join(pasta_pdf, nome_pdf)
    pdf.output(caminho_pdf)
    print(f"PDF gerado com sucesso: {caminho_pdf}")




def menu_diario():
    while True:
        print("\n=== Diário de Aventura ===")
        print("1. Criar novo diário para um personagem")
        print("2. Adicionar nova entrada")
        print("3. Gerar PDF/ Atualizar PDF do diário")
        print("0. Voltar")

        op = input("Escolha uma opção: ").strip()
        if op == "1":
            criar_diario()
        elif op == "2":
            adicionar_entrada()
        elif op == "3":
            gerar_pdf_diario()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

