import pickle
import os

inventario = {
    "itens": {},
    "Ouro": 0,
    "kit_aplicado": False
}

ficha = None  # Guarda a ficha do personagem atualmente selecionada

def definir_ficha(f):
    global ficha
    ficha = f

def obter_caminho_fichas():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "Modulo_criacao_de_fichas", "Criacao_Fichas", "fichas")
    )

def carregar_ficha_personagem(nome_personagem):
    base_dir = obter_caminho_fichas()
    nome_arquivo = nome_personagem.lower().replace(" ", "_") + ".pkl"
    caminho_completo = os.path.join(base_dir, nome_arquivo)

    if not os.path.exists(caminho_completo):
        print(f"Ficha '{nome_personagem}' não encontrada.")
        return None

    with open(caminho_completo, "rb") as arquivo:
        return pickle.load(arquivo)

def carregar_inventario(nome_ficha):
    nome_base = nome_ficha.lower().replace(" ", "_")
    caminho_fichas = obter_caminho_fichas()
    nome_arquivo = os.path.join(caminho_fichas, f"{nome_base}_inventario.pkl")

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "rb") as arq:
            return pickle.load(arq)
    else:
        print("Inventário salvo não encontrado. Usando inventário vazio.")
        return {
            "itens": {},
            "Ouro": 0,
            "kit_aplicado": False
        }

def salvar_inventario(nome_ficha):
    nome_base = nome_ficha.lower().replace(" ", "_")
    caminho_fichas = obter_caminho_fichas()
    nome_arquivo = os.path.join(caminho_fichas, f"{nome_base}_inventario.pkl")

    with open(nome_arquivo, "wb") as arq:
        pickle.dump(inventario, arq)
    print(f"Inventário salvo em: {nome_arquivo}")

def calcular_capacidade_peso(ficha):
    racas_peso = {
        "anão da colina": 10, "anão da montanha": 15,
        "alto elfo": 0, "elfo da floresta": 0, "drow": 0,
        "halfling pés-leves": 0, "halfling robusto": 0,
        "humano": 5, "draconato": 15,
        "gnomo da floresta": 0, "gnomo das rochas": 0,
        "meio-elfo": 0, "meio-orc": 15, "tiefling": 0,
        "anão": 15, "elfo": 0, "halfling": 0, "gnomo": 0
    }

    raca = ficha.get("raça") or ficha.get("raca")
    if raca:
        raca = raca.strip().lower()
    else:
        print("⚠️ Raça não encontrada na ficha. A capacidade de carga será zero.")
        return 0

    try:
        forca = int(ficha["atributos"]["Força"])
    except (KeyError, ValueError, TypeError):
        print("⚠️ Atributo de Força inválido ou ausente. Usando Força 0.")
        forca = 0

    return racas_peso.get(raca, 0) + 15 * forca

def calc_peso_itens():
    peso_total = 0
    for item, info in inventario["itens"].items():
        quantos = info["quantidade"]
        kilos = info["peso"]
        peso_total += quantos * kilos
    return peso_total

