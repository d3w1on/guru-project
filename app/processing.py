
collection = {}

with open('data/Emissions.csv', 'rt') as f:
    data = f.readlines()
    for row in data:
        collection.update({row.split(',')[0]: row.split(',')[1:]})


def find_statistic_by_year(year):
    index = collection["CO2 per capita"].index(year)
    values = []

    for k in collection:
        values.append(collection[k][index])

    min_value = min(float(v) for v in values[1:])
    max_value = max(float(v) for v in values[1:])

    avg_value = sum(float(v) for v in values[1:]) / len(values[1:])
    min_value_country = {i for i in collection if str(min_value) in collection[i]}
    max_value_country = {i for i in collection if str(max_value) in collection[i]}

    print(f"In {year}, countries with minimum and maximum CO2 emission levels were: "
          f"{str(min_value_country).strip('{}')} and {str(max_value_country).strip('{}')} respectively.\n"
          f"Average CO2 emissions in {year} were {avg_value}")


find_statistic_by_year(input("Select a year to find statistics (1997 to 2010): "))
print(collection)




