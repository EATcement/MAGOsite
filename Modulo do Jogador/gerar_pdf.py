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
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)

    campos_posicoes = {
        "nome": (50, 30),
        "idade": (50, 40),
        "habilidades": (50, 50),
    }

    for campo, posicao in campos_posicoes.items():
        valor = data_dict.get(campo, "")
        if isinstance(valor, list):
            valor = ", ".join(valor)
        pdf.set_xy(*posicao)
        pdf.cell(0, 10, f"{valor}", ln=1)

    pdf.output(nome_arquivo)
