import pickle
import os

# Dicionários de opções
CLASSES = {
    "Guerreiro": "Bônus: +2 Força, +1 Constituição. Habilidade: Ataque Extra.",
    "Mago": "Bônus: +3 Inteligência. Habilidade: Magia Arcana.",
    "Ladino": "Bônus: +2 Destreza, +1 Carisma. Habilidade: Ataque Furtivo.",
    "Clérigo": "Bônus: +2 Sabedoria, +1 Constituição. Habilidade: Cura Divina.",
    "Bárbaro": "Bônus: +3 Força. Habilidade: Fúria.",
    "Bardo": "Bônus: +2 Carisma, +1 Destreza. Habilidade: Inspiração de Bardo.",
    "Bruxo": "Bônus: +2 Carisma. Habilidade: Magia de pacto.",
    "Druida": "Bônus: +2 Sabedoria. Habilidade: Forma Selvagem.",
    "Feiticeiro": "Bônus: +3 Carisma. Habilidade: Magia Inata.",
    "Monge": "Bônus: +2 Destreza, +1 Sabedoria. Habilidade: Artes Marciais.",
    "Paladino": "Bônus: +2 Carisma, +1 Força. Habilidade: Imposição das Mãos.",
    "Patrulheiro": "Bônus: +2 Destreza, +1 Sabedoria. Habilidade: Inimigo Favorito.",
}

RACAS = {
    "Humano": "Bônus: +1 em todos os atributos.",
    "Anão": "Bônus: +2 Constituição. Habilidade: Resistência a veneno.",
    "Anão da Colina": "Bônus: +2 Constituição, +1 Sabedoria. Habilidade: Resiliência Anã.",
    "Anão da Montanha": "Bônus: +2 Constituição, +2 Força. Habilidade: Treinamento Anão.",
    "Elfo": "Bônus: +2 Destreza. Habilidade: Visão no Escuro.",
    "Elfo da Floresta": "Bônus: +2 Destreza, +1 Sabedoria. Habilidade: Pé-Leve.",
    "Alto Elfo": "Bônus: +2 Destreza, +1 Inteligência. Habilidade: Treinamento Élfico.",
    "Drow": "Bônus: +2 Destreza, +1 Carisma. Habilidade: Magia Drow.",
    "Halfling": "Bônus: +2 Destreza. Habilidade: Sorte Halfling.",
    "Halfling Pés-Leves": "Bônus: +2 Destreza, +1 Carisma. Habilidade: Naturalmente Furtivo.",
    "Halfling Robusto": "Bônus: +2 Destreza, +1 Constituição. Habilidade: Resiliência Halfling.",
    "Gnomo": "Bônus: +2 Inteligência. Habilidade: Engenhocas.",
    "Gnomo das Rochas": "Bônus: +2 Inteligência, +1 Constituição. Habilidade: Conhecimento Mecânico.",
    "Gnomo da Floresta": "Bônus: +2 Inteligência, +1 Destreza. Habilidade: Falar com Animais.",
    "Meio-Elfo": "Bônus: +2 Carisma, +1 em duas outras habilidades. Habilidade: Versatilidade Élfica.",
    "Meio-Orc": "Bônus: +2 Força, +1 Constituição. Habilidade: Resistência Implacável.",
    "Draconato": "Bônus: +2 Força, +1 Carisma. Habilidade: Sopro de Dragão.",
    "Tiefling": "Bônus: +2 Carisma, +1 Inteligência. Habilidade: Magia Infernal.",
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

PASTA = "fichas"
os.makedirs(PASTA, exist_ok=True)

# Função interativa para raça/classe - corrigida para aceitar variações de maiúsculas/minúsculas
def escolher_interativo(titulo, opcoes):
    while True:
        print(f"\n{titulo} disponíveis:")
        for nome in opcoes:
            print(f"- {nome}")
        entrada = input("Digite o nome para ver detalhes, ou 'escolher [nome]' para selecionar: ").strip()
        
        if entrada.lower().startswith("escolher "):
            escolha_raw = entrada[9:].strip()
            escolha = None
            for chave in opcoes:
                if chave.lower() == escolha_raw.lower():
                    escolha = chave
                    break
            if escolha:
                print(f"\nVocê escolheu: {escolha}")
                return escolha
            else:
                print("Opção inválida.")
        else:
            busca = None
            for chave in opcoes:
                if chave.lower() == entrada.lower():
                    busca = chave
                    break
            if busca:
                print(f"{busca}: {opcoes[busca]}")
            else:
                print("Entrada inválida.")

# Subclasse baseada na classe (mantida, mas ajustando também para case insensitive)
def escolher_subclasse(classe):
    subclasses = SUBCLASSES.get(classe, [])
    if not subclasses:
        return "Nenhuma"
    while True:
        print(f"\nSubclasses para {classe}:")
        for s in subclasses:
            print(f"- {s}")
        entrada = input("Digite 'escolher [nome]' para selecionar: ").strip()
        if entrada.lower().startswith("escolher "):
            escolha_raw = entrada[9:].strip()
            escolha = None
            for s in subclasses:
                if s.lower() == escolha_raw.lower():
                    escolha = s
                    break
            if escolha:
                return escolha
            else:
                print("Subclasse inválida.")
        else:
            print("Entrada inválida.")

# Criar ficha (dicionário)
def criar_ficha():
    ficha = {}
    ficha["nome"] = input("Nome: ")
    ficha["gênero"] = input("Gênero: ")
    ficha["altura"] = input("Altura: ")
    ficha["alinhamento"] = input("Alinhamento: ")
    ficha["idade"] = input("Idade: ")
    ficha["aparência"] = input("Aparência: ")
    ficha["personalidade"] = input("Personalidade: ")
    ficha["história"] = input("História: ")
    ficha["raça"] = escolher_interativo("Raças", RACAS)
    ficha["classe"] = escolher_interativo("Classes", CLASSES)
    ficha["subclasses"] = escolher_subclasse(ficha["classe"])
    ficha["nível"] = input("Nível: ")
    print("\n--- Atributos ---")
    ficha["atributos"] = {
        "Força": input("FOR: "),
        "Destreza": input("DES: "),
        "Constituição": input("CON: "),
        "Inteligência": input("INT: "),
        "Sabedoria": input("SAB: "),
        "Carisma": input("CAR: "),
    }
    ficha["pontos_habilidade"] = input("Pontos de habilidade: ")
    ficha["proficiencias"] = input("Proficiências: ")
    return ficha

# Mostrar ficha
def exibir_ficha(ficha):
    print("\n--- FICHA DO PERSONAGEM ---")
    for campo, valor in ficha.items():
        print(f"{campo.capitalize()}: {valor}")

# Salvar com pickle
def salvar_ficha(ficha):
    nome_arquivo = ficha['nome'].lower().replace(" ", "_") + ".pkl"
    caminho = os.path.join(PASTA, nome_arquivo)
    with open(caminho, "wb") as arq:
        pickle.dump(ficha, arq)
    print(f"Ficha salva como: {caminho}")

# Carregar com pickle
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

# Menu principal
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
