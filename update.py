import os

list_of_updates = ["lxml"]

def updates_important():
  for i in list_of_updates:
    ret = os.system(i)
    if ret != 0:
      print("updates is ok!!!")
     else:
      print("erro ao realizar a instalacao")
