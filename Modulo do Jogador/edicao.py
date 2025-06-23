import pickle

def editar_ficha():
    try:
        with open("dicionarios.pkl", "rb") as f:
            dicionarios = pickle.load(f)
    except FileNotFoundError:
        print("❌ Arquivo 'dicionarios.pkl' não encontrado.")
        return

    print("\n📋 IDs de fichas disponíveis:")
    for id_ficha in dicionarios:
        print(f" - {id_ficha}")

    id_editar = input("\nDigite o ID da ficha que deseja editar: ").strip()

    if id_editar not in dicionarios:
        print("⚠️ ID não encontrado.")
        return

    ficha = dicionarios[id_editar]
    print(f"\n📄 Dados atuais da ficha {id_editar}:")
    for chave, valor in ficha.items():
        print(f"{chave}: {valor}")

    campo = input("\nQual campo deseja editar (nome, idade, habilidades)? ").strip().lower()

    if campo not in ficha:
        print("⚠️ Campo inválido.")
        return

    novo_valor = input(f"Digite o novo valor para '{campo}': ").strip()

    # Converte para o tipo correto, se necessário
    if campo == "idade":
        try:
            novo_valor = int(novo_valor)
        except ValueError:
            print("❌ Idade deve ser um número.")
            return
    elif campo == "habilidades":
        novo_valor = [h.strip() for h in novo_valor.split(",")]

    ficha[campo] = novo_valor
    dicionarios[id_editar] = ficha

    with open("dicionarios.pkl", "wb") as f:
        pickle.dump(dicionarios, f)

    print("✅ Ficha atualizada com sucesso!")