def add_kit(ficha):
    classe = ficha.get("classe", "").strip().lower()
    if inventario["kit_aplicado"]:
        print("Kit já aplicado anteriormente.")
        return

    kit_classes = {
        "guerreiro": {
            "espada longa": {"quantidade": 1, "peso": 3.0},
            "escudo": {"quantidade": 1, "peso": 6.0},
            "armadura de couro": {"quantidade": 1, "peso": 8.0},
            "rations": {"quantidade": 3, "peso": 0.5}
        },
        "mago": {
            "grimório": {"quantidade": 1, "peso": 2.0},
            "bastão arcano": {"quantidade": 1, "peso": 3.0},
            "poção de mana": {"quantidade": 2, "peso": 0.5},
            "túnica encantada": {"quantidade": 1, "peso": 1.5}
        },
        "ladino": {
            "adaga": {"quantidade": 2, "peso": 0.5},
            "capa de sombras": {"quantidade": 1, "peso": 1.0},
            "ganzuás": {"quantidade": 1, "peso": 0.2},
            "poção de invisibilidade": {"quantidade": 1, "peso": 0.3}
        },
        "clérigo": {
            "símbolo sagrado": {"quantidade": 1, "peso": 0.5},
            "mace": {"quantidade": 1, "peso": 4.0},
            "kit de cura": {"quantidade": 2, "peso": 1.0},
            "armadura leve": {"quantidade": 1, "peso": 6.0}
        },
        "bárbaro": {
            "machado de batalha": {"quantidade": 1, "peso": 5.5},
            "machadinha": {"quantidade": 2, "peso": 1.0},
            "lança": {"quantidade": 4, "peso": 1.3}
        },
        "bardo": {
            "alaúde": {"quantidade": 1, "peso": 1.0},
            "poção de cura": {"quantidade": 1, "peso": 0.5},
            "roupas elegantes": {"quantidade": 1, "peso": 2.0}
        },
        "bruxo": {
            "livro do pacto": {"quantidade": 1, "peso": 1.0},
            "arma de pacto": {"quantidade": 1, "peso": 1.5},
            "amuleto arcano": {"quantidade": 1, "peso": 0.2},
            "poção de mana": {"quantidade": 1, "peso": 0.5}
        },
        "druida": {
            "cajado natural": {"quantidade": 1, "peso": 3.0},
            "erva de cura": {"quantidade": 3, "peso": 0.3},
            "capa camuflada": {"quantidade": 1, "peso": 1.0}
        },
        "feiticeiro": {
            "anel arcano": {"quantidade": 1, "peso": 0.1},
            "poção de mana": {"quantidade": 2, "peso": 0.5},
            "roupa cerimonial": {"quantidade": 1, "peso": 1.5}
        },
        "monge": {
            "bastão": {"quantidade": 1, "peso": 2.0},
            "faixas de combate": {"quantidade": 1, "peso": 0.5},
            "medalhão do templo": {"quantidade": 1, "peso": 0.2}
        },
        "paladino": {
            "espada longa": {"quantidade": 1, "peso": 3.0},
            "símbolo sagrado": {"quantidade": 1, "peso": 0.5},
            "poção de cura": {"quantidade": 2, "peso": 0.5},
            "armadura pesada": {"quantidade": 1, "peso": 10.0}
        },
        "patrulheiro": {
            "arco longo": {"quantidade": 1, "peso": 2.0},
            "aljava com flechas": {"quantidade": 20, "peso": 0.1},
            "capa de floresta": {"quantidade": 1, "peso": 1.0}
        }
    }

    if classe not in kit_classes:
        print(f"Classe '{classe}' não tem um kit cadastrado.")
        print("As classes disponíveis atualmente são:")
        for k in sorted(kit_classes.keys()):
            print(f" - {k.capitalize()}")
        return

    kit = kit_classes[classe]

    for nome, dados in kit.items():
        quantidade = dados["quantidade"]
        peso = dados["peso"]

        if nome in inventario["itens"]:
            peso_existente = inventario["itens"][nome]["peso"]
            if peso_existente == peso:
                inventario["itens"][nome]["quantidade"] += quantidade
            else:
                nome_var = f"{nome} (variação)"
                inventario["itens"][nome_var] = {"quantidade": quantidade, "peso": peso}
        else:
            inventario["itens"][nome] = {"quantidade": quantidade, "peso": peso}

    inventario["Ouro"] += 10
    inventario["kit_aplicado"] = True
    print(f"Kit inicial da classe '{classe.capitalize()}' aplicado com sucesso!")


def mostrar_inventario():
    global ficha
    if ficha is None:
        print("Ficha não definida.")
        return
    print("\n---- *** Inventário *** ----")
    if not inventario["itens"]:
        print("Inventário vazio")
    else:
        for idx, (item, info) in enumerate(inventario["itens"].items(), start=1):
            print(f"{idx}. {item} | {info['peso']} Kg | ({info['quantidade']})")
    print(f"Ouro: {inventario['Ouro']}G\nPeso total: {calc_peso_itens()}/{calcular_capacidade_peso(ficha)}")

def adicionar_item(nome, quantidade, peso):
    global ficha
    if ficha is None:
        print("Ficha não definida.")
        return
    try:
        quantidade = int(quantidade)
        peso = float(peso)
    except ValueError:
        print("Quantia ou peso inválidos! Use apenas números.")
        return
    if quantidade <= 0 or peso <= 0:
        print("A quantidade e o peso devem ser positivos.")
        return

    atual = calc_peso_itens()
    max_peso = calcular_capacidade_peso(ficha)
    if atual + (peso * quantidade) > max_peso:
        print(f'"{nome}" excederia sua capacidade de carga.')
        return

    if nome in inventario["itens"]:
        peso_existente = inventario["itens"][nome]["peso"]
        if peso_existente == peso:
            inventario["itens"][nome]["quantidade"] += quantidade
        else:
            novo_nome = f"{nome} (variação)"
            inventario["itens"][novo_nome] = {"quantidade": quantidade, "peso": peso}
    else:
        inventario["itens"][nome] = {"quantidade": quantidade, "peso": peso}
    print(f'{nome} ({quantidade}) adicionado com sucesso!')

def editar_ouro(quantos):
    try:
        quantos = int(quantos)
    except ValueError:
        print("Valor de ouro inválido! Use um número inteiro.")
        return
    if inventario["Ouro"] + quantos < 0:
        print("Você não pode ficar com ouro negativo!")
        return
    inventario["Ouro"] += quantos
    if quantos < 0:
        print(f'{abs(quantos)}G removidos.')
    elif quantos > 0:
        print(f'{quantos}G foram adicionados.')
    else:
        print('Alteração de 0G? Nada foi alterado.')

