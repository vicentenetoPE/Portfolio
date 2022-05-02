import yfinance as yf
from datetime import datetime


def preco (x):
   x = yf.Ticker(x+".SA")
   x = x.info['regularMarketPrice']
   return x
print("Programa ativo")
loop = 0
c = 2
while c == 2:
    loop = loop + 1
    print("Estamos no loop nº: ", loop)
    print(datetime.today().strftime('%H:%M:%S'))
    gaptasa = round(preco("TASA4") - preco("TASA3"),2)
    print("O preço de TASA4-TASA3 é: ", gaptasa)


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

    gapalso = round(preco("ALSO3") - preco("MULT3"),2)
    print("O preço de MULT3-ALSO3 é: ", gapalso)

    gaptaee =  round(preco("TAEE4") - preco("TAEE3"),2)
    print("O preço de TAEE4-TAEE3 é: ", gaptaee)

    gaptaesa =  round(preco("TAEE4")*3 - preco("TAEE11"),2)
    print("O preço de TAEE4-TAEE11 é: ", gaptaesa, "o alvo é 0.6")

    gapsapr =  round(preco("SAPR11") - (preco("SAPR3")*5),2)
    print("O preço de SAPR11-SAPR3 é: ", gapsapr, "o alvo é 40 ou 80")

    gapmovi =  round((preco("LCAM3")*100) - (preco("MOVI3")*135),2)
    print("O preço de LCAM3-MOVI3 é: ", gapmovi, "o alvo é -20 ou 220")

    gapklbn =  round(preco("KLBN11")*100 - (preco("KLBN3")*100 + preco("KLBN4")*400),2)
    print("O preço de KLBN11­(KLBN3+KLBN4*4) é: ", gapklbn, "o alvo é 50")