import random

# Listas expandidas
prefixos_personagem = [
    "Al", "Bel", "Zar", "Tor", "Gra", "Fen", "Lor", "Mor", "Sil", "El",
    "Kael", "Thal", "Ny", "Vael", "Ryn", "Aer", "Dur", "Eryn", "Sael", "Gal",
    "Bryn", "Kara", "Ther", "Nim", "Orin", "Cal", "Jor", "Mal", "Xel", "Yra"
]
sufixos_personagem = [
    "dor", "mir", "thas", "gorn", "drak", "lian", "zeth", "mund", "rion", "xar",
    "mael", "nor", "ion", "bar", "viel", "dros", "vorn", "hiel", "thur", "ekar",
    "dil", "vyn", "ak", "en", "lor", "grim", "thul", "rad", "ien", "dos"
]

partes_monstro = [
    "Kroo", "Zig", "Tuh", "Bbron", "Oog", "Vuun", "Ur", "Sik", "Ahbron", "Drhong",
    "Gryin", "Nha", "Szy", "Xry", "Dr.", "Ph", "Glorp", "AAbron", "Shrek", "Tirek",
    "Zhon", "Fr", "Rk", "smuung", "Ob", "Sl", "Kz", "Yg", "Bl", "Gleeby"
]
finais_monstro = [
    "org", "nash", "goth", "raak", "zeer", "mogg", "zoth", "nurk", "drogg", "thuun",
    "laxx", "gur", "baal", "rekh", "vrax", "khuur", "xan", "grel", "zhak", "brok",
    "ugth", "mash", "dron", "karg", "zolg", "bruth", "drax", "shogg", "braag", "Deeby"
]

prefixos_lugar = [
    "El", "Thal", "My", "Vel", "Drak", "Ost", "Kael", "Zun", "Far", "Is",
    "Nor", "Val", "Aer", "Lun", "Mar", "Syl", "Nym", "Cor", "Aeth", "Brae",
    "Eri", "Tor", "Gal", "Rha", "Xan", "Lor", "Varn", "Sael", "Mal", "Zar",
    "Del", "Thyr", "Ila", "Or", "Krel", "Fen", "Bran", "Ysil", "Ulm", "Tir"
]
sufixos_lugar = [
    "arion", "dor", "khal", "thora", "myr", "ereth", "varia", "dara", "neth", "ave",
    "andir", "mir", "ion", "eth", "oria", "vyr", "wyn", "dell", "mere", "hal",
    "amar", "rel", "drith", "wynor", "kar", "harn", "uris", "eon", "aneth", "rax",
    "zhar", "quor", "dun", "fyr", "mos", "ul", "theas", "orn", "grin", "toril"
]

# Função base para combinar nomes
def gerar_nome(prefixos, sufixos):
    nome1 = random.choice(prefixos) + random.choice(sufixos)

    chance = random.random()

    # 20% de chance de adicionar hífen
    if chance < 0.2:
        nome2 = random.choice(prefixos) + random.choice(sufixos)
        return f"{nome1}-{nome2}"
    # 20% de chance de nome composto separado
    elif chance < 0.4:
        nome2 = random.choice(prefixos) + random.choice(sufixos)
        return f"{nome1} {nome2}"
    else:
        return nome1

# Funções finais expostas para o menu
def gerar_nome_personagem():
    return gerar_nome(prefixos_personagem, sufixos_personagem)

def gerar_nome_monstro():
    return gerar_nome(partes_monstro, finais_monstro)

def gerar_nome_lugar():
    return gerar_nome(prefixos_lugar, sufixos_lugar)
