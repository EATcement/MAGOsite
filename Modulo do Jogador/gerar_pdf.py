from fpdf import FPDF

class PDFComVisual(FPDF):
    def __init__(self, imagem_fundo):
        super().__init__()
        self.imagem_fundo = imagem_fundo

    def header(self):
        self.image(self.imagem_fundo, x=0, y=0, w=self.w, h=self.h)

def gerar_pdf_com_visual(nome_arquivo, data_dict, imagem_fundo):
    pdf = PDFComVisual(imagem_fundo)
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.set_text_color(0, 0, 0)

    campos_posicoes = {
        "nome": (165, 15),
        "classe": (96, 15),
        "raça": (120, 23),
        "nível": (185, 34),
        "idade": (50, 40),
        "personalidade": (165, 58),  # se quiser usar, adapte para "personalidade"
        "caracteristicas_habilidades": (165, 185),  # adapte para o que quer mostrar
        "proficiencias": (25, 265),  # adaptar para "proficiencias"
    }

    # Posição para os atributos dentro do subdicionário 'atributos'
    posicoes_atributos = {
        "Força": (22, 51),
        "Constituição": (22, 86),
        "Destreza": (22, 121),
        "Inteligência": (22, 156),
        "Sabedoria": (22, 191),
        "Carisma": (22, 226),
    }

    # Escrever campos principais
    for campo, posicao in campos_posicoes.items():
        valor = data_dict.get(campo, "")
        pdf.set_xy(*posicao)
        pdf.multi_cell(0, 5, str(valor))

    # Escrever atributos que estão dentro de data_dict["atributos"]
    atributos = data_dict.get("atributos", {})
    for attr, posicao in posicoes_atributos.items():
        valor = atributos.get(attr, "")
        pdf.set_xy(*posicao)
        pdf.multi_cell(0, 5, str(valor))

    pdf.output(nome_arquivo)

