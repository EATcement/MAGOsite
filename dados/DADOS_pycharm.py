import random
d4= {
    1: ("           ","┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("           ","┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("           ","┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("           ","┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘")
}
d6 = {
    1: ("           ","┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("           ","┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("           ","┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("           ","┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("           ","┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("           ","┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘")
}
d8 = {
    1: ("           ", "┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("           ", "┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("           ", "┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("           ", "┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("           ", "┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("           ", "┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
    7: ("           ", "┌─────────┐", "│ ●     ● │", "│ ●  ●  ● │", "│ ●     ● │", "└─────────┘"),
    8: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●     ● │", "│ ●  ●  ● │", "└─────────┘")
}
d10 = {
    1: ("           ", "┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("           ", "┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("           ", "┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("           ", "┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("           ", "┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("           ", "┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
    7: ("           ", "┌─────────┐", "│ ●     ● │", "│ ●  ●  ● │", "│ ●     ● │", "└─────────┘"),
    8: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●     ● │", "│ ●  ●  ● │", "└─────────┘"),
    9: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●  ●  ● │", "│ ●  ●  ● │", "└─────────┘"),
    10: ("┌───────────┐", "│ ●     ● ● │", "│       ● ● │", "│ ● ●       │", "│ ● ●     ● │", "└───────────┘")
}
d12 = {
    1: ("           ", "┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("           ", "┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("           ", "┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("           ", "┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("           ", "┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("           ", "┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
    7: ("           ", "┌─────────┐", "│ ●     ● │", "│ ●  ●  ● │", "│ ●     ● │", "└─────────┘"),
    8: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●     ● │", "│ ●  ●  ● │", "└─────────┘"),
    9: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●  ●  ● │", "│ ●  ●  ● │", "└─────────┘"),
    10: ("┌───────────┐", "│ ●     ● ● │", "│       ● ● │", "│ ● ●       │", "│ ● ●     ● │", "└───────────┘"),
    11: ("┌───────────┐", "│   ●   ●   │", "│   ● ● ●   │", "│   ● ● ●   │", "│   ● ● ●   │", "└───────────┘"),
    12: ("┌───────────┐", "│     ●     │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│     ●     │", "└───────────┘")
}
d20 = {
    1: ("           ", "┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("           ", "┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("           ", "┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("           ", "┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("           ", "┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("           ", "┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
    7: ("           ", "┌─────────┐", "│ ●     ● │", "│ ●  ●  ● │", "│ ●     ● │", "└─────────┘"),
    8: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●     ● │", "│ ●  ●  ● │", "└─────────┘"),
    9: ("           ", "┌─────────┐", "│ ●  ●  ● │", "│ ●  ●  ● │", "│ ●  ●  ● │", "└─────────┘"),
    10: ("┌───────────┐", "│ ●     ● ● │", "│       ● ● │", "│ ● ●       │", "│ ● ●     ● │", "└───────────┘"),
    11: ("┌───────────┐", "│   ●   ●   │", "│   ● ● ●   │", "│   ● ● ●   │", "│   ● ● ●   │", "└───────────┘"),
    12: ("┌───────────┐", "│     ●     │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│     ●     │", "└───────────┘"),
    13: ("┌───────────┐", "│     ●     │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│    ● ●    │", "└───────────┘"),
    14: ("┌───────────┐", "│    ● ●    │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│    ● ●    │", "└───────────┘"),
    15: ("┌───────────┐", "│    ● ●    │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│   ● ● ●   │", "└───────────┘"),
    16: ("┌───────────┐", "│   ● ● ●   │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│   ● ● ●   │", "└───────────┘"),
    17: ("┌───────────┐", "│   ● ● ●   │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│  ● ● ● ●  │", "└───────────┘"),
    18: ("┌───────────┐", "│  ● ● ● ●  │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│  ● ● ● ●  │", "└───────────┘"),
    19: ("┌───────────┐", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│  ● ● ● ●  │", "└───────────┘"),
    20: ("┌───────────┐", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "│ ● ● ● ● ● │", "└───────────┘")
}
dados_dict = {
    'd4': d4,
    'd6': d6,
    'd8': d8,
    'd10': d10,
    'd12': d12,
    'd20': d20
}
historico = []
def jogar_dado(valor, quantia):
    if valor not in dados_dict:
        print(f'Tolo! "{valor}" não é um dado válido!')
        return
    if not isinstance(quantia, int) or quantia <= 0:
        print("A quantidade de dados deve ser um número inteiro positivo!")
        return
    if quantia > 15:
        print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
        return
    dnum = dados_dict[valor]
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for i in range(quantia)]
    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")
    historico.append({"dado": valor.upper(), "quantia": quantia, "resultados": result, "total": sum(result)})

def jogar_d4():
    try:
        quantia = int(input("Quantos D4 você deseja rolar? "))
        if quantia <= 0:
            print("A quantidade de dados deve ser um número inteiro positivo!")
            return
        if quantia > 15:
            print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return

    dnum = dados_dict['d4']
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for _ in range(quantia)]

    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")

    historico.append({"dado": 'D4', "quantia": quantia, "resultados": result, "total": sum(result)})

def jogar_d6():
    try:
        quantia = int(input("Quantos D6 você deseja rolar? "))
        if quantia <= 0:
            print("A quantidade de dados deve ser um número inteiro positivo!")
            return
        if quantia > 15:
            print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return

    dnum = dados_dict['d6']
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for _ in range(quantia)]

    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")

    historico.append({"dado": 'D6', "quantia": quantia, "resultados": result, "total": sum(result)})

def jogar_d8():
    try:
        quantia = int(input("Quantos D8 você deseja rolar? "))
        if quantia <= 0:
            print("A quantidade de dados deve ser um número inteiro positivo!")
            return
        if quantia > 15:
            print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return

    dnum = dados_dict['d8']
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for _ in range(quantia)]

    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")

    historico.append({"dado": 'D8', "quantia": quantia, "resultados": result, "total": sum(result)})

def jogar_d10():
    try:
        quantia = int(input("Quantos D10 você deseja rolar? "))
        if quantia <= 0:
            print("A quantidade de dados deve ser um número inteiro positivo!")
            return
        if quantia > 15:
            print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return

    dnum = dados_dict['d10']
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for _ in range(quantia)]

    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")

    historico.append({"dado": 'D10', "quantia": quantia, "resultados": result, "total": sum(result)})

def jogar_d12():
    try:
        quantia = int(input("Quantos D12 você deseja rolar? "))
        if quantia <= 0:
            print("A quantidade de dados deve ser um número inteiro positivo!")
            return
        if quantia > 15:
            print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return

    dnum = dados_dict['d12']
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for _ in range(quantia)]

    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")

    historico.append({"dado": 'D12', "quantia": quantia, "resultados": result, "total": sum(result)})

def jogar_d20():
    try:
        quantia = int(input("Quantos D20 você deseja rolar? "))
        if quantia <= 0:
            print("A quantidade de dados deve ser um número inteiro positivo!")
            return
        if quantia > 15:
            print("Quantidade muito alta! Máximo permitido é 15 dados por vez.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return

    dnum = dados_dict['d20']
    maior = max(dnum.keys())
    result = [random.randint(1, maior) for _ in range(quantia)]

    for line in range(6):
        for dao in result:
            print(dnum.get(dao)[line], "", end="")
        print()
    print(f"\nValores: {result} | Total: {sum(result)}")

    historico.append({"dado": 'D20', "quantia": quantia, "resultados": result, "total": sum(result)})


def mostrar_historico():
    print("\n" + "_"*80)
    print("| Dado | QNT | Resultados" + " "*46 + "| Total |")
    print("|" + "-"*78 + "|")

    for entrada in historico:
        dado = entrada["dado"]
        quantia = entrada["quantia"]
        resultados = ", ".join(str(n) for n in entrada["resultados"])
        total = str(entrada["total"]).rjust(5, "0")
        linha = f"| {dado.center(4)} | {str(quantia).center(3)} | {resultados.ljust(56)}| {total} |"
        print(linha)
    print("-"*80)

