import os
import random
import time
import threading
from random import shuffle

inicioPuente = 10
largoPuente = 20

sem=threading.Semaphore(1)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.posicion2= 30
    self.velocidad = random.uniform(0.1, 0.5)
    

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1
    
    
  def dibujar(self):
    print(' ' * self.posicion + "Vacas")

  

  def run(self):
    
    while(True):
      if (inicioPuente-1==self.posicion):
        sem.acquire()

      if(30==self.posicion, self.posicion):
       sem.release()
     
      self.avanzar()

class Vaca2(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion2 = 0
    self.posicion2= 30
    self.velocidad = random.uniform(0.1, 0.5)
    

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion2-= 1
    
    
  def dibujar(self):
    print(' ' * self.posicion2 + "Vacas")

  

  def run(self):
    
    while(True):
      if (inicioPuente+1==self.posicion2):
        sem.acquire()

      if(30==self.posicion2):
       sem.release()
     
      self.avanzar()

vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()
  v2 = Vaca2()
  vacas.append(v2)
  v2.start()
#
# shuffle(vacas)
# vacas2 = []
# for i in range(5):
#   v2 = Vaca2()
#   vacas2.append(v2)
#   v2.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)


while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  
  # for v2 in vacas2:
  #   v2.dibujar()
  dibujarPuente()
  time.sleep(0.2)
