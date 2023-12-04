import functions

__Alunos = []


while True:
    option = functions.main_Menu()

    match option:
        case "0":
            break

        case "1":
            print("------------- Adicionar -----------")
            valid = functions.new_student(__Alunos)

            if valid == True:
                print("\nAluno Inserido!\n")
            else:
                print("Aluno Não Inserido!\n")
                
        case "2":
            print("------------- Atualizar -------------")
            valid = functions.update(__Alunos)            

        case "3":
            print("------------- Listar -------------\n")
            functions.show_Students(__Alunos)

        case "4":
            print("------------- Excluir -------------")

        case _:
            print("Valor Inválido!")
            
