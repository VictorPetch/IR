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
import math
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

def mov(t1,t2,t3,phy):
    try:
        Mov = '#0P%s#1P%s#2P%s#3P%sT2000' % (t1,t2,t3,phy)
        print(Mov)
        arm.envia_comando(Mov)
    except:
        print('Problema no envio do comando\nAbortando o programa...')

def Mov_Claw(claw):
    try:
        Mov = '#4P%sT1500' % (claw)
        arm.envia_comando(Mov)
    except:
        print('Problema no envio do comando\nAbortando o programa...')
#Prints das partes de x_linha
def P_x_linha(x,y,z,phi):
    print('X:', x, 'y:', y)
    print('Raiz: ',math.sqrt(x**2 + y**2) )
    print('Phi:', phi)
    print('8*Cos: ',8 * math.cos(math.radians(phi)) )

#Prints das partes de z_linha
def P_z_linha(x,y,z,phi):
    print('Z:',z)
    print('z-3:', z-3)
    print('8*Sen:', 8 * math.sin(math.radians(phi)))

def angulos (x,y,z,phi):
    x_linha = math.sqrt(x**2 + y**2) - 8 * math.cos(math.radians(phi))
    #P_x_linha(x,y,z,phi)
    #print('x_linha:', x_linha)
    z_linha = z - 3 - 8 * math.sin(math.radians(phi))
    #P_z_linha(x,y,z,phi)
    #print('z_linha:', z_linha)

    sen1 = y/(math.sqrt(x**2 + y**2))
    cos1 = x/(math.sqrt(x**2 + y**2))
    teta1 = math.degrees(math.atan2(sen1,cos1))
    #print("Sen1:",sen1 , "Cos1:",cos1 , "Atan2:",teta1 )
    print()

    Hipotenusa = (math.sqrt(x_linha**2 + z_linha**2))
    alfa = math.degrees( math.atan2(z_linha/Hipotenusa,x_linha/Hipotenusa))
    beta = math.degrees(math.acos((Hipotenusa**2 + 15**2 -19**2) /(2*Hipotenusa*15)))
    #print("Hipotenusa:", Hipotenusa, "Alfa:", alfa, "Beta;", beta)
    teta2 = (alfa + beta)
    #print("Teta2:", teta2)
    #print()

    seila = math.degrees(math.acos((x_linha**2 + z_linha**2 - 15**2 - 19**2)/(2*15*19)))
    print("seila", seila)
    cos3 = (x_linha**2 + z_linha**2 - 15**2 - 19**2)/(2*15*19)
    sen3 = math.sqrt(1-cos3**2)
    print(sen3)
    teta3 = math.degrees(math.atan2(sen3,cos3))
    #print("Argumento de teta3:",(x_linha**2 + z_linha**2 - 15**2 - 19**2)/(2*15*19))
    #print("Teta3:",teta3)

    teta4 = phi -( teta2 - teta3)
    #print("Teta4:", teta4)

    print(teta1,teta2,teta3,teta4)

    # Conversoes para pwm
    teta1 = abs(teta1)
    teta1 = (teta1/0.09) + 566.333333333

    teta2 = (teta2/0.09) + 500

    teta3 = (teta3/0.09) + 500
    teta4 = teta4 + 90
    teta4 = abs(teta4)
    teta4 = (teta4/0.09) + 500

    mov(teta1,teta2,teta3,teta4)


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
        X = input("Entre com o comando desejado \n")
        if(X == 'pegar' or X == 'PEGAR'): #Fecha a garra
            Mov_Claw(500)
            move = input() #(x,y,z,phi)
            ax = move[0]
            ay = move[1]
            az = move[2]
            aphi = move[3]
            angulos(ax,ay,az,aphi)
            time.sleep(2)
            Mov_Claw(1166.66)
        elif(X == 'SOLTAR' or X == 'soltar'): #Abrir a garra
             move = input() #(x,y,z,phi)
             ax = move[0]
             ay = move[1]
             az = move[2]
             aphi = move[3]
             angulos(ax,ay,az,aphi)
             time.sleep(2)
             Mov_Claw(500)

        elif(X == 'repouso' or X == 'REPOUSO'): #Ir para home
            mov(1500,1500,1500,1500)
        elif(X == 'MOVE' or X == 'move'): #movimentacao
            move = input() #(x,y,z,phi)
            ax = move[0]
            ay = move[1]
            az = move[2]
            aphi = move[3]
            -7,-34,11,-40
            angulos(ax,ay,az,aphi)


    arm.fecha_porta()
    print('\nPROGRAMA DEMONSTRACAO FINALIZADO\n\n')
