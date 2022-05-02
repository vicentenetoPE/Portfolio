import yfinance as yf

def preco (x):
   x = yf.Ticker(x+".SA")
   x = x.info['regularMarketPrice']
   return x
PETR4 = yf.Ticker("PETR4.SA")
print(PETR4.info)
entrada = input('coloque um número de 1 a 5 \n 1 - TASA \n 2 - PETR \n 3 - ALSO \n 4 - TAEE \n 5 - SAPR \n')
entrada = float(entrada)



p = 0
#def gap(y):
#def op(z):

if entrada == 1:
   gaptasa = round(preco("TASA4") - preco("TASA3"),2)
   print("O preço de TASA4-TASA3 é:", gaptasa)

if entrada == 2:
   gappetr = round(preco("PETR3") - preco("PETR4"),2)
   print("O preço de PETR3-PETR4 é: ", gappetr, "o alvo é 3.4")
   '''oppetr = 3
   if gappetr < 0:
      gappetr = gappetr * (-1)
   print("O preço de PETR3-PETR4 é:", gappetr)
   if gappetr < oppetr:
      print('Lucro em PETR de:', round((oppetr-gappetr),2))
   else:
      print('Prejuízo em PETR de:', round((oppetr-gappetr),2))'''


if entrada == 4:
   gaptaee =  round(preco("TAEE4") - preco("TAEE3"),2)
   print("O preço de TAEE4-TAEE3 é:", gaptaee)

if entrada == 5:
   gapsapr =  round(preco("SAPR11") - (preco("SAPR3")*5),2)
   print("O preço de SAPR11-SAPR3 é:", gapsapr)