#import serial, time   # Importar librerias necesarias
#from tello import *

#"""Example program to show how to read a multi-channel time series from LSL."""
#import serial, time  # Importar librerias necesarias
#import tello

#start()  # Comenzar la comunicación con el dron

#power = get_battery()
#print("Nivel de bateria:", power, "%")
#takeoff()
#print("hola")

# INICIA PROGRAMA PARA EL DRON MUSE 2
"""Example program to show how to read a multi-channel time series from LSL."""
import serial, time                     # Importar librerias necesarias
from pylsl import StreamInlet, resolve_stream
import pandas as pd
from openpyxl import Workbook
import csv
import numpy as np  
#import numpy



import serial, time   # Importar librerias necesarias
from tello import *
start() # Comenzar la comunicación con el dron

f=open("datos.csv","w")
escribir=csv.writer(f)

#f = open("valores.txt", "a")
# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])


MaxValorArreglo=0
CiclosTotales=0
Cont=0
ResultadosArreglo=[]
ValProv1=0
ValProv2=0
ResultProvFinal=0
MaxResultadosArreglo=0
AA=0
BB=0
CC=0
DD=0
EE=0
BanderaDron=0
Num_Act=0
Num_Act_Cont=0
while CiclosTotales<=10: # este valor hay que modificar
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it
    #ResultadosArreglo= numpy.zeros(5)
    #MaxResultadosArreglo=numpy.zeros(5)
    if Cont<=3:
        sample, timestamp = inlet.pull_sample()
        #print(timestamp, sample)
        #print( "Variable 1",sample[0])
        #print("Variable 2",sample[1])
        #inicio con la formula
        ValProv1 = sample[0] * sample[0]
        ##print("ValProv1", ValProv1)
        ValProv2 = sample[2] * sample[2]
        #print("ValProv2", ValProv2)
        ResultProvVolatil = ValProv1 + ValProv2
        ResultProvFinal=ResultProvFinal+ResultProvVolatil
        ResultadosArreglo.append(ResultProvVolatil)
        #ResultConDiv= ResultadosArreglo[0]/ResultProvFinal
        Cont +=1

    elif Cont==4:
        MaxResultadosArreglo = max(ResultadosArreglo)
        AA=ResultadosArreglo[0]/MaxResultadosArreglo
        BB = ResultadosArreglo[0] / MaxResultadosArreglo
        CC= ResultadosArreglo[0] / MaxResultadosArreglo
        DD= ResultadosArreglo[0] / MaxResultadosArreglo
        EE= ResultadosArreglo[0] / MaxResultadosArreglo
        Cont +=1
        #CiclosTotales +=1

    elif Cont ==5:
        ResultadosArreglo.clear()
        #print("ResultadosArreglo",ResultadosArreglo)
        #print("MaxResultadosArreglo",MaxResultadosArreglo)
        print("Valor de Real AA=",AA)
        Num_Act = round(AA, 2)
        print("Valor de AA sin decimales", Num_Act)
        Cont+=1

    elif Cont ==6:
        if Num_Act <=0.50: #este valor es que hay que modificar ejemplo 0.20,0.30, 0.50
            Num_Act_Cont +=1

        Cont +=1

    elif Cont ==7:
        print("entre a 7 ")
        print("Valor de Num_Act_Cont ",Num_Act_Cont)
        if BanderaDron==0 and Num_Act_Cont ==4:#este valor es que hay que modificar #8 por otro
            print("estoy volando")
            print("valor de Num_Act_Cont ", Num_Act_Cont)
            #print("Valor de AA =", AA)
            takeoff() #// elevar valor normal XXXXXXXXXX
            #up(80)
            #time.sleep(10)
            #up(80)
            #forward(20)
            land() # quitar si no funciona bien.
            #flip_left()
            #time.sleep(1)
            BanderaDron=1
            Num_Act_Cont = 0
            CiclosTotales += 1
        else:
            #land()
            #time.sleep(2)
            BanderaDron=0

        Cont=1

    lista = [sample[0], sample[1],Num_Act]
    escribir.writerow(lista)