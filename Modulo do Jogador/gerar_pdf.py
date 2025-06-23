from fpdf import FPDF

class PDFEstiloMedieval(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Times", size=12)

    def header(self):
        self.set_font("Times", "B", 20)
        self.set_text_color(80, 40, 20)
        self.cell(0, 12, "*** FICHA DO AVENTUREIRO ***", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 10)
        self.set_text_color(140, 100, 60)
        self.cell(0, 10, "-- Que os deuses o protejam nas trilhas do destino --", 0, 0, "C")

def gerar_pdf_sem_fundo(nome_arquivo, data_dict, inventario_dict=None):
    pdf = PDFEstiloMedieval()

    def titulo_secao(titulo):
        pdf.set_font("Times", "B", 16)
        pdf.set_text_color(100, 50, 20)
        pdf.cell(0, 10, f"-- {titulo.upper()} --", ln=True)
        pdf.set_draw_color(160, 120, 80)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)

    def escrever_linha(titulo, valor):
        pdf.set_font("Times", "B", 13)
        pdf.set_text_color(60, 30, 10)
        pdf.cell(50, 8, f"{titulo}:", ln=0)
        pdf.set_font("Times", "", 13)
        pdf.multi_cell(0, 8, str(valor))
        pdf.ln(1)

    # Informações Básicas
    titulo_secao("Informações Básicas")
    escrever_linha("Nome", data_dict.get("nome", ""))
    escrever_linha("Gênero", data_dict.get("gênero", ""))
    escrever_linha("Altura", data_dict.get("altura", ""))
    escrever_linha("Idade", data_dict.get("idade", ""))
    escrever_linha("Alinhamento", data_dict.get("alinhamento", ""))
    escrever_linha("Raça", data_dict.get("raça", ""))
    escrever_linha("Classe", data_dict.get("classe", ""))
    escrever_linha("Subclasse", data_dict.get("subclasses", ""))
    escrever_linha("Nível", data_dict.get("nível", ""))

    # Personalidade e história
    titulo_secao("Descrição e Personalidade")
    escrever_linha("Aparência", data_dict.get("aparência", ""))
    escrever_linha("Personalidade", data_dict.get("personalidade", ""))
    escrever_linha("História", data_dict.get("história", ""))

    # Atributos
    atributos = data_dict.get("atributos", {})
    if atributos:
        titulo_secao("Atributos")
        for chave in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            valor = atributos.get(chave, "-")
            escrever_linha(chave, valor)

    # Vida
    if "HP" in data_dict:
        titulo_secao("Pontos de Vida")
        escrever_linha("Vida", data_dict["HP"])

    # Idiomas e habilidades
    if "idiomas_proficiencias" in data_dict:
        titulo_secao("Idiomas e Proficiências")
        escrever_linha("Idiomas", data_dict["idiomas_proficiencias"])

    if "caracteristicas_habilidades" in data_dict:
        titulo_secao("Características e Habilidades")
        escrever_linha("Habilidades", data_dict["caracteristicas_habilidades"])

    # Inventário
    if inventario_dict and inventario_dict.get("itens"):
        titulo_secao("Inventário")
        pdf.set_font("Times", "I", 12)
        for item, info in inventario_dict["itens"].items():
            quantidade = info.get("quantidade", 0)
            pdf.multi_cell(0, 8, f"- {item} ({quantidade})")
        ouro = inventario_dict.get("Ouro", 0)
        pdf.ln(1)
        pdf.cell(0, 8, f"Ouro: {ouro}G", ln=True)
    else:
        pdf.set_font("Times", "I", 12)
        pdf.cell(0, 10, "Inventário vazio.", ln=True)

    # Equipamentos
    equipamentos = data_dict.get("equipamentos", [])
    if equipamentos:
        titulo_secao("Equipamentos")
        pdf.set_font("Times", "I", 12)
        for item in equipamentos:
            pdf.multi_cell(0, 8, f"- {item}")
        pdf.ln(2)

    pdf.output(nome_arquivo)
