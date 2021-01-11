travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country,visits,cities):
  travel_log.append({"country":country,"visits":visits,"cities":cities})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
for i in range(0,len(travel_log)):
    for j in travel_log[i]:
        print(f"{j}:{travel_log[i][j]}")
for i in range(0,len(travel_log)):
    for j in range(0,len(travel_log[i]["cities"])):
        print(travel_log[i]["cities"][j])