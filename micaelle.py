def alterar(pets):
    print("\n========== ALTERAR PET ==========")

    if len(pets) == 0:
        print("Nenhum pet cadastrado!")
        return

    nome_busca = input("Digite o nome do pet que deseja alterar: ")

    pet_encontrado = None

    for pet in pets:
        if pet.nome.lower() == nome_busca.lower():
            pet_encontrado = pet
            break

    if pet_encontrado is None:
        print("\nPet não encontrado!")
        return

    print("\nPet encontrado!")
    print("\nDigite os novos dados.")
    print("Se não quiser alterar algum dado, pressione ENTER.")

    # Alterar nome
    novo_nome = input(f"Novo nome ({pet_encontrado.nome}): ")

    if novo_nome != "":
        pet_encontrado.nome = novo_nome

    # Alterar idade
    nova_idade = input(f"Nova idade ({pet_encontrado.idade}): ")

    if nova_idade != "":
        try:
            nova_idade = int(nova_idade)

            if nova_idade >= 0:
                pet_encontrado.idade = nova_idade
            else:
                print("Idade inválida. A idade anterior foi mantida.")

        except ValueError:
            print("Idade inválida. A idade anterior foi mantida.")

    # Alterar raça
    nova_raca = input(f"Nova raça ({pet_encontrado.raca}): ")

    if nova_raca != "":
        pet_encontrado.raca = nova_raca

    # Alterar dono
    novo_dono = input(f"Novo dono ({pet_encontrado.dono}): ")

    if novo_dono != "":
        pet_encontrado.dono = novo_dono

    print("\nDados alterados com sucesso!")
