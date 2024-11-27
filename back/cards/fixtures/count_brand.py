import json
import pprint

# 원본 Json 파일 경로
input_file = './credit_card/credit_card_data.json'



with open(input_file, 'r', encoding='utf-8') as f:
    data1 = json.load(f)

brand=set()

for idx,item in enumerate(data1):
    brand.add(item['fields']["brand"])

print(brand)
