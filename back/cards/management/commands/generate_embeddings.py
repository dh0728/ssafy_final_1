import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from cards.models import Category, Credit_cards, Check_cards, Credit_card_category, Check_card_category

# 필요한 패키지 설치 명령어 출력
# "pip install faiss-cpu numpy sentence-transformers"

# 임베딩 모델 로드
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 데이터베이스에서 데이터 추출
categories = Category.objects.all()
credit_cards = Credit_cards.objects.all()
check_cards = Check_cards.objects.all()
credit_card_categories = Credit_card_category.objects.all()
check_card_categories = Check_card_category.objects.all()

# 카테고리 임베딩 생성
category_embeddings = {
    cat.category_id: model.encode(f"{cat.category_name}") for cat in categories
}

# 신용카드 임베딩 생성
credit_card_embeddings = {
    cc.credit_card_id: model.encode(
<<<<<<< HEAD
        f"{cc.credit_card_name} {cc.brand} {cc.pre_month_perform} {cc.domestic_fee} {cc.abroad_fee}"
=======
        f"{cc.credit_card_name}"
>>>>>>> 7a852adc33a11397a4469262d890b2d61237a2da
    ) for cc in credit_cards
}

# 체크카드 임베딩 생성
check_card_embeddings = {
    chk.check_card_id: model.encode(
<<<<<<< HEAD
        f"{chk.check_card_name} {chk.brand} {chk.pre_month_perform} {chk.domestic_fee} {chk.abroad_fee}"
=======
        f"{chk.check_card_name}"
>>>>>>> 7a852adc33a11397a4469262d890b2d61237a2da
    ) for chk in check_cards
}

# 신용카드-카테고리 임베딩 생성
credit_card_category_embeddings = {
    ccc.credit_card_category_id: model.encode(
        f"{ccc.title} {ccc.desc} {ccc.desc_detail}"
    ) for ccc in credit_card_categories
}

# 체크카드-카테고리 임베딩 생성
check_card_category_embeddings = {
    ckc.check_card_category_id: model.encode(
        f"{ckc.title} {ckc.desc} {ckc.desc_detail}"
    ) for ckc in check_card_categories
}

# 임베딩 결합 및 리스트 생성
embeddings = []
ids = []

# 모든 임베딩 추가
for cat_id, embedding in category_embeddings.items():
    embeddings.append(embedding)
    ids.append(f"category_{cat_id}")

for cc_id, embedding in credit_card_embeddings.items():
    embeddings.append(embedding)
    ids.append(f"credit_card_{cc_id}")

for chk_id, embedding in check_card_embeddings.items():
    embeddings.append(embedding)
    ids.append(f"check_card_{chk_id}")

for ccc_id, embedding in credit_card_category_embeddings.items():
    embeddings.append(embedding)
    ids.append(f"credit_card_category_{ccc_id}")

for ckc_id, embedding in check_card_category_embeddings.items():
    embeddings.append(embedding)
    ids.append(f"check_card_category_{ckc_id}")

# numpy 배열로 변환 (벡터는 float32로 변환)
all_embeddings = np.array(embeddings, dtype='float32')

# FAISS 인덱스 생성 및 저장
d = all_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(all_embeddings)

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'faiss_indices')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 인덱스 저장
index_file_path = os.path.join(output_dir, 'faiss_indices_combined_vector_index.index')
faiss.write_index(index, index_file_path)

# ID 매핑 저장 (원본 데이터와 매핑하기 위해)
ids_file_path = os.path.join(output_dir, 'faiss_indices_vector_ids.npy')
np.save(ids_file_path, np.array(ids))

print("FAISS 인덱스와 ID 매핑이 성공적으로 저장되었습니다.")

<<<<<<< HEAD
# 저장된 인덱스와 ID 매핑 불러오기
index = faiss.read_index(index_file_path)  # 저장된 FAISS 인덱스 불러오기
loaded_ids = np.load(ids_file_path)  # ID 매핑 파일 불러오기

print("FAISS 인덱스와 ID 매핑이 성공적으로 불러와졌습니다.")
=======

# 저장된 인덱스와 ID 매핑 불러오기
# index = faiss.read_index(index_file_path)  # 저장된 FAISS 인덱스 불러오기
# loaded_ids = np.load(ids_file_path)  # ID 매핑 파일 불러오기

# print("FAISS 인덱스와 ID 매핑이 성공적으로 불러와졌습니다.")
>>>>>>> 7a852adc33a11397a4469262d890b2d61237a2da

# # 사용자 쿼리 임베딩 생성
# user_query = input("검색하고 싶은 내용을 입력하세요: ")  # 사용자 입력 쿼리
# query_embedding = model.encode(user_query).astype('float32')  # 쿼리를 임베딩으로 변환

# # FAISS에서 검색 수행 (가장 유사한 5개 결과 찾기)
# D, I = index.search(np.array([query_embedding]), k=5)

# # 검색된 결과 출력
# print("추천된 결과:")
# for idx in I[0]:
#     original_id = loaded_ids[idx]
#     print(f"추천된 아이템 ID: {original_id}")
