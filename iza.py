def consultar(pets):

    print("\n========== CONSULTAR PETS ==========")

    if len(pets) == 0:
        print("Nenhum pet cadastrado!")                                                                                                                                                                                                                                       
        return

    print("1 - Consultar todos")
    print("2 - Buscar pelo nome")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n========== PETS CADASTRADOS ==========")

        for pet in pets:
            pet.exibir_dados()

    elif opcao == "2":

        nome_busca = input("Digite o nome do pet: ")

        encontrado = False

        for pet in pets:

            if pet.nome.lower() == nome_busca.lower():

                print("\n========== PET ENCONTRADO ==========")

                pet.exibir_dados()

                encontrado = True
                break

        if not encontrado:
            print("\nPet não encontrado!")

    else:
        print("Opção inválida!")
