<template>
  <div class="card-detail-container" v-if="cardData">
    <!-- 상단 영역: 카드 이미지와 기본 정보 -->
    <div class="card-basic-info">
      <div class="card-image-container">
        <div class="card-image">
          <img :src="cardData.img_path" :alt="cardData.credit_card_name">
        </div>
      </div>
      <div class="card-info">
        <h1>{{ cardData.credit_card_name }}</h1>
        <p class="brand">{{ cardData.brand }}</p>
        <div class="fees">
          <div class="fee-item">
            <span class="label">국내전용</span>
            <span class="value">{{ cardData.domestic_fee === 0 ? '없음' : `${formatNumber(cardData.domestic_fee)}원` }}</span>
          </div>
          <div class="fee-item">
            <span class="label">해외겸용</span>
            <span class="value">{{ cardData.abroad_fee === 0 ? '없음' : `${formatNumber(cardData.abroad_fee)}원` }}</span>
          </div>
        </div>
        <div class="perform">
          <span class="label">전월실적</span>
          <span class="value">{{ cardData.pre_month_perform }}</span>
        </div>
      </div>
    </div>

    <!-- 혜택 영역 -->
    <div class="benefits-section">
      <h2>카드 혜택</h2>
      <div class="benefits-list">
        <div v-for="benefit in cardData.benefits"
             :key="benefit.title"
             class="benefit-item">
          <div class="benefit-header">
            <h3>{{ benefit.title }}</h3>
            <p class="benefit-desc">{{ benefit.desc }}</p>
          </div>
          <div class="benefit-detail" v-html="formatDetail(benefit.desc_detail)"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { cardDetail } from '@/assets/cardDetail'

const route = useRoute()
const cardData = ref(null)

const formatNumber = (number) => {
  return number?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

const formatDetail = (detail) => {
  return detail?.replace(/\n/g, '<br>')
}

onMounted(() => {
  // 실제 API 연동 전까지는 더미 데이터 사용
  cardData.value = cardDetail
})
</script>

<style scoped>
.card-detail-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.card-basic-info {
  display: flex;
  gap: 3rem;
  margin-bottom: 3rem;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card-image-container {
  position: relative;
  width: 300px;
}

.card-image {
  width: 100%;
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-image::before {
  content: '';
  position: absolute;
  width: 80%;
  height: 80%;
  background: radial-gradient(circle, rgba(26, 20, 56, 0.08) 0%, rgba(255, 255, 255, 0) 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: -1;
  border-radius: 50%;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.card-info {
  flex: 1;
}

.card-info h1 {
  font-size: 1.8rem;
  color: #1a1438;
  margin-bottom: 0.5rem;
}

.brand {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.fees {
  display: flex;
  gap: 2rem;
  margin-bottom: 1rem;
}

.fee-item, .perform {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.label {
  color: #666;
}

.value {
  font-weight: 500;
}

.benefits-section {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.benefits-section h2 {
  font-size: 1.5rem;
  color: #1a1438;
  margin-bottom: 1.5rem;
}

.benefits-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.benefit-item {
  padding: 1.5rem;
  border: 1px solid #eee;
  border-radius: 8px;
}

.benefit-header {
  margin-bottom: 1rem;
}

.benefit-header h3 {
  font-size: 1.2rem;
  color: #1a1438;
  margin-bottom: 0.5rem;
}

.benefit-desc {
  color: #666;
  font-size: 1.1rem;
}

.benefit-detail {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .card-basic-info {
    flex-direction: column;
    gap: 1.5rem;
  }

  .card-image-container {
    width: 100%;
  }
}
</style>