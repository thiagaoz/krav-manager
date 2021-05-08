import krav_pandas
import colorama
from colorama import init, Fore, Back, Style

#
init(convert=True)
init(autoreset=True)

class Aluno:

    faixas = ['BRANCA','AMARELA','LARANJA','VERDE','AZUL','MARROM','PRETAI','PRETAII','PRETAIII','MESTRE']
    horarios = ['18:00','19:00','20:00']
    planos = ['MENSALISTA','ASSINATURA']

    #List of atributes that redigitar_function uses
    atributos ={
        1: ['BRANCA','AMARELA','LARANJA','VERDE','AZUL','MARROM','PRETAI','PRETAII','PRETAIII','MESTRE'],
        2 : ['18:00','19:00','20:00'],
        3 : ['MENSALISTA','ASSINATURA']}

    def __init__(self, *args):
        if isinstance(args[0], int):
            novo_aluno = krav_pandas.buscar_aluno(args[0])
            self.id = novo_aluno[0]
            self.nome = novo_aluno[1]
            self.sobrenome = novo_aluno[2]
            self.faixa = novo_aluno[3]
            self.hora = novo_aluno[4]
            self.plano = novo_aluno[5]
            self.nome_completo = self.nome + ' ' + self.sobrenome

        elif isinstance(args[0], str):
            self.nome = args[0].title()
            self.sobrenome = "Silva"
            self.nome_completo = self.nome + ' ' + self.sobrenome
            self.faixa = args[1].upper()
            self.hora = args[2]
            self.plano = args[3]
            self.id = krav_pandas.novo_id()

    def __str__(self):
        i = '-'*(30 - len(self.nome_completo))
        j = '-'*(10 - len(self.faixa) )
        return ('{} ------{} {} ---{} {} | {} | ID: {}'.format(self.nome_completo, i, self.faixa, j, self.hora, self.plano, self.id))

    def faixa_up(self):
        i = self.id - 1
        j = Aluno.faixas.index(self.faixa)
        self.faixa = Aluno.faixas[j+1]

    def nicePrint(self):
        print('--------------------------------------------------------------------------------------------')
        print('NOME: {}'.format(self.nome_completo))
        print('--------------------------------------------------------------------------------------------')
        print('FAIXA: {}      | MATRÍCULA: {}       | NASCIMENO: 01/01/1990 (31)'.format(self.faixa,self.id))
        print('--------------------------------------------------------------------------------------------')
        print('INSTRUTOR: Thiago Vaz        | HORÁRIO: Seg e Qua {}     | PLANO: {}'.format(self.hora, self.plano))
        print('--------------------------------------------------------------------------------------------')
        print('EMAIL: ciclano@gmail.com                              | TEL: (34)9.9999-9999/(34)9.8888-8888' )
        print('--------------------------------------------------------------------------------------------')
        print('ENDEREÇO: Av. Qualquer uma, N 123, Bairro: Brasil, Apto 101')
        print('--------------------------------------------------------------------------------------------')
        print('CEP: 999999 - 999                                         | OCUPAÇÃO: -')
        print('-------------------------------------- OBSERVAÇÕES -----------------------------------------')

