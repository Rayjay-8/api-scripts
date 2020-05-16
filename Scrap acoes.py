import requests,json
url1 = "https://statusinvest.com.br/home/mainsearchquery?q=azul4"
valores1dias = "https://statusinvest.com.br/category/tickerprice?ticker=azul4&type=-1"
valores5dias = "https://statusinvest.com.br/category/tickerprice?ticker=MEAL3&type=0"
valores30dias = "https://statusinvest.com.br/category/tickerprice?ticker=MEAL3&type=1"
valores6meses = "https://statusinvest.com.br/category/tickerprice?ticker=MEAL3&type=2"
valores1ANO = "https://statusinvest.com.br/category/tickerprice?ticker=azul4&type=3"
valores5ANO = "https://statusinvest.com.br/category/tickerprice?ticker=azul4&type=4"
url3 = "https://statusinvest.com.br/acao/getmargins?companyName=imc&type=0"
url4 = "https://statusinvest.com.br/acao/getbsactivepassivechart?companyName=imc&type=0"
url5 = "https://statusinvest.com.br/acao/getrevenue?companyName=imc&type=0&trimestral=false"
dados = requests.get(valores5ANO).text
variacao = requests.get(url1).text
tttx = json.loads(variacao)[0]['variation']

print("VARIACAO = "+str(tttx))
jjs = json.loads(dados)['prices']

soma = 0
for i in jjs:
    #print(i['price'])
    soma += i['price']
print("Media == "+str(soma/len(jjs)))
