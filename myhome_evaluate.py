import json

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
    print(products)

    


summary = [
    read_data(f"data-{i}.json")
    for i in range(1)
]
