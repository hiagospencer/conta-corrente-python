# Class
from time import sleep
import os
from datetime import datetime
import pytz
from random import randint

class ContaCorrente():
    """
    Criar um objeto ContaCorrente para gerenciar as contas dos clientes
    
    Attributos:
        nome (str): Nome do Cliente
        cpf (int): Cpf do Cliente
        agencia (int): Agencia do Banco do Cliente 
        num_conta (int): Número da conta do Cliente
        saldo (float): Saldo disponível na conta do Cliente
        limite (float): Lmite de cheque especial daquele Cliente
        historia (str): Histórico das transações do Cliente
        
    """
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y %H:%M:%S')
    
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.historico = []
        self.cartoes = []
        
    def cadastrar_conta(self):
        """ Metodo de Cadastrar os dados do Clientes """
        self.nome = input('Nome Completo: ').capitalize().strip()
        self.cpf = int(input('CPF: '))
        self.agencias = int(input('Número Agência: '))
        self.num_conta = int(input('Número da Conta: '))
        print(f'Conta Cadastrada com sucesso!')
        
    def consultar_saldo(self):
        """ metodo de consultar o saldo da Conta do Cliente """
        sleep(2)
        print(f'Seu saldo atual é de R${self._saldo:,.2f}')
        
    
    def depositar_dinheiro(self, valor):
        """ Metodo de Depositar dinheiro na conta do Cliente """
        self._saldo += valor
        sleep(2)
        print(f'Deposito de R${valor:,.2f} realizado com sucesso!')
        self.historico.append((valor, self._saldo, ContaCorrente._data_hora()))
        
    def limite_conta(self):
        """ Metodo de consultar o limite do cheque especial do cliente """
        self._limite = -1000
        return self._limite
        
        
    def sacar_dinheiro(self, valor):
        """ Metodo de Sacar dinheiro da conta do Cliente e verificando se ele entrou ou não no cheque especial """
        if self._saldo - valor < self.limite_conta():
            sleep(1)
            print('Você não tem saldo suficiente para realizar esse valor')
            self.consultar_saldo()
            
        else:
            self._saldo -= valor
            print(f'Saque de R${valor:,.2f} realizado com sucesso!')
            self.historico.append((-valor, self._saldo, ContaCorrente._data_hora()))
            
            
    def dados_conta(self):
        """ Metodo de ver os dados do Cliente """
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Agência: {self.agencias}')
        print(f'Número da Conta: {self.num_conta}')
        
        
    def consultar_historico_transacao(self):
        """ Metodo de consultar o histórico de transações da conta bancaria do Cliente """
        print('Histórico de Transações: ')
        print('Valor, Saldo, Data e Hora')
        
        for transacao in self.historico:
            print( transacao)
        

class CartaoCredito:
    """
    Criando um Class do Cartão de Credito e axiliando com a class da conta corrente
    
    Attributos:
        numero (int): Número do Cartão
        _titular (str): Nome do titular do cartão de credito
        _validade (int): Validade do cartão de credito
        _cod_segurança(int): Números do código de segunraça do cartão de credito
        _limite(float): limite do cartão de credito
        conta_corrente(obj): Aqui é a class da ContaCorrente passado como parâmetro
    
    """
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = '{}{}{}{} {}{}{}{} {}{}{}{} {}{}{}{}'.format(*str(randint(1000000000000000, 9999999999999999)))
        self._titular = titular
        self._validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self._cod_seguranca = f'{randint(0,9)}{randint(0, 9)}{randint(0, 9)}'
        self._limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
        
    # VERIFICANDO SE A SENHA TEM 4 DIGITOS E É NUMEROS
    @property    
    def senha(self):
        return self.senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha inválida!')
            
            

if __name__ == '__main__':
    
    opcao = input('Opção: ')
    
    if opcao == '1':
        nome = input('Nome Completo: ').capitalize().strip()
        cpf = int(input('CPF: '))
        agencia = int(input('Número Agência: '))
        num_conta = int(input('Número da Conta: '))
        sleep(2)
        
    