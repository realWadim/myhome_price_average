import json
import os
import math

def read_data(filename):
    with open(filename) as f:
        data = json.load(f)["Data"]
        
    products = [
        {
            "price": entry["price"],
            "size": entry["area_size"],
            "square_price": round(float(entry["price"])/float(entry["area_size"]),2),
            "user": data["Users"]["Data"].get(entry["user_id"], {}).get("username", None)
        }
        for entry in data["Prs"]
    ]
    return products


summaries = [
    read_data(f"history/01-10-20/data-{i}.json") # pointing at a specific date
    for i in range(len([1 for x in list(os.scandir("./history/01-10-20")) if x.is_file()]))
]

headers = ["price","square_price","size"]

def get_averages():
    for header in headers:    
        ga=[
        float(str(entry[header]).replace(",",".")) for summary in summaries for entry in summary
        #if float(entry["price"]) > 8000 and float(entry["price"]) < 10000000 # TODO find a place for it
        ]
        ga.sort()

        average = sum(ga)/len(ga)
        median = ga[math.floor(len(ga)/2)]

        print(f"average {header}: " + str(round(average,2)))
        print(f"median {header}: " + str(round(median,2)))
        cut = ga[math.floor(0.1*len(ga)):math.floor(0.9*len(ga))]
        adjusted_average_price= sum(cut)/len(cut)
        adjusted_median_price = cut[math.floor(len(ga)/2)]
        print(f"adjusted average {header}: " + str(round(adjusted_average_price,2)))
        print(f"adjusted median {header}: " + str(round(adjusted_median_price,2)))
        print()
        #print(len(ga))
        #print(len(cut))

get_averages()

