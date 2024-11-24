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
  padding: 32px;
}

.card-basic-info {
  display: flex;
  gap: 56px;  /* 48px에서 증가 */
  margin-bottom: 32px;
  padding: 40px;  /* 32px에서 증가 */
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.card-image-container {
  width: 400px;  /* 320px에서 증가 */
  height: 260px; /* 200px에서 증가 */
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f8f9fa;
  border-radius: 16px;  /* 더 부드러운 모서리 */
  transition: transform 0.3s ease;
  padding: 20px;  /* 여백 추가 */
  margin-top: 40px;
}

.card-image-container:hover {
  transform: translateY(-4px);
}

.card-image {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.card-info {
  flex: 1;
}

.info-header {
  margin-bottom: 24px;
}

.cashback-tag {
  display: inline-block;
  padding: 6px 16px;
  background: #f3f0ff;
  color: #845ef7;
  border-radius: 20px;
  font-size: 14px;
  margin-bottom: 16px;
}

.card-info h1 {
  font-size: 24px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 8px;
}

.brand {
  color: #666;
  font-size: 16px;
  margin-bottom: 24px;
}

.main-benefits {
  margin: 24px 0;
}

.benefit-icon {
  padding: 12px 16px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 8px;
  font-size: 15px;
  color: #495057;
}

.bank-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 48px;
  background: #4C6EF5;
  color: white;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(76, 110, 245, 0.2);
}

.bank-btn:hover {
  background: #4263eb;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 110, 245, 0.3);
}

.card-details {
  display: flex;
  align-items: center;
  gap: 24px;
  margin: 24px 0;
  padding: 16px 0;
  border-top: 1px solid #eee;
  border-bottom: 1px solid #eee;
}

.detail-row {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.detail-row span:first-child {
  font-size: 14px;
  color: #666;
}

.detail-row span:last-child {
  font-size: 16px;
  font-weight: 500;
  color: #1a1438;
}

.separator {
  width: 1px;
  height: 40px;
  background: #eee;
}

.additional-info {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.visa-tag,
.online-tag,
.type-tag {
  padding: 4px 12px;
  background: #f8f9fa;
  border-radius: 20px;
  font-size: 13px;
  color: #666;
}

.benefits-section {
  background: white;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.benefits-section h2 {
  font-size: 20px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 24px;
}

.benefit-item {
  padding: 24px;
  border: 1px solid #eee;
  border-radius: 12px;
  margin-bottom: 16px;
  transition: all 0.2s ease;
}

.benefit-item:hover {
  border-color: #4C6EF5;
  box-shadow: 0 2px 8px rgba(76, 110, 245, 0.1);
}

.benefit-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 8px;
}

.benefit-desc {
  color: #495057;
  font-size: 15px;
  line-height: 1.5;
}

.benefit-detail {
  margin-top: 16px;
  font-size: 14px;
  color: #666;
  line-height: 1.6;
}
</style>