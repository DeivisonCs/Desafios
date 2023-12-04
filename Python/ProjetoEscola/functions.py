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

def verify_int(x):
    if x.isdigit():
        return True
    
    return False


def verify_Cad(age, cpf, mat, sex):

    # sex = sex.upper()
    if verify_int(age) == False:
        print("\nIdade Inválida!")
        return False

    elif int(age) < 0:
        print("\nIdade Inválida!")
        return False
    
    elif sex.upper() != 'M' and sex.upper() != 'F': 
        print("\nSexo Inválido!")
        return False
    
    elif verify_int(mat) == False:
        print("\nMatricula Inválida!")
        return False
    
    elif int(mat) < 0:
        print("\nMatricula Inválida!")
        return False
    
    else: 
        return True


def new_student(Lista):
    name = input("Nome: ")
    age = input("Idade: ")
    cpf = input("CPF: ")
    mat = input("Matricula: ")
    sex = input("Sexo: ")

    valid = verify_Cad(age, cpf, mat, sex)

    if valid == True:
        age = int(age)
        mat = int(mat)
        sex = sex.upper()

        Lista.append(Alunos(name=name, age=int(age), cpf=cpf, matricula=int(mat), sexo=sex))
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