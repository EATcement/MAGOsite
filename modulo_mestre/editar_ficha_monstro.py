import os
import pickle
from .gerar_pdf_monstro import gerar_pdf_monstro
from Modulo_criacao_de_fichas.Criacao_Fichas.Fichas_Monstros import (
    TIPOS_MONSTROS, TAMANHOS, ALINHAMENTOS, TIPOS_DANO,
    escolher_opcao_numerada, escolher_multiplas_opcoes
)

def editar_ficha_monstro():
    pasta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "monstros"))
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".pkl")]

    if not arquivos:
        print("Nenhuma ficha de monstro encontrada.")
        return

    print("\nFichas de monstro disponíveis:")
    for idx, nome in enumerate(arquivos, 1):
        print(f"{idx}. {nome.replace('.pkl', '')}")

    while True:
        escolha = input("Digite o número da ficha a editar: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(arquivos):
                nome_arquivo = arquivos[escolha - 1]
                break
        print("Opção inválida. Tente novamente.")

    caminho = os.path.join(pasta, nome_arquivo)
    with open(caminho, "rb") as arq:
        monstro = pickle.load(arq)

    print("\n--- Editando Ficha de Monstro ---")

    monstro["nome"] = input(f"Nome ({monstro['nome']}): ") or monstro["nome"]
    monstro["tipo"] = escolher_opcao_numerada("Tipo do monstro", TIPOS_MONSTROS)
    monstro["tamanho"] = escolher_opcao_numerada("Tamanho do monstro", TAMANHOS)
    monstro["alinhamento"] = escolher_opcao_numerada("Alinhamento", ALINHAMENTOS)
    monstro["CA"] = input(f"Classe de Armadura (CA) ({monstro['CA']}): ") or monstro["CA"]
    monstro["PV"] = input(f"Pontos de Vida (PV) ({monstro['PV']}): ") or monstro["PV"]
    monstro["deslocamento"] = input(f"Deslocamento ({monstro['deslocamento']}): ") or monstro["deslocamento"]
    monstro["nivel_desafio"] = input(f"Nível de desafio (ND) ({monstro['nivel_desafio']}): ") or monstro["nivel_desafio"]
    monstro["xp"] = input(f"XP ({monstro['xp']}): ") or monstro["xp"]

    print("\n--- Editar Atributos ---")
    for atributo in monstro["atributos"]:
        atual = monstro["atributos"][atributo]
        novo = input(f"{atributo} ({atual}): ")
        if novo.strip():
            monstro["atributos"][atributo] = novo

    monstro["vulnerabilidades"] = escolher_multiplas_opcoes("Vulnerabilidades", TIPOS_DANO)
    monstro["resistencias"] = escolher_multiplas_opcoes("Resistências", TIPOS_DANO)
    monstro["imunidades"] = escolher_multiplas_opcoes("Imunidades", TIPOS_DANO)

    habilidades = input("Habilidades especiais (separadas por vírgula): ")
    if habilidades.strip():
        monstro["habilidades"] = [h.strip() for h in habilidades.split(",") if h.strip()]

    ataques = input("Ataques (separados por vírgula): ")
    if ataques.strip():
        monstro["ataques"] = [a.strip() for a in ataques.split(",") if a.strip()]

    monstro["descricao"] = input(f"Descrição adicional ({monstro['descricao']}): ") or monstro["descricao"]

    
    with open(caminho, "wb") as arq:
        pickle.dump(monstro, arq)

    
    nome_pdf = nome_arquivo.replace(".pkl", ".pdf")
    pasta_saida = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdfs", "monstros_pdf"))
    os.makedirs(pasta_saida, exist_ok=True)
    caminho_pdf = os.path.join(pasta_saida, nome_pdf)

    gerar_pdf_monstro(caminho_pdf, monstro)
    print(f"\nFicha de monstro atualizada e PDF gerado em: {caminho_pdf}")

    
    novo_nome_base = monstro["nome"].lower().replace(" ", "_")
    novo_caminho = os.path.join(pasta, novo_nome_base + ".pkl")

    if novo_caminho != caminho:
        os.rename(caminho, novo_caminho)
        print(f"Arquivo renomeado para: {novo_nome_base}.pkl")
        caminho = novo_caminho

    
    with open(caminho, "wb") as arq:
        pickle.dump(monstro, arq)


if __name__ == "__main__":
    editar_ficha_monstro()
