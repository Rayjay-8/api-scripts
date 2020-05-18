import requests,json

papel = "meal3"

url1 = "https://statusinvest.com.br/home/mainsearchquery?q="+papel 
valores1dia = "https://statusinvest.com.br/category/tickerprice?ticker="+papel +"&type=-1"
valores5dias = "https://statusinvest.com.br/category/tickerprice?ticker="+papel +"&type=0"
valores30dias = "https://statusinvest.com.br/category/tickerprice?ticker="+papel +"&type=1"
valores6meses = "https://statusinvest.com.br/category/tickerprice?ticker="+papel +"&type=2"
valores1ANO = "https://statusinvest.com.br/category/tickerprice?ticker="+papel +"&type=3"
valores5ANO = "https://statusinvest.com.br/category/tickerprice?ticker="+papel +"&type=4"
url3 = "https://statusinvest.com.br/acao/getmargins?companyName=imc&type=0"
url4 = "https://statusinvest.com.br/acao/getbsactivepassivechart?companyName=imc&type=0"
url5 = "https://statusinvest.com.br/acao/getrevenue?companyName=imc&type=0&trimestral=false"
dados = requests.get(valores30dias).text

variacao = requests.get(url1).text
tttx = json.loads(variacao)[0]['variation']
valor_agora = json.loads(variacao)[0]['price']
print("Valor atual = "+str(valor_agora))
print("Alta/Baixa = "+str(tttx)+"%")


jjs = json.loads(dados)['prices']

soma = 0
for i in jjs:
    #print(i['price'])
    soma += i['price']
print("Valor Media == "+str(soma/len(jjs)))
