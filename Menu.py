
import Aluno as al
import os
import krav_pandas

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print('-------======= KRAV MANAGER v0.1 ========-------')
while(True):
  print('----==== MENU PRINCIPAL ====----')
  print('\n[1] CADASTRAR \n[2] BUSCAR \n[3] LISTAR \n[4] GRADUAR \n[5] Estatísticas \n[0] SAIR')
  menu = input('Escolha: ')
  
  #termina o programa
  if menu == '0': break 
  
  #opcao para cadastrar aluno
  if menu == '1':
    while(True):
        print('\nCadastrando novo aluno')
        atributos = ['NOME', 'FAIXA']
        aluno_list = []
        for i in range(len(atributos)):
          a = input(atributos[i] +': ')
          aluno_list.append(a)

        aluno = al.Aluno(aluno_list[0], aluno_list[1])
        print('\nConfira os dados abaixo:')
        print(aluno)
        print('\n[1] Confirmar cadastro \n[2] Redigitar \n[0] Cancelar')
        menu = input('Escolha: ')
        if menu =='1': 
          krav_pandas.inserir_aluno(aluno) 
          break
        if menu == '2': 
          cls()
        elif menu == '0': 
          cls()
          break
        else:
          input('\nOpção Inválida!! \nRetornando ao Menu Principal...\nENTER para prosseguir...')
          cls()
          break
 
  #buscar aluno pelo ID
  if menu == '2':
        id = int(input('ID do Aluno: '))
        aluno = al.Aluno(id)
        cls()
        print(aluno)

  #listar alunos por faixas e ou horários de treino
  if menu == '3':
    requisitos = {}
    selecionados = []
    while(menu == '3'):
      cls()
      print('Por quais categorias gostaria de listar?')
      print('\n[1] TODOS os Alunos \n[2] Faixa \n[3] Horário \n[4] Listar Selecionados \n[0] SAIR')
      if selecionados: print(selecionados)
      
      menu3 = input("Escolha: ")
      if menu3 == '1': 
        cls()
        krav_pandas.listar_alunos(**requisitos) 
        print()
        break

      if menu3 == '2':
        requisitos['belt'] = []

        while(True):
          cls()
          if selecionados: 
            print('SELECIONADOS: ' + str(selecionados))
          else:
            print('Nenhuma requisito selecionado')

          print('\n[T] Trocar de Categoria \n[ENTER] Listar')
          faixa = input('Digite a Faixa: ').upper()
          
          if faixa == '0': 
            menu = '0'
            break

          elif faixa == 'T': 
            break

          elif not faixa:
            cls()
            krav_pandas.listar_alunos(**requisitos)
            menu = '0'
            break

          elif faixa not in requisitos['belt']: 
            requisitos['belt'].append(faixa)
            selecionados.append(faixa)

      if menu3 == '3':
        requisitos['time'] = []
        
        while(True):
          cls()
          if selecionados:
            print('SELECIONADO: '+ str(selecionados))
          print('\n[1] 18:00 \n[2] 19:00 \n[3] 20:00 \n[4] Trocar de categoria \n[0] Menun Principal \n[ENTER] Listar ')
          hora = input('\nHorário: ').upper()
          
          if hora == '0': 
            menu = '0'
            break
          
          elif hora == '4': 
            break
         
          elif not hora: 
            cls()
            krav_pandas.listar_alunos(**requisitos)
            menu = '0'
            break
          
          elif hora == '1': 
            requisitos['time'].append('18:00')
            selecionados.append('18:00')
         
          elif hora == '2': 
            requisitos['time'].append('19:00')
            selecionados.append('19:00')
         
          elif hora == '3': 
            requisitos['time'].append('20:00')
            selecionados.append('20:00')
      
      if menu3 == '4':
        if selecionados:
          cls()
          krav_pandas.listar_alunos(**requisitos)
          break
        else:
          print('Escolha um requisito!!!')
          input()

      if menu3 == '0':
        break
        
  #busca aluno por ID, passa uma faixa dele e pergunta se quer graduar outro
  #ainda não está atualizando no DATAFRAME
  if menu == '4':
    menu4 = 'oi'
    cls()
    alunoId = int(input('Qual ID do aluno? \nID: '))
    aluno = al.Aluno(alunoId)
    print()
    print(aluno)
    menu4 = input('\nGraduar Aluno [S/N]? ').upper()
    if menu4 == 'S':
      aluno.faixa_up()
      print('\nPARABÉNS!') 
      krav_pandas.atualiza_aluno(aluno)
      print(aluno)

  if menu == '5':
    cls()
    print('Gerar estatísticas de qual categoria?')
    print('[1] Faixa \n[2] Horário \n[3] Planos \n[0] Menu Principal')
    menu5 = input('Escolha: ')
    cls()
    if menu5 == '1':
     krav_pandas.alunos_stats('belt')
    elif menu5 == '2':
     krav_pandas.alunos_stats('time')
    elif menu5 == '3':
     krav_pandas.alunos_stats('pay_plan')
    print()
    
