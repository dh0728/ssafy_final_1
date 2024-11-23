import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Django 프로젝트 경로에 맞게 설정
index_file_path ='cards/management/commands/faiss_indices/faiss_indices_combined_vector_index.index'
ids_file_path = 'cards/management/commands/faiss_indices/faiss_indices_vector_ids.npy'

# FAISS 인덱스 및 ID 매핑 파일 불러오기
index = faiss.read_index(index_file_path)
loaded_ids = np.load(ids_file_path)

# 임베딩 모델 로드
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 사용자 쿼리 입력 및 검색 수행
user_query = input("검색하고 싶은 내용을 입력하세요: ")
query_embedding = model.encode(user_query).astype('float32')

# 검색 수행 (가장 유사한 5개 결과 찾기)
D, I = index.search(np.array([query_embedding]), k=10)

# 검색된 결과 출력
print("추천된 결과:")
for idx in I[0]:
    original_id = loaded_ids[idx]
    print(f"추천된 아이템 ID: {original_id}")