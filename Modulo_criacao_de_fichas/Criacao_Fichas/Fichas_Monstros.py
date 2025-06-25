import pickle
import os


PASTA_MONSTROS = "monstros"
os.makedirs(PASTA_MONSTROS, exist_ok=True)

TIPOS_MONSTROS = [
    "Aberração", "Besta", "Construto", "Dragão", "Elemental",
    "Fada", "Gigante", "Humanoide", "Monstro", "Mortos-Vivos"
]

TAMANHOS = [
    "Minúsculo", "Muito Pequeno", "Pequeno", "Médio",
    "Grande", "Enorme", "Colossal"
]

ALINHAMENTOS = [
    "Leal e Bom", "Neutro e Bom", "Caótico e Bom",
    "Leal e Neutro", "Neutro", "Caótico e Neutro",
    "Leal e Mau", "Neutro e Mau", "Caótico e Mau"
]

TIPOS_DANO = [
    "Cortante", "Perfurante", "Contundente", "Fogo",
    "Gelo", "Raio", "Ácido", "Veneno", "Psíquico", "Sônico"
]

def escolher_opcao_numerada(titulo, opcoes):
    print(f"\n{titulo}:")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    while True:
        escolha = input("Digite o número da opção desejada: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return opcoes[int(escolha) - 1]
        print("Opção inválida. Tente novamente.")
        
def input_texto_obrigatorio(label):
    while True:
        texto = input(label).strip()
        if texto:
            return texto
        print("Este campo não pode estar vazio.")

def escolher_multiplas_opcoes(titulo, opcoes):
    print(f"\n{titulo} (digite números separados por vírgula, ou deixe vazio para nenhuma):")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    escolha = input("Sua escolha: ")
    if not escolha.strip():
        return []
    selecionados = []
    for num in escolha.split(","):
        num = num.strip()
        if num.isdigit() and 1 <= int(num) <= len(opcoes):
            selecionados.append(opcoes[int(num)-1])
        else:
            print(f"Opção inválida ignorada: {num}")
    return selecionados

def criar_ficha_monstro():
    monstro = {}
    monstro["nome"] = input_texto_obrigatorio("Nome do monstro: ")
    monstro["tipo"] = escolher_opcao_numerada("Tipo do monstro", TIPOS_MONSTROS)
    monstro["tamanho"] = escolher_opcao_numerada("Tamanho do monstro", TAMANHOS)
    monstro["alinhamento"] = escolher_opcao_numerada("Alinhamento", ALINHAMENTOS)
    monstro["CA"] = input("Classe de Armadura (CA): ")
    monstro["PV"] = input("Pontos de Vida (PV): ")
    monstro["deslocamento"] = input("Deslocamento (ex: 9m): ")
    
    monstro["nivel_desafio"] = input("Nível de desafio (ND): ")
    monstro["xp"] = input("XP concedida quando derrotado: ")
    
    print("\n--- Atributos ---")
    monstro["atributos"] = {
        "Força": input("FOR: "),
        "Destreza": input("DES: "),
        "Constituição": input("CON: "),
        "Inteligência": input("INT: "),
        "Sabedoria": input("SAB: "),
        "Carisma": input("CAR: ")
    }

    monstro["vulnerabilidades"] = escolher_multiplas_opcoes("Vulnerabilidades", TIPOS_DANO)
    monstro["resistencias"] = escolher_multiplas_opcoes("Resistências", TIPOS_DANO)
    monstro["imunidades"] = escolher_multiplas_opcoes("Imunidades", TIPOS_DANO)
    monstro["habilidades"] = input("Habilidades especiais (separadas por vírgula): ").split(",")
    monstro["ataques"] = input("Ataques (separados por vírgula): ").split(",")
    monstro["descricao"] = input("Descrição adicional (história, poderes, etc): ")
    
    return monstro

def exibir_ficha_monstro(monstro):
    print("\n--- FICHA DO MONSTRO ---")
    for campo, valor in monstro.items():
        if campo == "atributos":
            print("Atributos:")
            for attr, val in valor.items():
                print(f"  {attr}: {val}")
        elif isinstance(valor, list):
            lista_formatada = ", ".join([v.strip() for v in valor]) if valor else "Nenhuma"
            print(f"{campo.capitalize()}: {lista_formatada}")
        else:
            print(f"{campo.capitalize()}: {valor}")

def salvar_ficha_monstro(monstro):
    nome_arquivo = monstro['nome'].lower().replace(" ", "_") + ".pkl"
    caminho = os.path.join(PASTA_MONSTROS, nome_arquivo)
    with open(caminho, "wb") as arq:
        pickle.dump(monstro, arq)
    print(f"Ficha do monstro salva como: {caminho}")

def carregar_ficha_monstro():
    arquivos = [f for f in os.listdir(PASTA_MONSTROS) if f.endswith(".pkl")]
    if not arquivos:
        print("Nenhum monstro salvo encontrado.")
        return
    print("\nMonstros disponíveis:")
    for a in arquivos:
        print("- " + a.replace(".pkl", ""))
    nome = input("Digite o nome do arquivo (sem .pkl): ").lower().replace(" ", "_") + ".pkl"
    caminho = os.path.join(PASTA_MONSTROS, nome)
    if os.path.exists(caminho):
        with open(caminho, "rb") as arq:
            monstro = pickle.load(arq)
            print("\nFicha do monstro carregada com sucesso!")
            exibir_ficha_monstro(monstro)
    else:
        print("Arquivo não encontrado.")

def main():
    while True:
        print("\n===== MENU DE FICHA MONSTRO =====:")
        print("1. Criar ficha de monstro")
        print("2. Carregar ficha de monstro")
        print("0. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            monstro = criar_ficha_monstro()
            exibir_ficha_monstro(monstro)
            salvar_ficha_monstro(monstro)
        elif op == "2":
            carregar_ficha_monstro()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
