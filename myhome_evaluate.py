import json
import os
import math

ga_square=[]

def read_data(filename):
    global ga_square
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
    #square= round(sum([dicts['square_price'] for dicts in products])/len([dicts['square_price'] for dicts in products]),2) # not useful for adjusted average  
    ga_square += [dicts['square_price'] for dicts in products]



summary = [
    read_data(f"history/data-{i}.json")
    for i in range(len([1 for x in list(os.scandir("./history")) if x.is_file()]))
]

average_square = sum(ga_square)/len(ga_square)
ga_square.sort()
median_square = ga_square[math.floor(len(ga_square)/2)]

print("average square total: " + str(average_square))
print("median total: " + str(median_square))
cut = ga_square[math.floor(0.05*len(ga_square)):math.floor(0.95*len(ga_square))]
adjusted_average_square_price= sum(cut)/len(cut)
print("adjusted average: " + str(adjusted_average_square_price))
print(len(ga_square))
print(len(cut))
print(cut)