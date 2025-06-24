import os
import pickle
from Modulo_criacao_de_fichas.Criacao_Fichas.Fichas_jogador import (
    PASTA, CLASSES, RACAS, ALINHAMENTOS, SUBCLASSES,
    escolher_opcao_numerada, escolher_subclasse, input_inteiro_positivo, calcular_vida
)
from Modulo_do_Jogador.gerar_pdf import gerar_pdf_sem_fundo

def editar_ficha_mestre():
    arquivos = [f for f in os.listdir(PASTA) if f.endswith(".pkl") and not f.endswith("_inventario.pkl")]
    if not arquivos:
        print("Nenhuma ficha encontrada.")
        return

    print("\nFichas disponíveis:")
    for idx, nome in enumerate(arquivos, 1):
        print(f"{idx}. {nome.replace('.pkl', '')}")

    while True:
        escolha = input("\nDigite o número da ficha que deseja editar: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(arquivos):
                nome_arquivo = arquivos[escolha - 1]
                break
        print("Opção inválida.")

    caminho = os.path.join(PASTA, nome_arquivo)
    with open(caminho, "rb") as arq:
        ficha = pickle.load(arq)

    print(f"\n--- Editando ficha: {ficha.get('nome', 'Desconhecido')} ---\n")

    # Editáveis de texto livre
    campos_texto = ["nome", "gênero", "altura", "idade", "aparência", "personalidade", "história"]
    for campo in campos_texto:
        atual = ficha.get(campo, "")
        novo = input(f"{campo.capitalize()} (atual: {atual}): ").strip()
        if novo:
            ficha[campo] = novo

    # Escolhas numeradas (alinhamento, raça, classe, subclasse)
    ficha["alinhamento"] = escolher_opcao_numerada("Alinhamento", ALINHAMENTOS)
    ficha["raça"] = escolher_opcao_numerada("Raça", RACAS)
    ficha["classe"] = escolher_opcao_numerada("Classe", CLASSES)
    ficha["subclasses"] = escolher_subclasse(ficha["classe"])

    # Nível
    ficha["nível"] = input_inteiro_positivo(f"Nível (atual: {ficha.get('nível', '1')}): ")

    # Editar atributos
    print("\n--- Editando Atributos ---")
    atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    novos_atributos = {}
    for atributo in atributos:
        atual = ficha["atributos"].get(atributo, 10)
        while True:
            novo = input(f"{atributo} (atual: {atual}, máx 20): ").strip()
            if not novo:
                novos_atributos[atributo] = atual
                break
            if novo.isdigit():
                novo = int(novo)
                if 1 <= novo <= 20:
                    novos_atributos[atributo] = novo
                    break
            print("Valor inválido. Digite número inteiro entre 1 e 20.")
    ficha["atributos"] = novos_atributos

    # Recalcular HP
    calcular_vida(ficha)

    # Renomear .pkl se o nome mudou
    novo_nome_base = ficha["nome"].lower().replace(" ", "_")
    novo_caminho = os.path.join(PASTA, novo_nome_base + ".pkl")

    if novo_caminho != caminho:
        os.rename(caminho, novo_caminho)
        print(f"Arquivo renomeado para: {novo_nome_base}.pkl")
        caminho = novo_caminho

    # Salvar .pkl
    with open(caminho, "wb") as arq:
        pickle.dump(ficha, arq)

    print("\nFicha salva com sucesso!")

    # Atualizar o PDF
    pasta_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdfs"))
    os.makedirs(pasta_pdf, exist_ok=True)
    nome_pdf = f"ficha_{novo_nome_base}.pdf"
    caminho_pdf = os.path.join(pasta_pdf, nome_pdf)
    gerar_pdf_sem_fundo(caminho_pdf, ficha)

    print(f"PDF atualizado: {caminho_pdf}")

if __name__ == "__main__":
    editar_ficha_mestre()
