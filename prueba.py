import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
semaphoro2 = threading.Semaphore(1)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    try:
      time.sleep(self.velocidad)
      self.posicion += 1
    finally:
      if self.posicion == largoPuente+inicioPuente:
        semaphoro2.release()

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    semaphoro2.acquire()
    while(True):
      self.avanzar()
    
     
vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)


while(True):
  
     cls()
     print('Apretá Ctrl + C varias veces para salir...')
     print()
     dibujarPuente()
     for v in vacas:
      v.dibujar()
     dibujarPuente()
     print('')
     dibujarPuente()
     for v in vacas:
      v.dibujar()    #le puse vaquitas a los dos porque quedaba más simpático
     dibujarPuente()

     time.sleep(0.2)