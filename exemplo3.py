
import time
import base64
from desktopmagic.screengrab_win32 import (getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,getRectAsImage, getDisplaysAsImages)
import cv2
import numpy as np
import pyautogui
import random
import platform
import subprocess
def imagesearch_count(image, precision=0.9):
    img_rgb = getScreenAsImage()
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= precision)
    count = 0
    guarda_posicaoes = []
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if pt not in guarda_posicaoes:
        	guarda_posicaoes.append(pt)
        count = count + 1
    cv2.imwrite('result.png', img_rgb)
    return count,guarda_posicaoes

Img01 = """undefined"""
imgdata  = base64.b64decode(Img01)
filename = 'img01.png'
with open(filename, 'wb') as f:
    f.write(imgdata)
 
resu = imagesearch_count(filename,precision=0.99)
 
print(resu)
input(f"Identificados {resu[0]} resultados continuar?")
ll = list((cv2.imread(filename)).shape[0:2])
meiox, meioy = ll[0]/2, ll[1]/2
for i in resu[1]:
    ii = list(i)
    pyautogui.click(ii[0]+meiox,ii[1]+meioy)