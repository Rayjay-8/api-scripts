import os
#informe na lista os modulos para instalar
list_of_updates = ["asdfcxwer","github","desktopmagic","keyboard","pyautogui","cv2"]
def updates_important():
  global list_of_updates
  for i in list_of_updates:
    os.system("pip install "+i)
    #ret = os.system("pip uninstall "+i)
    print(i+" | install ok!!!")
updates_important()
