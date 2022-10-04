from random import randint

from matplotlib.rcsetup import validate_int_or_None


class Agencia:
    """
    Criando a classe da Agência 
    
    Attributos:
        telefona(int): Telefone da Agência.
        cnpj(int): CNPJ da Agência.
        numero(int): Número da Agência do Cliente. 4 Digitos.
        clientes(str): Quantidades de Clientes na Agência.
        caixa(float): Valor total em caixa da Agência.
        emprestimo(float): Metodo de Emprestar Dinheiro ao Cliente da Agência.
    """
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj 
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimo = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f"Caixa abaixo do recomendado. Caixa atual {self.caixa}")
        else:
            print(f'O valor do caixa está Ok. Caixa atual {self.caixa}')
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimo.append((valor, cpf, juros))
        else:
            print("Empréstimo não é possivel. Dinheiro não disponível em caixa.")
            
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        

class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        ''' Herdando o init da Class mãe, pegando as mesmas informações '''
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
        
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor 
        self.caixa += valor
        

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000
        
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else: 
            print('O Cliente não tem o patrimônio mínino necessário para entrar na Agência Premium.')
        
if __name__ == '__main__':
    # Programa

    agencia_virtual = AgenciaVirtual('www.hiaguinhospencer.com' ,654432, 200003430)
    agencia_virtual.verificar_caixa()
    agencia_virtual.depositar_paypal(valor = int(input('Qual valor do deposito? ')))
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)


    agencia_comum = AgenciaComum(432234, 90004494)
    agencia_comum.verificar_caixa()


    agencia_premium = AgenciaPremium(234532, 900004942)
