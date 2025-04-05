#2. feladat
with open("EUcsatlakozas.txt", encoding="utf-8") as FILE:
    FILE.readline()
    countries = []
    for data in FILE:
        parts = data.strip().split(";")
        countries.append(parts)

#3. feladat
years = []
for country in countries:
    date_str = country[1].replace(".", "")
    year = date_str[:4]
    years.append(year)

print(len(years))

#4. feladat
for country in countries:
    date_str = country[1].replace(".", "")
    year = date_str[:4]
    if year == "2007":
        print(country[0])

#5. feladat
for country in countries:
    if country[0] == "Magyarország":
        print(year)

#6. feladat
for country in countries:
    date_str = country[1].replace(".", "")
    month = date_str[4:6]
    if month == "05":
        print("Volt májusban csatlakozás.")
        break

#7. feladat
latest_country = countries[0][0]
latest_date = countries[0][1]

for country in countries[1:]:
    if country[1] > latest_date:
        latest_date = country[1]
        latest_country = country[0]
print(f"Az utoljára csatlakozott tagállam: {latest_country} ({latest_date})")
#8. feladat
stats = {}
for country in countries:
    date_str = country[1].replace(".", "")
    year = date_str[:4]
    if year not in stats:
        stats[year] = 1
    else:
        stats[year] += 1

for year in stats.keys():
    print(f"{year} - {stats[year]} ország")