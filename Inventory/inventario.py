inventario = {
    "itens": {},
    "Ouro": 0,
    "kit_aplicado": False
}

personagem = {
    "nome": "GOZADOR DO DIABO", "raça": "halfling", "inteligência": 15, "força": 20, "classe": "patrulheiro"
}

def calcular_capacidade_peso():
    raças_peso = {
        "anão das colinas": 10,
        "anão da montanha": 15,
        "alto elfo ": 0,
        "elfo da floresta": 0,
        "elfo negro (drow)": 0,
        "halfling pés-leves": 0,
        "halfling robusto": 0,
        "humano": 5,
        "draconato": 15,
        "gnomo da floresta": 0,
        "gnomo das rochas": 0,
        "meio-elfo": 0,
        "meio-orc": 15,
        "tiefling": 0
    }
    raça_personagem = personagem["raça"].strip().lower()
    força_personagem = personagem["força"]
    failsafe = raças_peso.get(raça_personagem, 0)
    return failsafe + 15 * força_personagem

def calc_peso_itens():
    peso_total = 0
    for item, info in inventario["itens"].items():
        quantos = info["quantidade"]
        kilos = info["peso"]
        peso_total += quantos * kilos
    return peso_total

def add_kit():
    if inventario["kit_aplicado"]:
        return

    kit_classes = {
        "barbaro": {"machado de batalha": {"quantidade": 1, "peso": 5.5}, "machadinha": {"quantidade": 2, "peso": 1.0}, "lança": {"quantidade": 4, "peso": 1.3}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "bardo": {"armadura de couro": {"quantidade": 1, "peso": 4.0}, "rapieira": {"quantidade": 1, "peso": 1.0}, "adaga": {"quantidade": 1, "peso": 0.5}, "alaúde": {"quantidade": 1, "peso": 1.5}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "clerigo": {"maça": {"quantidade": 1, "peso": 2.0}, "escudo": {"quantidade": 1, "peso": 3.0}, "armadura de malha": {"quantidade": 1, "peso": 20.0}, "amuleto sagrado": {"quantidade": 1, "peso": 0.2}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "druida": {"cajado de madeira": {"quantidade": 1, "peso": 2.0}, "armadura de couro": {"quantidade": 1, "peso": 4.0}, "cimitarra": {"quantidade": 1, "peso": 1.5}, "amuleto da natureza": {"quantidade": 1, "peso": 0.2}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "guerreiro": {"espada longa": {"quantidade": 1, "peso": 1.5}, "armadura de malha": {"quantidade": 1, "peso": 20.0}, "escudo": {"quantidade": 1, "peso": 3.0}, "lança": {"quantidade": 2, "peso": 1.3}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "monge": {"bastão": {"quantidade": 1, "peso": 2.0}, "lança": {"quantidade": 10, "peso": 1.3}, "manto de monge": {"quantidade": 1, "peso": 1.0}, "corda 30m": {"quantidade": 1, "peso": 4.5}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "paladino": {"claymore": {"quantidade": 1, "peso": 3.5}, "escudo": {"quantidade": 1, "peso": 3.0}, "armadura de placas": {"quantidade": 1, "peso": 30.0}, "símbolo sagrado": {"quantidade": 1, "peso": 0.2}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "patrulheiro": {"espada curta": {"quantidade": 2, "peso": 1.0}, "armadura de couro": {"quantidade": 1, "peso": 4.0}, "arco longo": {"quantidade": 1, "peso": 1.5}, "flechas": {"quantidade": 20, "peso": 0.1}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "ladino": {"adaga": {"quantidade": 2, "peso": 0.5}, "armadura de couro": {"quantidade": 1, "peso": 4.0}, "espada curta": {"quantidade": 1, "peso": 1.0}, "gazua": {"quantidade": 5, "peso": 0.05}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "mago": {"cajado arcano": {"quantidade": 1, "peso": 2.0}, "tomo de magias": {"quantidade": 1, "peso": 3.0}, "poção de mana": {"quantidade": 2, "peso": 0.5}, "roupas arcanas": {"quantidade": 1, "peso": 2.0}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "feiticeiro": {"varinha mágica": {"quantidade": 1, "peso": 0.7}, "cristal de foco": {"quantidade": 1, "peso": 0.3}, "poção de mana": {"quantidade": 2, "peso": 0.5}, "roupas arcanas": {"quantidade": 1, "peso": 2.0}, "saco de dormir": {"quantidade": 1, "peso": 2.5}},
        "warlock": {"livro do pacto": {"quantidade": 1, "peso": 3.0}, "arma de pacto": {"quantidade": 1, "peso": 1.5}, "amuleto arcano": {"quantidade": 1, "peso": 0.2}, "poção de mana": {"quantidade": 1, "peso": 0.5}, "saco de dormir": {"quantidade": 1, "peso": 2.5}}
    }

    classe = personagem["classe"].lower()
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
    print("\n---- *** Inventário *** ----")
    if not inventario["itens"]:
        print("Inventário vazio")
    else:
        for idx, (item, info) in enumerate(inventario["itens"].items(), start=1):
            quantidade = info["quantidade"]
            peso = info["peso"]
            print(f"{idx}. {item}  {peso}Kg ({quantidade})")
    print(f"Ouro: {inventario['Ouro']}G\nPeso total: {calc_peso_itens()}/{calcular_capacidade_peso()}")

def adicionar_item(nome, quantidade, peso):
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
    max_peso = calcular_capacidade_peso()
    if atual + (peso * quantidade) >= max_peso:
        print(f'"{nome}" Excediria sua capacidade de carga e portanto não foi adicionado!')
        return

    if nome in inventario["itens"]:
        peso_existente = inventario["itens"][nome]["peso"]
        if peso_existente == peso:
            inventario["itens"][nome]["quantidade"] += quantidade
            print(f'{nome}({quantidade} adicionado com sucesso!)')
        else:
            novo_nome = f"{nome} (variação)"
            inventario["itens"][novo_nome] = {"quantidade": quantidade, "peso": peso}
            print(f'{nome} ({quantidade})foi adicionado em outro slot devido a varaição de peso do item')
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
        print(f'Você selecionou {item}({quantia})')
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
                print("Entrada inválida, digite o N° da posição do item no inventário")
    else:
        print("Item inválido!")

