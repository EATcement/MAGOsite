import pickle
import os

PASTA_MONSTROS = "monstros"
os.makedirs(PASTA_MONSTROS, exist_ok=True)

def criar_ficha_monstro():
    monstro = {}
    monstro["nome"] = input("Nome do monstro: ")
    monstro["tipo"] = input("Tipo (ex: aberração, besta, morto-vivo...): ")
    monstro["tamanho"] = input("Tamanho (ex: Pequeno, Médio, Grande): ")
    monstro["alinhamento"] = input("Alinhamento (ex: Leal Mau, Caótico Bom): ")
    monstro["CA"] = input("Classe de Armadura (CA): ")
    monstro["PV"] = input("Pontos de Vida (PV): ")
    monstro["deslocamento"] = input("Deslocamento (ex: 9m): ")

    print("\n--- Atributos ---")
    monstro["atributos"] = {
        "Força": input("FOR: "),
        "Destreza": input("DES: "),
        "Constituição": input("CON: "),
        "Inteligência": input("INT: "),
        "Sabedoria": input("SAB: "),
        "Carisma": input("CAR: ")
    }

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
            print(f"{campo.capitalize()}: {', '.join(valor)}")
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
        print("\nMenu - Fichas de Monstros:")
        print("1. Criar ficha de monstro")
        print("2. Carregar ficha de monstro")
        print("3. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            monstro = criar_ficha_monstro()
            exibir_ficha_monstro(monstro)
            salvar_ficha_monstro(monstro)
        elif op == "2":
            carregar_ficha_monstro()
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
