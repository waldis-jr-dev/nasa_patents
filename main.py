import json

with open('nasa-patents-api-1.json', 'r', encoding= 'utf-8') as file:
    data = json.load(file)

patents = {}

for patent in data:
    keys = patents.keys()
    if 'patent_expiration_date' in patent:
        year = int(patent['patent_expiration_date'][:4:])
        if year not in keys:
            patents[year] = 1
        if year in keys:
            patents[year] += 1

for year in sorted(patents):
    print(f'{year}: {"*"*patents[year]}')
