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
