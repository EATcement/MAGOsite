from .gerar_nomes import (
    gerar_nome_personagem,
    gerar_nome_monstro,
    gerar_nome_lugar
)


def menu_gerador_nomes():
    opcoes = {
        "1": ("Nome de Personagem", gerar_nome_personagem),
        "2": ("Nome de Monstro", gerar_nome_monstro),
        "3": ("Nome de Lugar", gerar_nome_lugar)
    }

    print("\n--- Gerador de Nomes Aleatórios ---")
    for chave, (descricao, _) in opcoes.items():
        print(f"{chave}. {descricao}")

    escolha = input("Escolha o tipo de nome (1-3): ").strip()
    if escolha not in opcoes:
        print("Opção inválida.")
        return

    while True:
        qtd = input("Quantos nomes deseja gerar (1 a 3)? ").strip()
        if qtd.isdigit() and 1 <= int(qtd) <= 3:
            qtd = int(qtd)
            break
        print("Quantidade inválida. Tente novamente.")

    nome_tipo, funcao_geradora = opcoes[escolha]
    print(f"\n{nome_tipo}s gerados:")
    for _ in range(qtd):
        print("-", funcao_geradora())



if __name__ == "__main__":
    menu_gerador_nomes()
