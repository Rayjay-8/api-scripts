from tkinter import *
import time,pyautogui,keyboard
from tkinter import ttk
from desktopmagic.screengrab_win32 import (
getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
getRectAsImage, getDisplaysAsImages)
import os

### obs
# prints serao armazenados no diretorio dos modulos/folder_print
# nao alterar o nome das imagens pois sera usada o nome da ultima + 1

root = Tk()
#root.withdraw()
root.overrideredirect(True)
root.wm_geometry("400x400")
root.attributes('-alpha', 0.7)
root.wm_attributes('-topmost','true')
root.config(bg="#aa3434")

label = Label(text="Ctrl + S = Salvar img\nCtrl + Q = Quit\n Centralize o objeto\n",fg="#fff")
label.config(bg="#343434")
label.pack(side="left",fill="both",expand=True)



grip = ttk.Sizegrip(root)
grip.place(relx=1.0, rely=1.0, anchor="se")
grip.lift(label)

ee = []
def set_click(e):
    global ee
    ee = [e.x,e.y]
label.bind("<ButtonPress-1>", set_click)

size_now = [400,400]
ssize_now=[400,400]
trie = 0
def OnMotion(event):
    global ssize_now,trie
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    root.geometry("%sx%s" % ((x1-x0),(y1-y0)))
    
    size_now.append((x1-x0))
    size_now.append((y1-y0))
    trie+=1
    ssize_now.pop(-1)
    ssize_now.pop(-1)
    ssize_now.append(size_now[-1])
    ssize_now.append(size_now[-2])
    if trie > 1:
        size_now.pop(0)
        size_now.pop(0)
        label.config(text="")
    return
grip.bind("<B1-Motion>", OnMotion)

ponto_inicial =[0,0]
def OnMotion2(event):
    global ponto_inicial
    
    x1 = root.winfo_pointerx()
    y1 = root.winfo_pointery()
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    
    ponto_inicial.pop(-1)
    ponto_inicial.pop(-1)
    ponto_inicial.append(x0)
    ponto_inicial.append(y0)
    root.wm_geometry("{}x{}+{}+{}".format(size_now[0]+5,size_now[1]+5,x1-ee[0],y1-ee[1]))

    
label.bind("<B1-Motion>", OnMotion2)

while True:
    if keyboard.is_pressed('ctrl+s'):
        
        label.config(text="")
        print("Salvo")
        root.wm_attributes('-alpha', 0.0)
        
        
        dado = str(ssize_now + ponto_inicial)
        dado = dado[1:-1].split(",")
        a=int(dado[0])
        b=int(dado[1])
        #print(a,b)
        c=int(dado[2])
        d=int(dado[3])
        print("se erro pq diretorio folder print nao existe - tratar criando o diretorio")
        try:
            arqui = os.listdir("folder_print")
        except:
            os.mkdir("folder_print")
        try:
            assert arqui != ""
            new_name = int(arqui[-1].replace(".png",""))+1
        except:
            new_name = "1"
        with open("logcords.txt","w") as kk:
            kk.write("{}\n{}\n{}\n{}".format(c,d,b+c+13,a+d+10))
        im = getRectAsImage((c,d,b+c+13,a+d+10))
        im.save(f"folder_print/{new_name}.png")
        root.wm_attributes('-alpha', 0.7)
        
        time.sleep(1)
    if keyboard.is_pressed('ctrl+q'):
        print("Sair")
        root.destroy()
        quit()
    root.update()

root.destroy()
