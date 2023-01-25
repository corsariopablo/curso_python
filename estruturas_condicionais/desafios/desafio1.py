menu = """"

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Valor informado é inválido.')
        
        
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Saldo insuficiente!')
        
        elif excedeu_limite:
            print('Valor acima do limite diário!')
        
        elif excedeu_saques:
            print('Máximo 3 saques por dia!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f} \n'
            numero_saques += 1
        
        else:
            print('Algo de errado não está certo... tente novamente!')


    
    elif opcao == '3':
        print('\n **********########## EXTRATO ##########**********')
        print('Não foram realizadas movimentações em sua conta.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('====================================================')

    elif opcao == '0':
        print('Obrigado por usar o Banco 24h!')
        break

    else:
        print('Operação inválida, por favor selecione uma opção válida.')
