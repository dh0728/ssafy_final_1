# Colab으로 모델 생성
'''
pip install langchain langchain-community
pip install langchain langchain-openai tiktoken
pip install faiss-cpu

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore

# 원본 데이터 로드하기
import json

credit_card__file_path = '/content/drive/MyDrive/ssafy_1_final/combined_check_card_data.json'

with open(credit_card__file_path, "r", encoding="utf-8") as f:
    check_card_data = json.load(f)

print(check_card_data)  # 데이터 확인

# 카테고리를 기준으로 문서 생성
documents = []
for card in check_card_data:
    for category in card['categories']:
        content = f"Category: {category} Card ID :{card['check_card_id']}"
        documents.append(content)

print(documents)

# Splitter 적용 chunk로 쪼개기
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = splitter.create_documents(documents)

print(docs)

cache_dir = LocalFileStore("./.cache/practice/")

#API-KEY 설정
OPENAI_API_KEY = 'MY_KEY'


embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=OPENAI_API_KEY
    )

#임베딩하기
cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)

vectorstore = FAISS.from_documents(docs, cached_embeddings)

# FAISS 벡터 스토어 생성
vectorstore = FAISS.from_documents(docs, cached_embeddings)
print(f"Stored {len(docs)} documents in FAISS vector store.")

# FAISS 저장소 저장
faiss_store_dir = "/content/drive/MyDrive/ssafy_1_final/faiss_vector_store_check"
vectorstore.save_local(faiss_store_dir)
print(f"FAISS vector store saved to {faiss_store_dir}.")

# 검색기 생성
retriever = vectorstore.as_retriever(search_kwargs={"k": 9})
#복합 검색 질의
query = "Category: 카페/디저트"
results = retriever.get_relevant_documents(query)

# 결과 출력
print("Search Results (Multi-category query):")
for result in results:
    print(result.page_content)

'''
