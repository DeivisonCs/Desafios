import functions

while True:
    option = functions.main_Menu()

    match option:
        case 0:
            break

        case 1:
            print("Adicionar")

        case 2:
            print("Atualizar")

        case 3:
            print("Listar")

        case 4:
            print("Excluir")

        case _:
            print("Valor Inválido!")
            
