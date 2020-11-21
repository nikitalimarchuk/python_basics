products = [
    (1, {"name": "Milk", "price": 100, "quantity": 5, "measure": "item"}),
    (2, {"name": "Beef", "price": 400, "quantity": 2, "measure": "item"}),
    (3, {"name": "Egg", "price": 10, "quantity": 7, "measure": "package"}),
    (4, {"name": "Tuna", "price": 1000, "quantity": 70, "measure": "kg"})
]

statistics = dict()

for product in products:
    number, item = product
    for key, value in item.items():
        if key not in statistics:
            statistics[key] = []
        statistics[key].append(value)

for key, value in statistics.items():
    statistics[key] = list(set(statistics[key]))

print(statistics)
