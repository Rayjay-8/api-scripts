
import requests, json
dt = json.loads(requests.get("https://jsonblob.com/api/json/60d946db-0a9c-11eb-af5c-57272dc9e1cc",headers={"Content-Type": "application/json; charset=utf-8","Accept": "application/json"}).text)
for i in dt["Execultando"]:/n    if i["nome"] == name:/n        i["Resultado"] = "Finalizado"/n        alteracao = 1/n    return alteracao