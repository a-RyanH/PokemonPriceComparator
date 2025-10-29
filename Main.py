import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))

df = pd.read_excel("JPNpoke.xlsx")
pokeDict = pd.Series(df.usd.values, index=df.name).to_dict()

profitableCards = [["Profit", "Price", "Name", "Link", ]]
notSoldCards = ["JpnName"]

for key in pokeDict:

    #formats data from table to be used in url
    nameAndSetNum = key.split("}")
    nameAndSetNum[1] = nameAndSetNum[1].replace("〈", "")
    nameAndSetNum[1] = nameAndSetNum[1].replace("〉", "+")
    setFilter = (nameAndSetNum[1].split("+"))[1]
    setFilter = setFilter.replace("[" , "")
    setFilter = setFilter.replace("]" , "")

    #Scrapes TCGplayer for price by set and number
    url =  "https://www.tcgplayer.com/search/all/product?Language=all&q=" + nameAndSetNum[1] + "&view=grid&setName=" + setFilter
    driver.get(url)
    wait = WebDriverWait(driver, 3)
    try:
        name_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card__title.truncate"))).text
        try:
            price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory__price-with-shipping"))).text
        except:
            print("Card out of stock")
    except:
        print("Card not found")
        notSoldCards.append(nameAndSetNum[0])

    #compares price in table to price on tcg player
    if(price_element):
        comparablePrice = float(price_element[1:])

        #Card Authentication
        setNumber = str(((nameAndSetNum[1].split("+"))[0].split("/"))[0]) #takes the  x in x/set to compare to name



        if(((comparablePrice*1.3)<pokeDict[key] or comparablePrice+10<pokeDict[key]) and setNumber in name_element):
            cardProfit = str(round(pokeDict[key] - comparablePrice, 2))
            print(name_element + " " + price_element + " Profit: $" + cardProfit)
            profitableCards.append([cardProfit, price_element, name_element, url])


profitDf = pd.DataFrame(profitableCards[1:], columns = profitableCards[0])
unknownDf = pd.DataFrame(notSoldCards)

profitDf.to_excel('buySheet.xlsx', index=False)
unknownDf.to_excel('checkSheet.xlsx', index=False)