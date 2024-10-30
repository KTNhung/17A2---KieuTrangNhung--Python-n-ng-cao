#Chuyển đổi python sang json
import json
a = {
    'name': "Nhung",
    "age": 20,
    "class": "DHKL17A2HN"
}

chuyen_doi = json.dumps(a, ensure_ascii=True )

print(chuyen_doi)
