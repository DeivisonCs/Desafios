class Alunos:
    def __init__(self, name, age, cpf, matricula, sexo):
        self.name = name
        self.age = age
        self.cpf= cpf
        self.matricula = matricula
        self.sexo = sexo


def main_Menu():
    print("------------- Menu -----------\n")
    print("1 - Adicionar")
    print("2 - Atualizar")
    print("3 - Listar")
    print("4 - Excluir")
    print("0 - sair")

    return int(input("\n--> "))


# ------------- Inserir ---------------

def verify_Cad(age, cpf, mat, sex):

    # sex = sex.upper()
    if age < 0:
        print("\nIdade Inválida!\n")
        return False

    elif sex.upper() != 'M' and sex.upper() != 'F': 
        print("\nSexo Inválido!\n")
        return False
    
    elif mat < 0:
        print("\nMatricula Inválida!\n")
        return False
    
    else: 
        return True


def new_student(Lista):
    name = input("Nome: ")
    age = int(input("Idade: "))
    

    cpf = input("CPF: ")
    mat = int(input("Matricula: "))
    sex = input("Sexo: ")

    valid = verify_Cad(age, cpf, mat, sex)

    if valid == True:
        Lista.append(Alunos(name=name, age=age, cpf=cpf, matricula=mat, sexo=sex))
        return True
    else:
        return False
    

# ------------------ Listar --------------------

def show_Students(List):
    for item in List:
        print(f"\tNome: {item.name}")
        print(f"\tIdade: {item.age}")
        print(f"\tSexo: {item.sexo}")
        print(f"\tMatricula: {item.matricula}")
        print(f"\tCPF: {item.cpf}\n")