from lxml import html
import requests, time, datetime
date = datetime.datetime.today()
prices=[]
totals=[]
sizes=[]
page_nr=1
note_nr=1
while page_nr<=3:
    #comment out 1 of the two requests for either Data on Bstumi or Tbilsi
    #page = requests.get("https://www.myhome.ge/en/s/Apartment-for-sale-House-for-Sale-Batumi?Keyword=Batumi&AdTypeID=1&PrTypeID=1.2&Page="+str(page_nr)+"&GID=8742159")
    #page = requests.get("https://www.myhome.ge/en/s/Apartment-for-sale-House-for-Sale-Tbilisi?Keyword=Tbilisi&AdTypeID=1&PrTypeID=1.2&Page="+str(page_nr)+"&GID=1996871")
    #page = requests.get("https://www.myhome.ge/en/s/Apartment-for-sale-Tbilisi?Keyword=Tbilisi&AdTypeID=1&PrTypeID=1&Page="+str(page_nr)+"&GID=1996871") # nur wohnungen tbilisi
    page = requests.get("https://www.myhome.ge/en/s/Apartment-for-rent-Tbilisi?Keyword=Tbilisi&AdTypeID=3&PrTypeID=1&Page="+str(page_nr)+"&mapC=41.73188365%2C44.8368762993663&regions=688137211&districts=737816010&cities=1996871&GID=1996871") # nur wohnungen zu vermieten grmaghele
    tree = html.fromstring(page.content)
    prices_current_site = tree.xpath('//span[@class="sq-price-gel d-none ml-5px"]/text()')
    print('Page '+str(page_nr)+': Squaremeter prices: ')
    print(prices_current_site)
    prices.extend(prices_current_site)
    total_current_site = tree.xpath('//b[@class="item-price-gel d-none mr-2"]/text()')
    print('Page '+str(page_nr)+': Apartment prices: ')
    print(total_current_site)
    totals.extend(total_current_site)
    sizes_current_site = tree.xpath('//div[@class="item-size"]/text()')
    print('Page '+str(page_nr)+': Apartment sizes: ')
    print(sizes_current_site)
    sizes.extend(sizes_current_site)
    page_nr += 1
    time.sleep(5)
prices = [int(i)for i in prices]
print(prices)
totals = [x.replace(",","") for x in totals]
totals = [int(i)for i in totals]
sizes = [x.replace(".00","") for x in sizes]
sizes = [int(i) for i in sizes]
print(totals)
average_total = sum(totals)/len(totals)
#average_size = average_total/average_price size calculated from average m2 / average sale
average_size = sum(sizes)/len(sizes)
#average_price = sum(prices)/len(prices) #durchschnittlicher qm2 preis. muss bei mietwohnung aus sein
average_price = average_total/average_size
print('average m² price: '+ str(average_price))
print('average apartment price: '+str(average_total))
print('average apartment size: '+ str(average_size))
path='history/note'+str(note_nr)+'.txt'
results = ', '.join([str(page_nr - 1),str(average_price),str(average_total),str(average_size),str(date)])
hntxt=open(path,'w+')
hntxt.writelines(results)
hntxt.close()
