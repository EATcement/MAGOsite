import pickle
import os

def obter_caminho_fichas():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "fichas")
    )

PASTA = obter_caminho_fichas()
os.makedirs(PASTA, exist_ok=True)

CLASSES = {
    "Guerreiro": {
        "bonus": {"Força": 2, "Constituição": 1},
        "habilidade": "Ataque Extra"
    },
    "Mago": {
        "bonus": {"Inteligência": 3},
        "habilidade": "Magia Arcana"
    },
    "Ladino": {
        "bonus": {"Destreza": 2, "Carisma": 1},
        "habilidade": "Ataque Furtivo"
    },
    "Clérigo": {
        "bonus": {"Sabedoria": 2, "Constituição": 1},
        "habilidade": "Cura Divina"
    },
    "Bárbaro": {
        "bonus": {"Força": 3},
        "habilidade": "Fúria"
    },
    "Bardo": {
        "bonus": {"Carisma": 2, "Destreza": 1},
        "habilidade": "Inspiração de Bardo"
    },
    "Bruxo": {
        "bonus": {"Carisma": 2},
        "habilidade": "Magia de pacto"
    },
    "Druida": {
        "bonus": {"Sabedoria": 2},
        "habilidade": "Forma Selvagem"
    },
    "Feiticeiro": {
        "bonus": {"Carisma": 3},
        "habilidade": "Magia Inata"
    },
    "Monge": {
        "bonus": {"Destreza": 2, "Sabedoria": 1},
        "habilidade": "Artes Marciais"
    },
    "Paladino": {
        "bonus": {"Carisma": 2, "Força": 1},
        "habilidade": "Imposição das Mãos"
    },
    "Patrulheiro": {
        "bonus": {"Destreza": 2, "Sabedoria": 1},
        "habilidade": "Inimigo Favorito"
    }
}

RACAS = {
    "Humano": {
        "bonus": {"Força": 1, "Destreza": 1, "Constituição": 1, "Inteligência": 1, "Sabedoria": 1, "Carisma": 1},
        "habilidade": "Versatilidade Humana"
    },
    "Anão": {
        "bonus": {"Constituição": 2},
        "habilidade": "Resistência a veneno"
    },
    "Anão da Colina": {
        "bonus": {"Constituição": 2, "Sabedoria": 1},
        "habilidade": "Resiliência Anã"
    },
    "Anão da Montanha": {
        "bonus": {"Constituição": 2, "Força": 2},
        "habilidade": "Treinamento Anão"
    },
    "Elfo": {
        "bonus": {"Destreza": 2},
        "habilidade": "Visão no Escuro"
    },
    "Elfo da Floresta": {
        "bonus": {"Destreza": 2, "Sabedoria": 1},
        "habilidade": "Pé-Leve"
    },
    "Alto Elfo": {
        "bonus": {"Destreza": 2, "Inteligência": 1},
        "habilidade": "Treinamento Élfico"
    },
    "Drow": {
        "bonus": {"Destreza": 2, "Carisma": 1},
        "habilidade": "Magia Drow"
    },
    "Halfling": {
        "bonus": {"Destreza": 2},
        "habilidade": "Sorte Halfling"
    },
    "Halfling Pés-Leves": {
        "bonus": {"Destreza": 2, "Carisma": 1},
        "habilidade": "Naturalmente Furtivo"
    },
    "Halfling Robusto": {
        "bonus": {"Destreza": 2, "Constituição": 1},
        "habilidade": "Resiliência Halfling"
    },
    "Gnomo": {
        "bonus": {"Inteligência": 2},
        "habilidade": "Engenhocas"
    },
    "Gnomo das Rochas": {
        "bonus": {"Inteligência": 2, "Constituição": 1},
        "habilidade": "Conhecimento Mecânico"
    },
    "Gnomo da Floresta": {
        "bonus": {"Inteligência": 2, "Destreza": 1},
        "habilidade": "Falar com Animais"
    },
    "Meio-Elfo": {
        "bonus": {"Carisma": 2},
        "habilidade": "Versatilidade Élfica"
    },
    "Meio-Orc": {
        "bonus": {"Força": 2, "Constituição": 1},
        "habilidade": "Resistência Implacável"
    },
    "Draconato": {
        "bonus": {"Força": 2, "Carisma": 1},
        "habilidade": "Sopro de Dragão"
    },
    "Tiefling": {
        "bonus": {"Carisma": 2, "Inteligência": 1},
        "habilidade": "Magia Infernal"
    }
}




SUBCLASSES = {
    "Guerreiro": ["Campeão", "Mestre de Batalha", "Cavaleiro Arcano"],
    "Mago": ["Evocador", "Ilusionista", "Necromante"],
    "Ladino": ["Assassino", "Trapaceiro Arcano", "Espião"],
    "Clérigo": ["Domínio da Vida", "Domínio da Guerra", "Domínio da Luz"],
    "Bárbaro": ["Caminho do Berserker", "Caminho do Totem"],
    "Bardo": ["Colégio do Conhecimento", "Colégio da Bravura"],
    "Bruxo": ["Pacto com o Diabo", "Pacto com a Fada", "Pacto com o Grande Antigo"],
    "Druida": ["Círculo da Terra", "Círculo da Lua"],
    "Feiticeiro": ["Linhagem Dracônica", "Magia Selvagem"],
    "Monge": ["Caminho das Mãos", "Caminho da Sombra", "Caminho dos Quatro Elementos"],
    "Paladino": ["Juramento de Devoção", "Juramento da Vingança", "Juramento dos Anciões"],
    "Patrulheiro": ["Caçador", "Mestre das Feras"]
}

