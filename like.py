
import time
import base64
import cv2
import pyautogui
import random
import platform
import subprocess
def imagesearch_count(image, precision=0.9):
    from desktopmagic.screengrab_win32 import getScreenAsImage
    import numpy as np
    import cv2
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

Img01 = """iVBORw0KGgoAAAANSUhEUgAAACQAAAAgCAYAAAB6kdqOAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADwSURBVFhH7ZYxDoQgEEX3GJR2lnbewM7SG1h6Au0s7bwxm29CQvQ7I1kWLChe4TDMvEkI+DHG2DdRhDSKkEYR0ihCGn8RqqrKzvNsu66j6xLRhZzMvu8HLEciqtBZZl1XmicRTegsA6ZporkSUYSYDBiGgeZLRBFaluUiA/q+t23bXsAArA4IEqrr+pjage+maaiMhHS2goQwnV/YTezHnoJBWI9sQtjHemQTujtHWYTGcaT1QRYh7GH1QXIhXBGstiO5kPbgJhXato3W9flZCHE08uN3PHlKgoTYTc3ijKf/RkFCKShCGkVI42VCxn4BsRzJgmFaIGkAAAAASUVORK5CYII="""
imgdata  = base64.b64decode(Img01)
filename = 'img01.png'
with open(filename, 'wb') as f:
    f.write(imgdata)
resu = imagesearch_count(filename,precision=0.90)
print(resu)
meiox, meioy = 20, 19
def func1():
    for i in resu[1]:
        ii = list(i)
        pyautogui.click(ii[0]+meiox,ii[1]+meioy)
func1()