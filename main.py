from turtle import *
from time import *
from random import *

a = "loading..."
while (True):
  for i in range(10):
    print(a)
    r = random()
    sleep(r)
  print("UNSECCESSFUL. RETRYING...")
  sleep(1)
