import pyautogui

print("ray silva de arruda")
pyautogui.hotkey('win','x')
pyautogui.press('a')
pyautogui.hotkey('win','x')
pyautogui.press('t')

import requests, json
he = {"Content-Type": "application/json; charset=utf-8","Accept": "application/json"}
dt = json.loads(requests.get("https://jsonblob.com/api/json/60d946db-0a9c-11eb-af5c-57272dc9e1cc",headers=he).text)

for i in dt["Execultando"]:
    if i["nome"] == "pwdandtarefas":
        i["Resultado"] = "Finalizado"

final_data = json.dumps(dt)
requests.put("https://jsonblob.com/api/jsonBlob/60d946db-0a9c-11eb-af5c-57272dc9e1cc",headers=he,data=final_data)