#---- PERSONAL REMMINDER for upcoming features or fixes
#tratar valores ausentes no pandas

#comentario em ingles
#COMMIT: feat: New entry system for students with less typing
#and option to choose especific atribute to retype


#Changes on the dataframe are not permanent
from Aluno import Aluno
import os
import krav_pandas

#shortcut to print "Wrong input message"
opcao_errada = lambda: input('\nOpção INCORRETA! \nENTER para continuar...')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#percorre os valores da lista para gerar um menu, depois testa e retorna o valor escolhido da lista
def cadastra_atributo(lista):
  if len(lista) > 5:
    l = len(lista)
    for i in range(1,l,2):
      espaco = ' '* (20 - len(lista[i-1]))
      print('[{}] {}{}[{}] {}'.format(i, lista[i-1], espaco, i+1, lista[i]))
      i += 2
      if (i == l) and (l%2 != 0): 
        print('[{}] {}'.format(i, lista[i-1]))
        break
  
  else:
    for i, value in enumerate(lista, 1):
      print('[{}] {}'.format(i, value))
  try:
        entrada = int(input('Escolha: ')) - 1
        return lista[entrada]
  except:
    return '[VAZIO]'

#
def redigitar_aluno(i, lista):
  if i == 1:
    lista[0] = (input('NOME: '))
  else:
    lista[i-1] = (cadastra_atributo(Aluno.atributos[i-1]))

print('-------======= KRAV MANAGER v0.1 ========-------')
while(True):
  print('----==== MENU PRINCIPAL ====----')
  print('\n[1] CADASTRAR \n[2] BUSCAR \n[3] LISTAR \n[4] GRADUAR \n[5] Estatísticas \n[0] SAIR')
  menu = input('Escolha: ')
  
  #termina o program
  if menu == '0': break 
  
  #Register a new student on the dataframe
  elif menu == '1':
    while(True):
      cls()
      print('\nCadastrando novo aluno')
      print()
      atributos = ['NOME', 'FAIXA','HORÁRIO','PLANO']
      aluno_list = []

      #collecting and adding student values
      aluno_list.append(input('NOME: ')) 
      print('\nEscolha a FAIXA')
      aluno_list.append(cadastra_atributo(Aluno.faixas))
      print('\nEscolha o HORÁRIO')
      aluno_list.append(cadastra_atributo(Aluno.horarios))
      print('\nEscolha o PLANO')
      aluno_list.append(cadastra_atributo(Aluno.planos))

      #Percorre a lista e preenche com [VAZIO] todos atributos que não foram digitados
      # for i, value in enumerate(aluno_list):
      #   if not value: aluno_list[i] = '[VAZIO]' 
      
      #show the new student and ask cconfirmation before registration
      cls()
      aluno = Aluno(*aluno_list)
      print('\nConfira os dados abaixo:')
      print(aluno)
      print('\n[1] Confirmar cadastro \n[2] Redigitar \n[0] Cancelar')
      menu1 = input('Escolha: ')
      if menu1 =='1': 
        krav_pandas.inserir_aluno(aluno) 
        break

      #Let the user pick a field to type or choose another value
      elif menu1 == '2': 
        while menu1 == '2':
          try: #avoid entry type errors
            cls()
            print(aluno)
            print('Qual categoria gostaria de redigitar?')
            print('[1] NOME \n[2] FAIXA \n[3] HOÁRIO \n[4] PLANO \n[5] CONFIRMAR cadastro \n[0] SAIR sem cadastrar')
            i = int(input('Escolha: '))
            if i == 5: 
              krav_pandas.inserir_aluno(aluno)
              menu1 = 'out'
            elif i == 0:
              menu1 = 'out'
            else:
              redigitar_aluno(i, aluno_list)
              aluno = Aluno(*aluno_list)
          except:
            opcao_errada
        break
      elif menu1 == '0': 
        cls()
        break
      else:
        opcao_errada()
        cls()
        break
 
  #buscar aluno pelo ID
  elif menu == '2':
        id = int(input('ID do Aluno: '))
        aluno = Aluno(id)
        cls()
        aluno.nicePrint()

  #listar alunos por faixas e ou horários de treino
  elif menu == '3':
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
        
  #GRADUAR busca aluno por ID, passa uma faixa dele e pergunta se quer graduar outro
  #ainda não está atualizando no DATAFRAME
  elif menu == '4':
    menu4 = 'oi'
    cls()
    alunoId = int(input('Qual ID do aluno? \nID: '))
    aluno = Aluno(alunoId)
    print()
    print(aluno)
    menu4 = input('\nGraduar Aluno [S/N]? ').upper()
    if menu4 == 'S':
      aluno.faixa_up()
      print('\nPARABÉNS!') 
      krav_pandas.atualiza_aluno(aluno)
      print(aluno)

  #Get stats from students (belts, payment, training hours)
  elif menu == '5':
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
    
  else:
    opcao_errada()
    cls()




