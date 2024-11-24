<template>
  <div class="card-list">
    <div v-for="card in store.cards" :key="getCardId(card)" class="card-item">
      <!-- 왼쪽: 카드 이미지 -->
      <div class="card-container">
        <div class="circle-bg"></div> <!-- 원 배경 -->
        <div class="card-image">
          <img :src="card.img_path" :alt="getCardName(card)" />
        </div>
      </div>

      <!-- 오른쪽: 카드 정보 -->
      <div class="card-content">
        <!-- 카드명과 브랜드 -->
        <div class="card-header">
          <div class="title-wrap">
            <h3>{{ getCardName(card) }}</h3>
            <span class="brand">{{ card.brand }}</span>
          </div>
          <div class="button-group">
            <RouterLink :to="{ name: 'CardDetail', params: { type: store.currentType === 'credit' ? 'credit' : 'check', cardId: getCardId(card)}}" class="detail-btn">
              자세히 보기
            </RouterLink>
            <button @click="registerCard(card)" class="register-btn"> + 내 카드 등록</button>
          </div>
        </div>

        <!-- 혜택 태그 -->
        <div class="benefit-tag">최대 18만원 캐시백</div>

        <!-- 혜택 그리드 -->
        <div class="benefits-grid">
          <div v-for="(category, index) in getCardCategories(card)"
              :key="index"
              class="benefit-item">
            <div class="benefit-title">{{ category.title }}</div>
            <div class="benefit-desc">{{ category.desc }}</div>
          </div>
        </div>

        <!-- 카드 정보 -->
        <div class="card-info">
          <div class="info-row">
            <span>연회비</span>
            <span>{{ card.abroad_fee === 0 ? '없음' : `${formatNumber(card.abroad_fee)}원` }}</span>
          </div>
          <div class="separator">/</div>
          <div class="info-row">
            <span>전월실적</span>
            <span>{{ card.pre_month_perform }}</span>
          </div>
        </div>
      </div>
    </div>
    <div ref="observerTarget" class="observer-target"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useCardStore } from "@/stores/cards.js"

const store = useCardStore()
const observerTarget = ref(null)

// ID 가져오기
const getCardId = (card) => {
  return card.credit_card_id || card.check_card_id
}

// 카드 이름 가져오기
const getCardName = (card) => {
  return card.credit_card_name || card.check_card_name
}

// 카드 카테고리 정보 가져오기
const getCardCategories = (card) => {
  // credit_card_category 또는 check_card_category에서 해당 카드의 카테고리 정보 반환
  return card.categories?.slice(0, 3) || []
}

// 숫자 포맷팅
const formatNumber = (number) => {
  return number?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

// 마지막 카드의 ID 가져오기
const getLastCardId = () => {
  if (store.cards.length === 0) return null
  const lastCard = store.cards[store.cards.length - 1]
  return lastCard.credit_card_id || lastCard.check_card_id
}

const setupObserver = () => {
  const observer = new IntersectionObserver(async (entries) => {
    const target = entries[0]
    if (target.isIntersecting && store.hasMoreCards) {
      const lastId = getLastCardId()
      if (lastId) {
        await store.getMoreCards(lastId)
      }
    }
  }, {
    threshold: 0.5
  })

  if (observerTarget.value) {
    observer.observe(observerTarget.value)
  }

  return observer
}

// currentType이 변경될 때마다 observer 재설정
watch(() => store.currentType, () => {
  if (observerTarget.value) {
    setupObserver()
  }
})

const registerCard = async (card) => {
  try {
    const cardType = store.currentType === 'credit' ? 1 : 2
    const cardId = getCardId(card)

    const result = await store.registerMyCard(cardType, cardId)
    alert(result.message)
  } catch (error) {
    console.error('카드 등록 실패:', error)
    alert('카드 등록 중 오류가 발생했습니다.')
  }
}

onMounted(() => {
  const observer = setupObserver()

  // cleanup
  return () => {
    if (observerTarget.value) {
      observer.unobserve(observerTarget.value)
    }
  }
})
</script>

<style scoped>
.card-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
.card-container {
  position: relative; /* 카드와 원을 겹치기 위한 부모 컨테이너 */
  display: flex; /* 카드 정렬에 필요한 flex 적용 */
  align-items: center; /* 세로 중앙 정렬 */
  justify-content: center; /* 카드와 내용 정렬 조정 */
  width: 200px; /* 필요한 만큼 확장 */
  height: 120px;
}

.circle-bg {
  position: absolute; /* 카드 뒤에 배경을 배치 */
  margin-right: 24px;
  transform: translateX(-50%,50%); 
  width: 120px; /* 원의 너비 */
  height: 120px; /* 원의 높이 (정사각형) */
  background-color: #f3f3f3; /* 원 배경색 */
  border-radius: 50%; /* 원 형태로 만듦 */
  z-index: 0; /* 카드보다 뒤로 배치 */
}

.card-image {
  width: 130px;
  height: 130px;
  margin-right: 24px;
  /* margin-top: 48px; 제거 */
  z-index: 1;
  display: flex;
  align-items: center;  /* 세로 중앙 정렬 */
  justify-content: center;  /* 가로 중앙 정렬 */
  /* transition: transform 0.3s ease; */
  overflow: hidden;
}

.card-image img {
  max-width: 100%; /* 이미지를 컨테이너에 맞게 조정 */
  max-height: 100%; /* 높이를 맞춤 */
  object-fit: contain; /* 이미지의 비율을 유지하며 컨테이너에 맞춤 */
  display: block; /* 기본 margin 제거 */
}

.card-item {
  display: flex;
  padding: 24px;
  border: 1px solid #eee;
  border-radius: 12px;
  margin-bottom: 20px;
  background: white;
  transition: all 0.2s ease;
  align-items: center;  /* 추가: 카드 내용과 이미지 세로 중앙 정렬 */
  /* overflow: hidden; */
}

.card-image:hover {
  animation: bounce 0.5s ease;
  cursor: pointer;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}



.card-image:hover img {
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

.card-content {
  flex: 1;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.title-wrap {
  display: flex;
  flex-direction: column;
}

.title-wrap h3 {
  font-size: 1.3rem;
  font-weight: 600;
  margin: 0;
  margin-bottom: 4px;
  color: #1a1438;
}

.brand {
  color: #666;
  font-size: 0.9rem;
}

.detail-btn {
  padding: 8px 16px;
  background: #000;
  color: white;
  border: none;
  border-radius: 4px;
  text-decoration: none;
  font-size: 0.9rem;
}

.benefit-tag {
  display: inline-block;
  padding: 4px 12px;
  background-color: #fff3e0;
  color: #ff6b00;
  border-radius: 4px;
  font-size: 0.9rem;
  margin-bottom: 16px;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.benefit-item {
  padding: 16px;
  background: #f8f9fa;
  border-radius: 8px;
}

.benefit-title {
  font-weight: 500;
  margin-bottom: 8px;
  color: #333;
}

.benefit-desc {
  color: #666;
  font-size: 0.9rem;
}

.card-info {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #666;
  font-size: 0.9rem;
}

.info-row {
  display: flex;
  gap: 8px;
}

.separator {
  color: #ddd;
}

.observer-target {
  height: 20px;
  margin: 20px 0;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.detail-btn {
  padding: 8px 16px;
  background: #000;
  color: white;
  border: none;
  border-radius: 4px;
  text-decoration: none;
  font-size: 0.9rem;
  text-align: center;
}

.register-btn {
  padding: 8px 16px;
  background: #f8f9fa;
  color: #333;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.register-btn:hover {
  background: #e9ecef;
}
</style>