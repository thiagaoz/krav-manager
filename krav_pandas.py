#Escrever (ATUALIZAR ALUNO) como se fosse um arquivo de texto normal, escrever com "open /with"
#import csv 
#desempacotar a csv como dicionário e unpack os valores separados por '|' em cada key
#usar INDEX_COL = 'ID' para mudar o index padrão da coluna e resolver problemas de conversão
#entre do ID para LInhas (Row)




import pandas as pd

df = pd.read_csv('C:/Users/zeron/AppData/Local/Programs/Python/Python39/TESTES/KravPandas/testekravmaga.csv')

def listar_alunos(**kwargs): #vai receber {'belt': lista_belt, 'time': lista_time}
    filtro = df['id'] != None
    for coluna in df:
        if coluna in kwargs:
            filtro  = filtro & df[coluna].isin(kwargs.get(coluna))

    print_df(df[filtro].sort_values(by=['first_name']))

def buscar_categorias():
    categorias = ['first_name','last_name']
    usadas = []
    while True:
        print('\n1 - FAIXA\n2 - HORÁRIO\n3 - PLANO\n0 - SAIR\nT - TESTAR Função')
        categoria = input('=> ')
        if categoria not in ('1','2','3','0','t'):
            print('OPCAO INVALIDA!')
        if categoria in usadas:
            print('CATEGORIA já selecionada!') 
        else:
            usadas.append(categoria)
            if categoria == '0': break
            if categoria == '1': categorias.append('belt') 
            if categoria == '2': categorias.append('time')
            if categoria == 't': 
                categorias = ['first_name','last_name','belt','time'] 
                break

    print(df[categorias].head(10))
    print('Imprimendo apenas os 10 primeiros')


def buscar_faixa(faixa_min, faixa_max = None):
    if faixa_max == None:
        filtro = df['belt'] == faixa_min
    else:
        grupo = []
        i_min = faixas.index(faixa_min)
        i_max = faixas.index(faixa_max) +1
        for i in range(i_min, i_max):
            grupo.append(faixas[i])
        filtro = df['belt'].isin(grupo)

    print(df.loc[filtro])

def buscar_aluno(reg: int) -> tuple:
    i = (reg - 1)
    nome = df['first_name'].values[i]
    faixa = df['belt'].values[i]
    hora = df['time'].values[i]
    sobrenome = df['last_name'].values[i]
    plano = df['pay_plan'].values[i]
    return (reg, nome, sobrenome, faixa, hora, plano)

def faixa_upgrade(registro: int):
    filtro = df['id'] == registro
    posicao = df[filtro].index
    faixa = df['belt'].values[posicao]
    i = faixas.index(faixa)
    faixa = faixas[i+1]
    df.loc[filtro,'belt'] = faixa

def inserir_aluno(Aluno):
    i = novo_id()
    novo_aluno = {'id': i, 'first_name': Aluno.nome, 'last_name': Aluno.sobrenome, 'belt': Aluno.faixa, 
    'time': Aluno.hora, 'pay_plan': Aluno.plano}
    df2 = df.append(novo_aluno, ignore_index=True)
    print(df2.tail(2))

def novo_id() -> int:
    i_max = list(df['id'])[-1]
    return i_max +1

def atualiza_aluno(Aluno):
    i = Aluno.id - 1
    df.loc[i, 'first_name'] = Aluno.nome
    df.loc[i, 'last_name'] = Aluno.sobrenome
    df.loc[i, 'belt'] = Aluno.faixa
    df.loc[i, 'time'] = Aluno.hora
    df.loc[i, 'pay_plan'] = Aluno.plano
    print(df[df['id'] == i+1])

def print_df(lista):
    for i in range(len(lista)):
        aluno = []
        for j in range(lista.shape[1]):
            aluno.append(lista.iloc[i,j])

        nome_completo = str(aluno[1] + ' ' +aluno[2])
        k = '-'*(30 - (len(nome_completo) + len(str(i+1))))
        j = '-'*(10 - len(aluno[4]))
        print('{}) {} ------{} {} ---{} {} | {} | ID: {}'.format(i+1, nome_completo, k, aluno[4], j, aluno[5], aluno[6], aluno[0]))
    print('\n ==>  '+ str(lista.shape[0]) + ' Alunos encontrados\n')

def alunos_stats(atributo):
    filtro = df['id'] != None
    df_stats = df[filtro].sort_values(by=[atributo])
    atributo = dict(df_stats[atributo].value_counts())
    for key, value in atributo.items():
        print(str(key) + ': ' + str(value)+' ('+ str(value*100/100)+'%)')


