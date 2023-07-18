menu = '''
========== MENU ==========
[1]-Sacar
[2]-Depositar
[3]-Extrato
[0]-Sair\n'''

LIMITE_SAQUE = 3
LIMITE_POR_SAQUE = 500
saldo = 0.0
extrato = '\t========Extrato=========\n\n'
numero_saques = 0

while True:

    print(menu)
    operacao = int(input('Selecione a operação: '))

    if operacao == 1:
        if saldo == 0:
            print('Sem saldo!\n')
            continue
        elif numero_saques >= LIMITE_SAQUE:
            print('Saques diários excedidos!\n')
            continue
        else:
            valor_saque = float(input('Valor a sacar: R$'))

            if (valor_saque > LIMITE_POR_SAQUE):
                print('Limite por saque excedido!')
                print(f'Limite: R${LIMITE_POR_SAQUE:.2f}')
                continue
            elif (valor_saque > saldo):
                print('\nSaldo insuficiente!')
                print(f'Saldo atual: R${saldo:.2f}')
                continue
            else:
                print(f'\nValor do saque:{valor_saque:.2f}')
                print(f'Saldo após saque:{saldo-valor_saque:.2f}')

                confirmacao = int(input('[1] confirmar [2] cancelar: '))
                if confirmacao == 2:
                    continue
                else:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato = extrato + f'\tSaque: R${valor_saque:.2f}\n\tSaldo: R${saldo:.2f}\n\n'
    
    elif operacao == 2:
        valor_deposito = float(input('Insira o valor: R$'))

        if valor_deposito <= 0:
            print('Valor inválido!\n')
            continue
        
        print(f'\nValor do depósito: R${valor_deposito:.2f}')
        print(f'Saldo após depósito: R${saldo + valor_deposito:.2f}')

        confirmacao = int(input('[1] confirmar [2] cancelar: '))
        if confirmacao == 2:
            continue
        else:
            saldo += valor_deposito
            extrato += f'\tDepósito: R${valor_deposito:.2f}\n\tSaldo: R${saldo:.2f}\n\n'

    elif operacao == 3:
        print(extrato)
        print('\t========================')

    elif operacao == 0:
        break

    else:
        print('\nOpção inválida')
        continue

print('\nVolte sempre!!!')
