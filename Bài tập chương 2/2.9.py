import json
a = {
    'name': "Nhung",
    "age": 20,
    "class": "DHKL17A2HN"
}
chuyen_doi = json.dumps(a, indent=4, sort_keys=True )
print(chuyen_doi)