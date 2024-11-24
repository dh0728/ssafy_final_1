<template>
  <div class="card-detail-container" v-if="store.card">
    <!-- 상단 영역: 카드 이미지와 기본 정보 -->
    <div class="card-basic-info">
      <div class="card-image-container">
        <div class="circle-bg"></div> <!-- 원 배경 -->
        <div class="card-image">
          <img :src="store.card.img_path" :alt="store.card.credit_card_name">
        </div>
      </div>
      <div class="card-info">
        <div class="info-header">
          <div class="cashback-tag">최대 9만원 캐시백</div>
          <div class="share-button">
<!--            <img src="@/assets/images/share-icon.svg" alt="공유하기">-->
          </div>
          <h1>{{ store.card.credit_card_name }}</h1>
          <p class="brand">{{ store.card.brand }}</p>
        </div>

        <!-- 주요 혜택 아이콘 -->
        <div class="card_body"> 
          <div class="main-benefits">
            <div v-for="(benefit, index) in store.card.benefits?.slice(0, 3)"
                :key="index"
                class="benefit-icon">
              <span>{{ benefit.desc }}</span>
            </div>
          </div>
          
          <div class="action-button">
            <a v-if="store.card.is_active"
              :href="store.card.bank_url"
              target="_blank"
              class="bank-btn">
              카드사 바로가기
              <span class="arrow">→</span>
            </a>
            <div v-else class="inactive-msg">
              발급이 중단된 카드입니다
            </div>
          </div>
        </div>
        

        <!-- 카드 상세 정보 -->
        <div class="card-details">
          <div class="detail-row">
            <span>연회비</span>
            <span>{{ store.card.abroad_fee === 0 ? '없음' : `${formatNumber(store.card.abroad_fee)}원` }}</span>
          </div>
          <div class="separator">/</div>
          <div class="detail-row">
            <span>전월실적</span>
            <span>{{ store.card.pre_month_perform }}</span>
          </div>
        </div>

        <!-- 추가 정보 -->
        <div class="additional-info">
          <span class="visa-tag">VISA</span>
          <span class="online-tag">ONLINE ONLY</span>
          <span class="type-tag">온라인발급 전용 카드</span>
        </div>

        <!-- 카드사 버튼 -->
    
      </div>
    </div>

    <!-- 혜택 섹션 -->
    <div class="benefits-section">
      <h2>카드 혜택</h2>
      <div class="benefits-list">
        <div v-for="benefit in store.card.benefits"
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
import {computed, onMounted} from 'vue'
import { useRoute } from 'vue-router'
import { useCardStore } from "@/stores/cards"

const route = useRoute()
const store = useCardStore()

const cardData = computed(() => store.card)

const formatNumber = (number) => {
  return number?.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

const formatDetail = (detail) => {
  return detail?.replace(/\n/g, '<br>')
}

onMounted(async () => {
  console.log('Route params:', route.params)
  const { type, cardId } = route.params
  await store.getCardDetail(type, cardId)
  console.log('Card data:', store.card)
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
  align-items: center;
}

.card-image-container {
  position: relative;
  width: 300px;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center; /* 세로 중앙 정렬 */
}

.circle-bg {
  position: absolute; /* 카드 뒤에 배경을 배치 */
  transform: translateX(-50%, 50%);
  width: 200px; /* 원의 너비 */
  height: 200px; /* 원의 높이 (정사각형) */
  background-color: #f3f3f3; /* 원 배경색 */
  border-radius: 50%; /* 원 형태로 만듦 */
  z-index: 0; /* 카드보다 뒤로 배치 */
}

.card-image {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-image img {
  max-width: 100%; /* 부모 너비에 맞게 조정 */
  max-height: 100%; /* 부모 높이에 맞게 조정 */
  object-fit: contain; /* 이미지 비율 유지 */
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

.card-info {
  flex: 1;
}


.main-benefits {
  display: flex;
  flex-direction: column; /* 혜택 리스트는 세로 정렬 */
  gap: 0.5rem; /* 혜택 아이템 간 간격 */
}

.action-button {
  flex-shrink: 0; /* 버튼 크기를 고정 */
  text-align: right; /* 버튼 내용 오른쪽 정렬 */
  margin-right: 30px; /* 왼쪽으로 20px 당기기 */
  align-items: center; /* 세로 중앙 정렬 */
}

.bank-btn {
  display: inline-block;
  /* padding: 0.5rem 1rem; */
  width: 270px;
  height: 50px;
  text-decoration: none; /* 밑줄 제거 */
  background-color: #4C6EF5; /* 버튼 배경색 */
  color: white; /* 텍스트 색상 */
  border-radius: 10px; /* 버튼 모서리 둥글게 */
  font-weight: bold; /* 굵은 텍스트 */
  font-size: 22px;
  align-items: center; /* 텍스트를 세로 중앙 정렬 */
  text-align: center;
  justify-content: center;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.bank-btn:hover {
  background-color: #4e2db8; /* 호버 시 배경색 변경 */
  color: #eaeaff; /* 호버 시 텍스트 색상 변경 */
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