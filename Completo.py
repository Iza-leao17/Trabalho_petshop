class Pet:
    def __init__(self, nome, idade, raca, dono):
   
        self.__nome = nome
        self.idade = idade
        self.raca = raca
        self.dono = dono


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


    def fazer_som(self):
        return "Som de animal"


    def exibir_dados(self):
        print("-----------------------------")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Dono: {self.dono}")
        print(f"Som: {self.fazer_som()}")
        print("-----------------------------")
       
class Cachorro(Pet):


    def fazer_som(self):
        return "Au au!"




class Gato(Pet):


    def fazer_som(self):
        return "Miau!"


def cadastrar(pets):


    print("\n========== CADASTRAR PET ==========")


    nome = input("Nome do pet: ")


    try:
        idade = int(input("Idade do pet: "))


        if idade < 0:
            print("A idade não pode ser negativa!")
            return


    except ValueError:
        print("Digite uma idade válida!")
        return


    raca = input("Raça do pet: ")
    dono = input("Nome do dono: ")


    print("\nEscolha a espécie:")
    print("1 - Cachorro")
    print("2 - Gato")


    especie = input("Opção: ")


    if especie == "1":
        pet = Cachorro(nome, idade, raca, dono)


    elif especie == "2":
        pet = Gato(nome, idade, raca, dono)


    else:
        print("Espécie inválida!")
        return


    pets.append(pet)


    print("\nPet cadastrado com sucesso!")

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

    novo_nome = input(f"Novo nome ({pet_encontrado.nome}): ")

    if novo_nome != "":
        pet_encontrado.nome = novo_nome

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

    nova_raca = input(f"Nova raça ({pet_encontrado.raca}): ")

    if nova_raca != "":
        pet_encontrado.raca = nova_raca

    novo_dono = input(f"Novo dono ({pet_encontrado.dono}): ")

    if novo_dono != "":
        pet_encontrado.dono = novo_dono

    print("\nDados alterados com sucesso!")

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
    "Tem certeza que deseja excluir este pet? (S/N): ")

    if confirmacao.lower() == "s":

        pets.remove(pet_encontrado)

        print("\nPet excluído com sucesso!")

    else:
        print("\nExclusão cancelada!")

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