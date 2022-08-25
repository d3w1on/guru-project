
collection = {}

with open('data/Emissions.csv', 'rt') as f:
    data = f.readlines()
    for row in data:
        collection.update({row.split(',')[0]: row.split(',')[1:-1]})

print(collection)
