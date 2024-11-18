<template>
  <div class="card-list">
    <div v-for="card in cards" :key="card.credit_card_id" class="card-item">
      <!-- 왼쪽: 카드 이미지 -->
      <div class="card-image">
        <img :src="card.img_path" :alt="card.credit_card_name">
      </div>

      <!-- 오른쪽: 카드 정보 -->
      <div class="card-content">
        <!-- 카드명과 브랜드 -->
        <div class="card-header">
          <div class="title-wrap">
            <h3>{{ card.credit_card_name }}</h3>
            <span class="brand">{{ card.brand }}</span>
          </div>
          <a :href="card.bank_url" target="_blank" class="detail-btn">자세히 보기</a>
        </div>

        <!-- 혜택 태그 -->
        <div class="benefit-tag">최대 18만원 캐시백</div>

        <!-- 혜택 그리드 -->
        <div class="benefits-grid">
          <div class="benefit-item">
            <div class="benefit-title">공과금</div>
            <div class="benefit-desc">10% 할인</div>
          </div>
          <div class="benefit-item">
            <div class="benefit-title">마트, 편의점</div>
            <div class="benefit-desc">10% 할인</div>
          </div>
          <div class="benefit-item">
            <div class="benefit-title">식음료</div>
            <div class="benefit-desc">10% 할인</div>
          </div>
        </div>

        <!-- 카드 정보 -->
        <div class="card-info">
          <div class="info-row">
            <span>해외결제 수수료</span>
            <span>{{ formatNumber(card.abroad_fee) }}원</span>
          </div>
          <div class="separator">/</div>
          <div class="info-row">
            <span>전월실적</span>
            <span>{{ card.pre_month_perform }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { cardData } from '@/assets/cardData.js'
import { cardCategory } from '@/assets/cardCategory.js'

const cards = ref([])
const categories = ref([])

// 숫자 포맷팅
const formatNumber = (number) => {
  return number?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

// 카드별 카테고리 정보 가져오기
const getCardCategories = (cardId) => {
  return categories.value.filter(cat =>
      cat.credit_card_id === cardId
  ).slice(0, 3) // 최대 3개만 표시
}

onMounted(() => {
  // cardData.js에서 카드 정보 가져오기
  cards.value = cardData.item.map(item => item.fields)

  // cardCategory.js에서 카테고리 정보 가져오기
  categories.value = cardCategory.item.map(item => item.fields)
})
</script>

<style scoped>
.card-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.card-item {
  display: flex;
  padding: 24px;
  border: 1px solid #eee;
  border-radius: 12px;
  margin-bottom: 20px;
  background: white;
  transition: all 0.2s ease;
}

.card-image {
  width: 200px;
  min-width: 200px;
  height: 120px;
  margin-right: 24px;
  margin-top: 48px; /* 상단 여백 추가 */
  display: flex;
  align-items: center;
  justify-content: center; /* 가운데 정렬 추가 */
  transition: transform 0.3s ease;
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

/* 부드러운 전환을 위한 추가 스타일 */
/* 이미지 크기도 약간 조정 */
.card-image img {
  width: 100%; /* 이미지 크기를 약간 줄임 */
  height: 100%;
  object-fit: contain;
  transition: all 0.3s ease;
}

/* 선택적: 호버 시 약간의 그림자 효과 추가 */
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

.title-wrap h3 {
  font-size: 1.3rem;
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

.tab-btn::after,
.tab-btn.active::after {
  display: none !important;
}
</style>