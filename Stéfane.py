def excluir(pets):

    print("\n========== EXCLUIR PET ==========")

    if len(pets) == 0:
        print("Nenhum pet cadastrado!")
        return

    nome_busca = input("Digite o nome do pet que deseja excluir: ")

    pet_encontrado = None

    for pet in pets:

        if pet.nome.lower() == nome_busca.lower():
            pet_encontrado = pet
            break

    if pet_encontrado is None:
        print("\nPet não encontrado!")
        return

    print("\nPet encontrado:")
    pet_encontrado.exibir_dados()

    confirmacao = input(
        "Tem certeza que deseja excluir este pet? (S/N): "
    )

    if confirmacao.lower() == "s":

        pets.remove(pet_encontrado)

        print("\nPet excluído com sucesso!")

    else:
        print("\nExclusão cancelada!")

# MENU PRINCIPAL

def menu():

    pets = []

    while True:

        print("\n")
        print("======================================")
        print("       🐾 SISTEMA PET SHOP 🐾")
        print("======================================")
        print("1 - Cadastrar pet")
        print("2 - Consultar pets")
        print("3 - Alterar pet")
        print("4 - Excluir pet")
        print("5 - Sair")
        print("======================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cadastrar(pets)

        elif opcao == "2":

            consultar(pets)

        elif opcao == "3":

            alterar(pets)

        elif opcao == "4":

            excluir(pets)

        elif opcao == "5":

            print("\nEncerrando o sistema...")
            print("Obrigada por utilizar o Pet Shop!")

            break

        else:

            print("\nOpção inválida!")
            print("Escolha uma opção de 1 a 5.")

# INICIAR O PROGRAMA

if __name__ == "__main__":
    menu()

