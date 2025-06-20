from fpdf import FPDF

class PDFComVisual(FPDF):
    def __init__(self, imagem_fundo):
        super().__init__()
        self.imagem_fundo = imagem_fundo

    def header(self):
        # Coloca a imagem de fundo cobrindo toda a página
        self.image(self.imagem_fundo, x=0, y=0, w=self.w, h=self.h)


def gerar_pdf_com_visual(nome_arquivo, data_dict, imagem_fundo):
    pdf = PDFComVisual(imagem_fundo)
    pdf.add_page()

    # Exemplo de conteúdo no centro da ficha visual (ajuste as posições como quiser)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    
    campos_posicoes = {
        "nome": (50, 30),
        "idade": (50, 40),
        "habilidades": (50, 50),  # será convertido para string
    }

    for campo, posicao in campos_posicoes.items():
        valor = data_dict.get(campo, "")
        if isinstance(valor, list):
            valor = ", ".join(valor)  # transforma lista em string
        pdf.set_xy(*posicao)
        pdf.cell(0, 10, f"{valor}", ln=1)

    pdf.output(nome_arquivo)
    return nome_arquivo
if __name__ == "__main__":
    caminho_pdf = "C:/Users/Isabelle/Documents/GitHub/MAGOsite/Modulo do Jogador/ficha_integrada_visual.pdf"
    caminho_imagem_fundo = "C:/Users/Isabelle/Documents/GitHub/MAGOsite/Modulo do Jogador/Ficha Personagem 3.jpg"
    dados = {"nome": "Exemplo Teste"}

    gerar_pdf_com_visual(caminho_pdf, dados, caminho_imagem_fundo)
    print(f"PDF gerado em: {caminho_pdf}")
