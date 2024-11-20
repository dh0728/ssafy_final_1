<template>
  <div class="card-list">
    <div v-for="card in store.cards" :key="getCardId(card)" class="card-item">
      <!-- 왼쪽: 카드 이미지 -->
      <div class="card-image">
        <img :src="card.img_path" :alt="getCardName(card)">
      </div>

      <!-- 오른쪽: 카드 정보 -->
      <div class="card-content">
        <!-- 카드명과 브랜드 -->
        <div class="card-header">
          <div class="title-wrap">
            <h3>{{ getCardName(card) }}</h3>
            <span class="brand">{{ card.brand }}</span>
          </div>
          <RouterLink :to="{ name: 'CardDetail', params: { type: store.currentType === 'credit' ? 'credit' : 'check',cardId: getCardId(card)}}" class="detail-btn">
            자세히 보기
          </RouterLink>
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
import { ref, computed, onMounted, watch } from 'vue'
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

.card-image {
  width: 200px;
  min-width: 200px;
  height: 120px;
  margin-right: 24px;
  /* margin-top: 48px; 제거 */
  display: flex;
  align-items: center;  /* 세로 중앙 정렬 */
  justify-content: center;  /* 가로 중앙 정렬 */
  align-self: center;  /* 부모 요소 기준 중앙 정렬 */
  transition: transform 0.3s ease;
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

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: all 0.3s ease;
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
</style>