def remover_item(posicao):
    try:
        posicao = int(posicao)
    except ValueError:
        print("Posição inválida!")
        return
    inventario_lista = list(inventario["itens"].items())
    if 0 <= posicao < len(inventario_lista):
        item, info = inventario_lista[posicao]
        quantia = info["quantidade"]
        print(f'Você selecionou {item} ({quantia})')
        if quantia == 1:
            inventario["itens"].pop(item)
        else:
            remove_item = input(f'Quantos de {item} deseja remover? ')
            if remove_item.isdigit():
                quantos = int(remove_item)
                if quantos <= 0:
                    print("Remoção inválida.")
                    return
                if quantos >= quantia:
                    inventario["itens"].pop(item)
                else:
                    inventario["itens"][item]["quantidade"] -= quantos
            else:
                print("Entrada inválida.")
    else:
        print("Item inválido!")

def escolher_ficha():
    pasta_fichas = obter_caminho_fichas()
    arquivos = [f for f in os.listdir(pasta_fichas) if f.endswith(".pkl") and not f.endswith("_inventario.pkl")]

    if not arquivos:
        print("Nenhuma ficha .pkl encontrada.")
        return None

    print("Escolha uma ficha:")
    for idx, nome in enumerate(arquivos, start=1):
        print(f"{idx}. {nome[:-4]}")

    while True:
        escolha = input("Digite o número da ficha: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(arquivos):
                nome_arquivo = arquivos[escolha - 1]
                nome_personagem = nome_arquivo[:-4].replace("_", " ")
                return nome_personagem
            else:
                print("Número fora do intervalo.")
        else:
            print("Entrada inválida.")

def menu_inventario():
    global ficha
    
    while True:
        # Sempre pedir a ficha antes de mostrar o menu
        print("Escolha uma ficha para acessar o inventário:")
        pasta_fichas = obter_caminho_fichas()
        arquivos = [f for f in os.listdir(pasta_fichas) if f.endswith(".pkl") and not f.endswith("_inventario.pkl")]

        if not arquivos:
            print("Nenhuma ficha .pkl encontrada.")
            return

        for idx, nome in enumerate(arquivos, start=1):
            print(f"{idx}. {nome.replace('.pkl', '')}")

        escolha = input("Digite o número da ficha (ou 0 para voltar): ").strip()
        if escolha == "0":
            return
        if not escolha.isdigit() or not (1 <= int(escolha) <= len(arquivos)):
            print("Escolha inválida, tente novamente.")
            continue

        nome_arquivo = arquivos[int(escolha) - 1]
        nome_personagem = nome_arquivo[:-4].replace("_", " ")
        f = carregar_ficha_personagem(nome_personagem)
        if f is None:
            print("Falha ao carregar a ficha.")
            continue
        definir_ficha(f)
        print(f"Ficha de {nome_personagem} carregada.")

        # Agora o menu do inventário para a ficha carregada
        while True:
            print("\n--- MENU DO INVENTÁRIO ---")
            print("1. Ver inventário")
            print("2. Adicionar item manualmente")
            print("3. Aplicar kit da classe")
            print("4. Editar ouro")
            print("5. Ver capacidade de carga")
            print("6. Ver peso total dos itens")
            print("7. Remover item do inventário")
            print("8. Salvar inventário")
            print("0. Voltar ao menu anterior")

            escolha_inv = input("Escolha uma opção (0-8): ").strip()

            if escolha_inv == "1":
                mostrar_inventario()
            elif escolha_inv == "2":
                nome_item = input("Nome do item: ").strip()
                quantidade = input("Quantidade: ").strip()
                peso = input("Peso por unidade (kg): ").strip()
                adicionar_item(nome_item, quantidade, peso)
            elif escolha_inv == "3":
                add_kit(ficha)
            elif escolha_inv == "4":
                quantia = input("Quanto ouro adicionar/remover? (use negativo para remover): ").strip()
                editar_ouro(quantia)
            elif escolha_inv == "5":
                capacidade = calcular_capacidade_peso(ficha)
                print(f"Capacidade de carga: {capacidade} Kg")
            elif escolha_inv == "6":
                peso_total = calc_peso_itens()
                print(f"Peso total dos itens: {peso_total} Kg")
            elif escolha_inv == "7":
                if not inventario["itens"]:
                    print("Inventário vazio!")
                    continue
                print("\nItens no inventário:")
                for idx, (item, info) in enumerate(inventario["itens"].items()):
                    print(f"{idx}: {item} ({info['quantidade']} unidades, {info['peso']} Kg cada)")
                pos = input("Digite o número do item que deseja remover: ").strip()
                remover_item(pos)
            elif escolha_inv == "8":
                if ficha:
                    salvar_inventario(ficha["nome"])
                else:
                    print("Ficha não definida. Não é possível salvar o inventário.")
            elif escolha_inv == "0":
                break
            else:
                print("Opção inválida! Escolha um número de 0 a 8.")

