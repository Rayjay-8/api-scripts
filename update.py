import os
#informe na lista os modulos para instalar
list_of_updates = ["lxml"]
def updates_important():
  global list_of_updates
  for i in list_of_updates:
    ret = os.system("pip install "+i)
    #ret = os.system("pip uninstall "+i)
    if ret != 0:
      print("updates is ok!!!")
    else:
      print("erro ao realizar a instalacao")
updates_important()
