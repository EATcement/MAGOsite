from fpdf import FPDF
import os

class PDFEstiloMonstro(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Times", size=12)

    def header(self):
        self.set_font("Times", "B", 20)
        self.set_text_color(150, 0, 0)  # Tom de vermelho
        self.cell(0, 12, "*** FICHA DE MONSTRO ***", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 10)
        self.set_text_color(200, 50, 50)
        self.cell(0, 10, "-- Que os deuses o protejam nas trilhas do destino --", 0, 0, "C")

def gerar_pdf_monstro(nome_arquivo, monstro):
    pdf = PDFEstiloMonstro()

    def titulo_secao(titulo):
        pdf.set_font("Times", "B", 16)
        pdf.set_text_color(180, 0, 0)
        pdf.cell(0, 10, f"-- {titulo.upper()} --", ln=True)
        pdf.set_draw_color(200, 0, 0)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)

    def escrever_linha(titulo, valor):
        pdf.set_font("Times", "B", 13)
        pdf.set_text_color(120, 0, 0)
        pdf.cell(50, 8, f"{titulo}:", ln=0)

        pdf.set_font("Times", "", 13)
        texto = str(valor) if valor else "-"
        y_atual = pdf.get_y()
        x_texto = pdf.l_margin + 50
        pdf.set_xy(x_texto, y_atual)
        largura_disponivel = pdf.w - x_texto - pdf.r_margin
        if largura_disponivel <= 0:
            largura_disponivel = pdf.w - pdf.l_margin - pdf.r_margin
        pdf.multi_cell(largura_disponivel, 8, texto)
        pdf.ln(1)

    # Informações Básicas
    titulo_secao("Informações Básicas")
    escrever_linha("Nome", monstro.get("nome", ""))
    escrever_linha("Tipo", monstro.get("tipo", ""))
    escrever_linha("Tamanho", monstro.get("tamanho", ""))
    escrever_linha("Alinhamento", monstro.get("alinhamento", ""))
    escrever_linha("Classe de Armadura", monstro.get("CA", ""))
    escrever_linha("Pontos de Vida", monstro.get("PV", ""))
    escrever_linha("Deslocamento", monstro.get("deslocamento", ""))
    escrever_linha("Nível de Desafio", monstro.get("nivel_desafio", ""))
    escrever_linha("XP", monstro.get("xp", ""))

    # Atributos
    atributos = monstro.get("atributos", {})
    if atributos:
        titulo_secao("Atributos")
        for chave in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            valor = atributos.get(chave, "-")
            escrever_linha(chave, valor)

    # Vulnerabilidades, Resistências e Imunidades
    titulo_secao("Vulnerabilidades / Resistências / Imunidades")
    escrever_linha("Vulnerabilidades", ", ".join(monstro.get("vulnerabilidades", []) or ["Nenhuma"]))
    escrever_linha("Resistências", ", ".join(monstro.get("resistencias", []) or ["Nenhuma"]))
    escrever_linha("Imunidades", ", ".join(monstro.get("imunidades", []) or ["Nenhuma"]))

    # Habilidades Especiais
    titulo_secao("Habilidades Especiais")
    escrever_linha("Habilidades", ", ".join(monstro.get("habilidades", []) or ["Nenhuma"]))

    # Ataques
    titulo_secao("Ataques")
    escrever_linha("Ataques", ", ".join(monstro.get("ataques", []) or ["Nenhum"]))

    # Descrição
    titulo_secao("Descrição")
    escrever_linha("Descrição", monstro.get("descricao", "Sem descrição."))

    # Criar diretório se não existir
    pasta_saida = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdfs", "monstros_pdf"))
    os.makedirs(pasta_saida, exist_ok=True)

    caminho_pdf = os.path.join(pasta_saida, f"{monstro['nome'].lower().replace(' ', '_')}.pdf")
    pdf.output(caminho_pdf)
    print(f"PDF salvo em: {caminho_pdf}")