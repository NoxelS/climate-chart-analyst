## KLIMADIAGRAMM-ANALYST VON NOEL SCHWABENLAND 2017 (FÜR ERDKUNDE LK)

#IMPORTS----------------------------------------------------------------------------------------------------------------IMPORTS
import os
import sys
#GLOBAL VARS------------------------------------------------------------------------------------------------------------GLOBAL VARS
## About the Script
version = "0.1"
date_r = "07.09.2017"
autor = "Noel Pascal Schwabenland"
## Global defs
def cls():
  print("----------------------------------------------------------------------")
  os.system("cls")
#DEFINITIONEN-----------------------------------------------------------------------------------------------------------DEFINITIONEN
## TEIL 1---------------------------------------------------------------------------------------------------------------DEF 1
def getName():
   print("Name der Messtation:\t",end="")
   return input("")

def getBreiteLaenge():
   print("Geografische Breite und Länge:\t", end="")
   return input("")

def getHoehe():
   print("Höhe der Messation:\t", end="")
   return input("")

def getZeit_beobachtung():
   print("Zeitraum:\t\t", end="")
   return input("")

def build_Beschreibung():
   return [getName(), getBreiteLaenge(), getHoehe(), getZeit_beobachtung()]

## TEIL 2---------------------------------------------------------------------------------------------------------------DEF 2
def getTemperaturen():
   cls()
   print("Anzahl Messwerte (Temperatur):\t", end="")
   anzahl_t = float(input(""))
   tag_temp = []
   for tag_x in range(int(anzahl_t)):
       print("Messwert[",tag_x+1,"]: ",end="")
       tag_temp.append(float(input("")))
   cls()
   return tag_temp


def getTmp_max(data = []):
   m = 0
   for x in range(len(data)):
       if data[x] > m:
           m = data[x]
   return m

def getTmp_min(data = []):
   h = float(sys.float_info.max)
   for x in range(len(data)):
       if data[x] < h:
           h = data[x]
   return h

def getAmplitude_2tage(data = []):
   ampl = 0
   for x in range(len(data)):
       if abs(data[x-1] - data[x]) > ampl:
           s_a = abs(data[x-1] - data[x])
   return format(abs(s_a), '.2f')


def getAmplitude_generell(data = []):
   return format(abs(getTmp_max(data) - getTmp_min(data)), '.2f')

def getTmp_d(data = []):
  tmp = float(0)
  for x in data:
    tmp += x
  return tmp/len(data)
## TEIL 3---------------------------------------------------------------------------------------------------------------DEF 3

def getNiederschlag():
   cls()
   print("Anzahl Messwerte (Niederschlag):\t", end="")
   anzahl_t = float(input(""))
   tag_n = []
   for tag_x in range(int(anzahl_t)):
       print("Messwert[", tag_x + 1, "]: ", end="")
       tag_n.append(float(input("")))
   cls()
   return tag_n

def getarid(data_tmp = [], data_n = []):
   i_a = 0
   for x in range(len(data_tmp)):
       if data_tmp[x] > data_n[x]:
           i_a += 1
   return float(i_a)

def gethumid(data_tmp=[], data_n=[]):
   i_h = 0
   for x in range(len(data_tmp)):
       if data_tmp[x] < data_n[x]:
           i_h += 1
   return  float(i_h)

def getSumme(data = []):
  s = float(0)
  for x in data:
    s += x
  return s
#MAIN SCRIPT------------------------------------------------------------------------------------------------------------MAIN SCRIPT

## Willkommensnachricht
print("Willkommen beim Klimadiagramm-Analyst ",version," ", date_r," von ", autor)
print("Drücken Sie eine Taste", end="")
tmp = input("...")
cls()
## Script TEIL 1 -> "Beschreibung der Lage des Ortes"-------------------------------------------------------------------TEIL 1
#                 = [Name, Breite/Länge, Höhe, Zeitraum]
data_beschreibung = build_Beschreibung()        # Stringarray

## Script TEIL 2 -> "Untersuchung der Temperaturwerte"------------------------------------------------------------------TEIL 2
#    Bsp.= [2, 4, 53 ,3.5 ,34]
data_tmp = getTemperaturen()                    # floatarray

data_max_tmp = getTmp_max(data_tmp)             # float
data_min_tmp = getTmp_min(data_tmp)             # float
data_ampl_g = getAmplitude_generell(data_tmp)   # float
data_ampl_2 = getAmplitude_2tage(data_tmp)      # float
data_durchschnitt_tmp = getTmp_d(data_tmp)      # float

print(data_tmp)
print(data_max_tmp)
print(data_min_tmp)
print(data_ampl_g)
print(data_ampl_2)

## Script TEIL 3 -> "Untersuchung der Niederschlagswerte"---------------------------------------------------------------TEIL 3

data_niederschlag = getNiederschlag()                       # floatarray

data_max_n = getTmp_max(data_niederschlag)                  # float
data_min_n = getTmp_min(data_niederschlag)                  # float
data_anzahl_arid = getarid(data_tmp, data_niederschlag)     # float
data_anzahl_humid = gethumid(data_tmp, data_niederschlag)   # float
data_summe_n = getSumme(data_niederschlag)                  # float
## Ausgabe--------------------------------------------------------------------------------------------------------------AUSGABE
cls()
print("Sie Benutzen den Klimadiagramm-Analyst ",version," (", date_r,") von ", autor)
print("Beschreibung des Orts:")
print("Messtation: ", data_beschreibung[0],"\tGeographische Breite und Länge: ", data_beschreibung[1],
     "\tHöhenlage: ", data_beschreibung[2],"\tBeobachtungszeitraum: ",data_beschreibung[3])
print("")

print("Untersuchung der Temperaturwerte:")
print("Jahresdurchschnittstemperatur: ",data_durchschnitt_tmp,"C°\tMaxima/Minima der Temperatur", data_max_tmp,"C°, ",
     data_min_tmp, "C°\tJahresamplitude: ", data_ampl_g,"C°")
print("")

print("Untersuchung der Niederschlagswerte:")
print("Jährliche Niederschlagssumme: ", data_summe_n,"mm\tMaxima/Minima Niderschläge: ",data_max_n,"mm, ", data_min_n,
     "mm\tAnzahl humide/aride Monate: ", data_anzahl_humid,", ", data_anzahl_arid)