ALINHAMENTOS = [
    "Ordeiro e Bom", "Neutro e Bom", "Caótico e Bom",
    "Ordeiro e Neutro", "Neutro", "Caótico e Neutro",
    "Ordeiro e Mau", "Neutro e Mau", "Caótico e Mau"
]

def escolher_opcao_numerada(titulo, opcoes):
    print(f"\n{titulo}:")

    if isinstance(opcoes, dict):
        nomes = list(opcoes.keys())
        for idx, nome in enumerate(nomes, 1):
            bonus = opcoes[nome].get("bonus", {})
            habilidade = opcoes[nome].get("habilidade", "—")
            bonus_str = ", ".join([f"+{v} {k}" for k, v in bonus.items()]) if bonus else "Sem bônus"
            print(f"{idx}. {nome} → Bônus: {bonus_str} | Habilidade: {habilidade}")
    elif isinstance(opcoes, list):
        nomes = opcoes
        for idx, item in enumerate(nomes, 1):
            print(f"{idx}. {item}")
    else:
        print("Formato de opções inválido.")
        return None
    while True:
        escolha = input("Digite o número da opção desejada: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(nomes):
                return nomes[escolha - 1]
        print("Opção inválida. Tente novamente.")


def escolher_subclasse(classe):
    subclasses = SUBCLASSES.get(classe, [])
    if not subclasses:
        return "Nenhuma"
    return escolher_opcao_numerada(f"Subclasses para {classe}", subclasses)

def input_inteiro_positivo(label):
    while True:
        valor = input(label)
        if valor.isdigit() and 1 <= (valor := int(valor)) <= 20:
            return valor
        print("Valor inválido. Digite apenas números inteiros positivos e menores que 20.")

def calcular_vida(ficha):
    raças_bonus = {
        "anão": 2,
        "anão da colina": 2,
        "anão da montanha": 2,
        "halfling robusto": 1,
        "gnomo das rochas": 1,
        "meio-orc": 1,
        "humano": 1,
    }
    classe_bonus = {
        "guerreiro": 1,
        "clérigo": 1,
    }

    raca = ficha["raça"].strip().lower()
    classe = ficha["classe"].strip().lower()
    con = int(ficha["atributos"]["Constituição"])
    lvl = int(ficha["nível"])
    hp = raças_bonus.get(raca, 0) + classe_bonus.get(classe, 0)  + con + lvl * 7
    ficha["HP"] = hp


def criar_ficha():
    ficha = {}
    ficha["nome"] = input("Nome: ")
    ficha["gênero"] = input("Gênero: ")
    ficha["altura"] = input("Altura: ")
    ficha["alinhamento"] = escolher_opcao_numerada("Alinhamentos", ALINHAMENTOS)
    ficha["idade"] = input("Idade: ")
    ficha["aparência"] = input("Aparência: ")
    ficha["personalidade"] = input("Personalidade: ")
    ficha["história"] = input("História: ")
    ficha["raça"] = escolher_opcao_numerada("Raças", RACAS)
    ficha["classe"] = escolher_opcao_numerada("Classes", CLASSES)
    ficha["subclasses"] = escolher_subclasse(ficha["classe"])
    ficha["nível"] = input_inteiro_positivo("Nível: ")

    print("\n--- Atributos ---")

    atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    atributos_finais = {}

    for atributo in atributos:
        bonus_classe = CLASSES.get(ficha["classe"], {}).get("bonus", {}).get(atributo, 0)
        bonus_raca = RACAS.get(ficha["raça"], {}).get("bonus", {}).get(atributo, 0)
        total_bonus = bonus_classe + bonus_raca

        while True:
            base = input_inteiro_positivo(f"{atributo.upper()} (+{total_bonus}): ")
            total = base + total_bonus
            if total > 20:
                print(f"Valor total com bônus ultrapassa 20 ({total}). Tente um valor menor.")
            else:
                atributos_finais[atributo] = total
                break

    ficha["atributos"] = atributos_finais
    calcular_vida(ficha)
    return ficha



def exibir_ficha(ficha):
    print("\n--- FICHA DO PERSONAGEM ---")
    for campo, valor in ficha.items():
        print(f"{campo.capitalize()}: {valor}")

def salvar_ficha(ficha):
    nome_arquivo = ficha['nome'].lower().replace(" ", "_") + ".pkl"
    caminho = os.path.join(PASTA, nome_arquivo)
    with open(caminho, "wb") as arq:
        pickle.dump(ficha, arq)
    print(f"Ficha salva como: {caminho}")

def carregar_ficha():
    arquivos = [f for f in os.listdir(PASTA) if f.endswith(".pkl")]
    if not arquivos:
        print("Nenhuma ficha salva encontrada.")
        return
    print("\nFichas disponíveis:")
    for a in arquivos:
        print("- " + a.replace(".pkl", ""))
    nome = input("Digite o nome do arquivo (sem .pkl): ").lower().replace(" ", "_") + ".pkl"
    caminho = os.path.join(PASTA, nome)
    if os.path.exists(caminho):
        with open(caminho, "rb") as arq:
            ficha = pickle.load(arq)
            print("\nFicha carregada com sucesso!")
            exibir_ficha(ficha)
    else:
        print("Arquivo não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Criar ficha")
        print("2. Carregar ficha")
        print("3. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            ficha = criar_ficha()
            exibir_ficha(ficha)
            salvar_ficha(ficha)
        elif op == "2":
            carregar_ficha()
        elif op == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
