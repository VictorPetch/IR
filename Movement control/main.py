"""<control the arm Lynxmotion by comand.>
    Copyright (C) 2018  WIlliam Ribeiro

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    contact :   https://github.com/willcribeiro or
                 william-cribeiro@bct.ect.ufrn.br
"""


from ufrn_al5d import RoboticArmAL5D
import time
import keyboard

#DEF BASE
base = 0
#LIMITS
min_base = 500
max_base = 2400

#DEF SHOULDER
SHL = 1
#LIMITS
min_SHL = 1200
max_SHL = 2000

#DEF ELBOW
ELB = 2
#LIMITS
min_ELB = 1100
max_ELB = 2000

#DEF WRIST
WRI = 3
#LIMITS
min_WRI = 500
max_WRI = 2500

#DEF GRIPPER
GRI = 4
#LIMITS
min_GRI = 1300
max_GRI = 2400

#PROPRIEDADES DO BRACO: SERVOS E LIMITES DE OPERACAO

properties = [base, min_base, max_base,
              SHL, min_SHL, max_SHL,
              ELB, min_ELB, max_ELB,
              WRI, min_WRI, max_WRI,
              GRI, min_GRI, max_GRI]

home = '#0P1500#1P1500#2P1500#3P1500#4P1500T1500'
arm = RoboticArmAL5D(properties)
arm.setup()

eixo0 = 1500
eixo1 = 1500
eixo2 = 1500
eixo3 = 1500
eixo4 = 1500

if(arm.abre_porta() == -1):
    print ('Erro abrindo a porta serial /dev/ttyS0\nAbortando o programa...\n')
else: 
    print('PROGRAMA  INICIADO\n\n')
    print ('Porta serial /dev/ttyS0 aberta com sucesso\n')
    try:
        arm.envia_comando(home)
        print(' envio para Home: %s \n' % (home))
    except:
         print('Problema no envio do comando\nAbortando o programa...')
  
    while True:
        X = input("Entre com o comando desejado")
        if(X == 'pegar' or X == 'PEGAR'): #Fecha a garra
            try:
                arm.envia_comando(home)
                print(' envio para Home: %s \n' % (home))
            except:
                print('Problema no envio do comando\nAbortando o programa...')

        elif(X == 'SOLTAR' or X == 'soltar'): #Abrir a garra
            try:
                arm.envia_comando(home)
                print(' envio para Home: %s \n' % (home))
            except:
                print('Problema no envio do comando\nAbortando o programa...')

        elif(X == 'repouso' or X == 'REPOUSO'): #Ir para home
            try:
                arm.envia_comando(home)
                print(' envio para Home: %s \n' % (home))
            except:
                print('Problema no envio do comando\nAbortando o programa...')

    
    arm.fecha_porta()
    print('\nPROGRAMA DEMONSTRACAO FINALIZADO\n\n')