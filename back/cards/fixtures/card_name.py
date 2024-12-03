import json
import pprint

# 원본 Json 파일 경로
input_file = '.\credit_card\credit_card_data.json'


# 필터링한 Json 파일 경로
output_file = 'credit_card_data2.json'



with open(input_file, 'r', encoding='utf-8') as f:
    data1 = json.load(f)

filtered_data = []

cardCompany =[

]

for idx,item in enumerate(data1):
    if item['fields']["brand"] not in cardCompany:
        cardCompany.append(item['fields']["brand"])

print(cardCompany)

# company_card 모델 데이터 만들기
# card_company_models=[]
# for idx,company in enumerate(cardCompany):
#     card_company_models.append({
#         "model": "cards.Card_company",
#         "fields": {
#             "card_company_id" : idx+1,
#             "company_name" : company
#         }
#     })

# company_output_file = 'card_company.json'

# with open(company_output_file, 'w', encoding='utf-8') as f:
#     json.dump(card_company_models, f, ensure_ascii=False, indent=4)

filtered_data=[]

for idx,item in enumerate(data1):
    if item['fields']["brand"] in cardCompany:
        item['fields']["brand"]= cardCompany.index(item['fields']["brand"])+1
        filtered_data.append(item)
    else:
        print(item)
        filtered_data.append(item)

# 결과 JSON 파일로 저장
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)