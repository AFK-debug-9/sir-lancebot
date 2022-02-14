import random, threading, time

def thread():
  bin = ''
  for i in range(5000*8):
    bin += random.choice('10')
    
  random.seed(str(int(bin,2))+bin)

def randomize():
  threadlings = []

  for i in range(10):
    threadlings.append(threading.Thread(target=thread))

  for threadling in threadlings:
    threadling.start()
  
  time.sleep(3)
  
  del threadlings # Sad :(
  
  for i in range(5000*8):
    bin += random.choice('10')
    
  return str(int(bin,2))+bin
