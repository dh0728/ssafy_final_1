import json
import pprint

# 필터링한 Json 파일 경로
output_file = 'category.json'

kinds={
    "모든가맹점":1,
    "교통":2,
    "주유":3,
    "통신":4,
    "마트/편의점":5,
    "쇼핑":6,
    "푸드":7,
    "카페/디저트":8,
    "뷰티/피트니스":9,
    "무실적":10,
    "공과금/렌탈":11,
    "병원/약국":12,
    "애완동물":13,
    "교육/육아":14,
    "자동차/하이패스":15,
    "레저/스포츠":16,
    "영화/문화":17,
    "간편결제":18,
    "항공마일리지":19,
    "공항라운지/PP":20,
    "프리미엄":21,
    "여행/숙박":22,
    "해외":23,
    "비지니스":24,
    "기타":25,
    '금융':26,
    '생활':27,
}

filtered_data=[]

for v,k in kinds.items():
    dict = {
        "model": "cards.Category",
    }
    dict['fields']={
        "category_id":k,
        "category_name":v
    }
    filtered_data.append(dict)

# 결과 JSON 파일로 저장
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

