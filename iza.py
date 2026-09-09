def consultar(pets):
    if len(pets) == 0:
        print("\nNenhum pet cadastrado!")
        return

    print("\n===== CONSULTAR PETS =====")
    print("1 - Ver todos os pets")
    print("2 - Buscar pet pelo nome")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n===== LISTA DE PETS =====")

        for pet in pets:
            print("-------------------------")
            print(f"Nome: {pet.nome}")
            print(f"Idade: {pet.idade}")
            print(f"Raça: {pet.raca}")
            print(f"Espécie: {pet.especie}")

    elif opcao == "2":
        nome_busca = input("Digite o nome do pet: ").lower()
        encontrado = False

        for pet in pets:
            if pet.nome.lower() == nome_busca:
                print("\n===== PET ENCONTRADO =====")
                print(f"Nome: {pet.nome}")
                print(f"Idade: {pet.idade}")
                print(f"Raça: {pet.raca}")
                print(f"Espécie: {pet.especie}")
                encontrado = True
                break

        if not encontrado:
            print("\nPet não encontrado!")

    else:
        print("\nOpção inválida!")