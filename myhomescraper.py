from lxml import html
import requests, time
prices=[]
totals=[]
page_nr=1
while page_nr<=100:
    #comment out 1 of the two requests for either Data on Bstumi or Tbilsi
    #page = requests.get("https://www.myhome.ge/en/s/Apartment-for-sale-House-for-Sale-Batumi?Keyword=Batumi&AdTypeID=1&PrTypeID=1.2&Page="+str(page_nr)+"&GID=8742159")
    #page = requests.get("https://www.myhome.ge/en/s/Apartment-for-sale-House-for-Sale-Tbilisi?Keyword=Tbilisi&AdTypeID=1&PrTypeID=1.2&Page="+str(page_nr)+"&GID=1996871")
    page = requests.get("https://www.myhome.ge/en/s/Apartment-for-sale-Tbilisi?Keyword=Tbilisi&AdTypeID=1&PrTypeID=1&Page="+str(page_nr)+"&GID=1996871") # nur wohnungen
    tree = html.fromstring(page.content)
    prices_current_site = tree.xpath('//span[@class="sq-price-gel d-none ml-5px"]/text()')
    print('Page '+str(page_nr)+': Squaremeter prices: ')
    print(prices_current_site)
    prices.extend(prices_current_site)
    total_current_site = tree.xpath('//b[@class="item-price-gel d-none mr-2"]/text()')
    print('Page '+str(page_nr)+': Apartment prices: ')
    print(total_current_site)
    totals.extend(total_current_site)
    page_nr += 1
    time.sleep(5)
prices = [int(i)for i in prices]
print(prices)
totals = [x.replace(",","") for x in totals]
totals = [int(i)for i in totals]
print(totals)
average_price = sum(prices)/len(prices)
average_total = sum(totals)/len(totals)
average_size = average_total/average_price
print('average price: '+ str(average_price))
print('average apartment price: '+str(average_total))
print('average apartment size: '+ str(average_size))
path='myhome/historicalnotes.txt'
results = ', '.join([str(page_nr - 1),str(average_price),str(average_total),str(average_size)])
hntxt=open(path,'r+')
hntxt.write(results)
hntxt.close()
