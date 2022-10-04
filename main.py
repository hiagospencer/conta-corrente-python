from ContaBanco import ContaCorrente, CartaoCredito
from agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual
from time import sleep
import os
        
# Programa
conta_hiago = ContaCorrente(nome='', cpf=0, agencia=0, num_conta=0)

cartao_hiago = CartaoCredito('Hiago', conta_hiago)

while True:
    sleep(4)
    os.system('cls')
    
    print('')
    print('=~'*20)
    print('    B A N C O  5 0 %   D E  J U R O S ')
    print('=~'*20)
    
    print('''
[1] Cadastrar Conta          
[2] Consultar Saldo
[3] Depositar Dinheiro
[4] Sacar Dinheiro
[5] Historico De Transações
[6] Dados Da Conta
[0] Sair
''')
    
    
    opcao = input('Opção: ')
    
    ## ========== VERIFICANDO AS OPÇÕES ========== ##
    
    # Cadastarando Conta
    if opcao == '1':
        conta_hiago.cadastrar_conta()
        sleep(1)
        
    # Consultando o Saldo
    elif opcao == '2':
        sleep(0.7)
        conta_hiago.consultar_saldo()
     
        
    # Depositando Dinheiro
    elif opcao == '3':
        valor = float(input('Qual o valor do deposito? '))
        sleep(1)
        conta_hiago.depositar_dinheiro(valor)
        
        
    # Sacando Dinheiro
    elif opcao == '4':
        sacar = float(input('Qual o valor que deseja sacar? '))
        sleep(1)
        conta_hiago.sacar_dinheiro(sacar)
        
    
    # Histórico de Transações
    elif opcao == '5':
        sleep(2)
        conta_hiago.consultar_historico_transacao()
    
    # Informações da Conta
    elif opcao == '6':
        sleep(2)
        conta_hiago.dados_conta()
        
    # Finalizando a operação
    elif opcao == '0':
        print('Aguarde!')
        sleep(2)
        print('Operação finalizada com sucesso!')
        break 
    else: 
        sleep(1)
        print('Opcão Inválida!')
        