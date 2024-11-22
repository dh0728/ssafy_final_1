import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json

# 필요한 패키지 설치 명령어 출력
# "pip install faiss-cpu numpy sentence-transformers"

# 임베딩 모델 로드
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 신용카드 데이터 로드
credit_card_file_path = 'combined_credit_card_data.json'
try:
    with open(credit_card_file_path, 'r', encoding='utf-8') as category_file:
        credits_data = json.load(category_file)
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {credit_card_file_path}")
    exit()

credit_card_embeddings = {
    card['credit_card_id']: model.encode(
        f"{card['credit_card_name']} " + " ".join(card['categories'])
    ) for card in credits_data
}

# 카테고리 개별 임베딩 결합
# credit_card_embeddings = {}
# for card in credits_data:
#     name_embedding = model.encode(card['credit_card_name'])
#     category_embeddings = [model.encode(category) for category in card['categories']]
#     combined_embedding = np.mean([name_embedding] + category_embeddings, axis=0)
#     credit_card_embeddings[card['credit_card_id']] = combined_embedding

# numpy 배열로 변환 (벡터는 float32로 변환)
all_embeddings = np.array(list(credit_card_embeddings.values()), dtype='float32')

# FAISS 인덱스 생성 및 저장
d = all_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(all_embeddings)

# 출력 디렉토리 생성
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'faiss_indices')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 인덱스 저장
index_file_path = os.path.join(output_dir, 'faiss_indices_combined_vector_index.index')
faiss.write_index(index, index_file_path)

# ID 매핑 저장 (원본 데이터와 매핑하기 위해)
ids = list(credit_card_embeddings.keys())
ids_file_path = os.path.join(output_dir, 'faiss_indices_vector_ids.npy')
np.save(ids_file_path, np.array(ids))

print("FAISS 인덱스와 ID 매핑이 성공적으로 저장되었습니다.")