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
    # Retorna o caminho absoluto da pasta onde ficam as fichas
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

def salvar_inventario(nome_ficha):
    nome_base = nome_ficha.lower().replace(" ", "_")
    caminho_fichas = obter_caminho_fichas()
    nome_arquivo = os.path.join(caminho_fichas, f"{nome_base}_inventario.pkl")

    with open(nome_arquivo, "wb") as arq:
        pickle.dump(inventario, arq)
    print(f"Inventário salvo em: {nome_arquivo}")

def calcular_capacidade_peso(ficha):
    racas_peso = {
        "anão da colina": 10,
        "anão da montanha": 15,
        "alto elfo": 0,
        "elfo da floresta": 0,
        "drow": 0,
        "halfling pés-leves": 0,
        "halfling robusto": 0,
        "humano": 5,
        "draconato": 15,
        "gnomo da floresta": 0,
        "gnomo das rochas": 0,
        "meio-elfo": 0,
        "meio-orc": 15,
        "tiefling": 0,
        "anão": 15,
        "elfo": 0,
        "halfling": 0,
        "gnomo": 0
    }
    raca = ficha["raça"].strip().lower()
    forca = int(ficha["atributos"]["Força"])
    return racas_peso.get(raca, 0) + 15 * forca

def calc_peso_itens():
    peso_total = 0
    for item, info in inventario["itens"].items():
        quantos = info["quantidade"]
        kilos = info["peso"]
        peso_total += quantos * kilos
    return peso_total

def add_kit(ficha):
    classe = ficha["classe"].lower()
    if inventario["kit_aplicado"]:
        print("Kit já aplicado anteriormente.")
        return

    kit_classes = {
        "bárbaro": {"machado de batalha": {"quantidade": 1, "peso": 5.5}, "machadinha": {"quantidade": 2, "peso": 1.0}, "lança": {"quantidade": 4, "peso": 1.3}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        # Copie os kits completos aqui como você já tem...
        "bruxo": {"livro do pacto": {"quantidade": 1, "peso": 1.0}, "arma de pacto": {"quantidade": 1, "peso": 1.5}, "amuleto arcano": {"quantidade": 1, "peso": 0.2}, "poção de mana": {"quantidade": 1, "peso": 0.5}, "saco de dormir": {"quantidade": 1, "peso": 2.5}}
    }

    if classe not in kit_classes:
        print("Classe inválida!")
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
    print(f"Kit inicial de {classe} aplicado! WoW! Irado!")

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
            quantidade = info["quantidade"]
            peso = info["peso"]
            print(f"{idx}. {item} | {peso} Kg | ({quantidade})")
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
    if quantidade <= 0:
        print("A quantidade deve ser um número inteiro positivo!")
        return
    if peso <= 0:
        print("O peso do item deve ser um número positivo!")
        return
    atual = calc_peso_itens()
    max_peso = calcular_capacidade_peso(ficha)
    if atual + (peso * quantidade) > max_peso:
        print(f'"{nome}" excederia sua capacidade de carga e, portanto, não foi adicionado!')
        return

    if nome in inventario["itens"]:
        peso_existente = inventario["itens"][nome]["peso"]
        if peso_existente == peso:
            inventario["itens"][nome]["quantidade"] += quantidade
            print(f'{nome} ({quantidade}) adicionado com sucesso!')
        else:
            novo_nome = f"{nome} (variação)"
            inventario["itens"][novo_nome] = {"quantidade": quantidade, "peso": peso}
            print(f'{nome} ({quantidade}) foi adicionado em outro slot devido à variação de peso do item')
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
        print("Posição inválida! Use um número inteiro.")
        return
    inventario_lista = list(inventario["itens"].items())
    if 0 <= posicao < len(inventario_lista):
        item, info = inventario_lista[posicao]
        quantia = info["quantidade"]
        print(f'Você selecionou {item} ({quantia})')
        if quantia == 1:
            inventario["itens"].pop(item)
            print(f'{item} foi perdido para sempre.')
        else:
            remove_item = input(f'Quantos de {item} deseja remover? ')
            if remove_item.isdigit():
                quantos = int(remove_item)
                if quantos <= 0:
                    print("Remoção inválida. Use um número positivo.")
                    return
                if quantos >= quantia:
                    inventario["itens"].pop(item)
                    print(f'{item} foi perdido para sempre.')
                else:
                    inventario["itens"][item]["quantidade"] -= quantos
                    print(f'{quantos} unidades de {item} foram descartadas.')
            else:
                print("Entrada inválida, digite o número da posição do item no inventário.")
    else:
        print("Item inválido!")

def escolher_ficha():
    pasta_fichas = obter_caminho_fichas()
    arquivos = [f for f in os.listdir(pasta_fichas) if f.endswith(".pkl")]

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
            print("Entrada inválida, digite apenas o número.")

def menu_inventario():
    global ficha
    if ficha is None:
        print("Nenhuma ficha definida. Escolha uma ficha antes de acessar o inventário.")
        personagem = escolher_ficha()
        if personagem:
            f = carregar_ficha_personagem(personagem)
            if f:
                definir_ficha(f)
                print(f"Ficha de {personagem} carregada.")
            else:
                print("Falha ao carregar a ficha.")
                return
        else:
            return

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

        escolha = input("Escolha uma opção (0-8): ").strip()

        if escolha == "1":
            mostrar_inventario()
        elif escolha == "2":
            nome = input("Nome do item: ").strip()
            quantidade = input("Quantidade: ").strip()
            peso = input("Peso por unidade (kg): ").strip()
            adicionar_item(nome, quantidade, peso)
        elif escolha == "3":
            add_kit(ficha)
        elif escolha == "4":
            quantia = input("Quanto ouro adicionar/remover? (use negativo para remover): ").strip()
            editar_ouro(quantia)
        elif escolha == "5":
            capacidade = calcular_capacidade_peso(ficha)
            print(f"Capacidade de carga: {capacidade} Kg")
        elif escolha == "6":
            peso = calc_peso_itens()
            print(f"Peso total dos itens: {peso} Kg")
        elif escolha == "7":
            if not inventario["itens"]:
                print("Inventário vazio!")
                continue
            print("\nItens no inventário:")
            for idx, (item, info) in enumerate(inventario["itens"].items()):
                print(f"{idx}: {item} ({info['quantidade']} unidades, {info['peso']} Kg cada)")
            pos = input("Digite o número do item que deseja remover: ").strip()
            remover_item(pos)
        elif escolha == "8":
            if ficha:
                salvar_inventario(ficha["nome"])
            else:
                print("Ficha não definida. Não é possível salvar o inventário.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida! Escolha um número de 0 a 8.")

