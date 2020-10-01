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
    #square= round(sum([dicts['square_price'] for dicts in products])/len([dicts['square_price'] for dicts in products]),2) # not useful for adjusted average  


summaries = [
    read_data(f"history/01-10-20/data-{i}.json")
    for i in range(len([1 for x in list(os.scandir("./history/01-10-20")) if x.is_file()]))
]


def get_average_square_price():
    ga=[
    entry["square_price"] for summary in summaries for entry in summary
    if entry["square_price"] > 150 and entry["square_price"] < 6000
    ]
    ga.sort()

    average = sum(ga)/len(ga)
    median = ga[math.floor(len(ga)/2)]

    print("average square total: " + str(average))
    print("median total: " + str(median))
    cut = ga[math.floor(0.1*len(ga)):math.floor(0.9*len(ga))]
    adjusted_average_price= sum(cut)/len(cut)
    adjusted_median_price = cut[math.floor(len(ga)/2)]
    print("adjusted average: " + str(round(adjusted_average_price,2)))
    print("adjusted median: " + str(round(adjusted_median_price,2)))
    print(len(ga))
    print(len(cut))

def get_average_price():
    ga=[
    float(entry["price"]) for summary in summaries for entry in summary
    if float(entry["price"]) > 8000 and float(entry["price"]) < 10000000
    ]
    ga.sort()

    average = sum(ga)/len(ga)
    median = ga[math.floor(len(ga)/2)]

    print("average square total: " + str(average))
    print("median total: " + str(median))
    cut = ga[math.floor(0.1*len(ga)):math.floor(0.9*len(ga))]
    adjusted_average_price= sum(cut)/len(cut)
    adjusted_median_price = cut[math.floor(len(ga)/2)]
    print("adjusted average: " + str(round(adjusted_average_price,2)))
    print("adjusted median: " + str(round(adjusted_median_price,2)))
    print(len(ga))
    print(len(cut))

get_average_price()
get_average_square_price()

