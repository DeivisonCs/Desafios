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

    return input("\n--> ")


def verify_int(x):
    if x.isdigit():
        return True
    
    return False

def get_Matricula():
    value = input("\nDigite a Matricula: ")

    if verify_int(value):
        return int(value)
    else:
        return False
    
def search_Matricula(List, search):
    for aluno in List:
        if aluno.matricula == search:
            return aluno
        
    return False


# --------------------------------- Inserir ----------------------------------

def verify_Cad(age, cpf, mat, sex):

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
    

# ---------------------------------- Atualizar -----------------------------------

def update_Menu():
    print("\n------------- Atualizar -----------\n")
    print("1 - Nome")
    print("2 - Idade")
    print("3 - Matricula")
    print("4 - CPF")
    print("5 - Sexo")
    print("0 - Voltar")

    return input("\n--> ")


def update(List):
    search = get_Matricula()

    if search:
        aluno = search_Matricula(List, search)
        if aluno == False:
            print("Aluno não Encontrado!")
            return aluno
        
        else:
            while True:
                option = update_Menu()

                match option:

                    case "0":
                        break

                    case "1":
                        aluno.name = input("\nNovo nome: ")

                    case "2":
                        new_Age = input("\nNova Idade: ")

                        valid = verify_int(new_Age)
                        if valid:
                            new_Age = int(new_Age)

                        if new_Age < 0:
                            print("\nIdade Inválida!")
                            continue
                        else:
                            aluno.age = new_Age
                            print("Idade Atualizada!")

                    case "3":
                        new_Mat = input("\nNova Matricula: ")

                        valid = verify_int(new_Mat)
                        if valid:
                            new_Mat = int(new_Mat)

                        if new_Mat < 0:
                            print("\nMatricula Inválida!")
                            continue
                        else:
                            aluno.matricula = new_Mat
                            print("Matricula Atualizada!")

                    case "4":
                        new_CPF = input("\nNovo CPF: ")

                        aluno.cpf = new_CPF
                        print("CPF Atualizado!")
                    
                    case "5":
                        new_Sex = input("\nNovo Sexo: ")

                        if new_Sex.upper() != 'M' and new_Sex.upper() != 'F':
                            print("\nSexo Inválido!")
                            continue
                        else:
                            aluno.sexo = new_Sex.upper()
                            print("\nSexo Atualizado!")

                    case _:
                        print("\nValor Inválido!")
    else:
        print("\nMatricula Inválida!\n")

# -------------------------------- Excluir ------------------------------------

def remove_Student(List):
    search = get_Matricula()

    if search:
        student = search_Matricula(List, search)
        
        print_Student(student)
        valid = input("Excluir aluno (S-sim/ N-não): ")

        if valid.upper() == 'S':
            List.pop(List.index(student))
            return True
        else:
            return False

# -------------------------------- Listar ------------------------------------

def show_Students(List):
    for student in List:
        print(f"\tNome: {student.name}")
        print(f"\tIdade: {student.age}")
        print(f"\tSexo: {student.sexo}")
        print(f"\tMatricula: {student.matricula}")
        print(f"\tCPF: {student.cpf}\n")

def print_Student(student):
    print(f"\tNome: {student.name}")
    print(f"\tIdade: {student.age}")
    print(f"\tSexo: {student.sexo}")
    print(f"\tMatricula: {student.matricula}")
    print(f"\tCPF: {student.cpf}\n")


#--------------------------------- Cadastros de Teste ---------------------------

def mod_Test(List):
    List.append( Alunos(name="Pedro", age=17, cpf="123.123.123-12", matricula=1, sexo="M") )
    List.append( Alunos(name="Maria", age=20, cpf="132.143.622-02", matricula=2, sexo="F") )
    List.append( Alunos(name="Felipe", age=29, cpf="123.123.123-12", matricula=3, sexo="M") )
    List.append( Alunos(name="Beatriz", age=23, cpf="185.194.833-62", matricula=4, sexo="F") )
    List.append( Alunos(name="Ana", age=19, cpf="171.181.513-15", matricula=5, sexo="F") )
