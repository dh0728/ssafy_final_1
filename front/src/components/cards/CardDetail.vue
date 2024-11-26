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
          </div>
          <h1>{{ getCardName }}</h1>
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
          <div class="separator"></div>
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
            <!-- 카테고리별 아이콘 동적 할당 -->
            <div class="benefit-icon">
              {{ getCategoryIcon(benefit.title) }}
            </div>
            <h3>{{ benefit.title }}</h3>
            <span class="toggle-btn">></span>
          </div>
          <div class="benefit-content">
            <p>{{ benefit.desc }}</p>
            <div class="benefit-detail" v-if="benefit.desc_detail" v-html="formatDetail(benefit.desc_detail)"></div>
          </div>
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

const getCategoryIcon = (category) => {
  const iconMap = {
  // 모든가맹점
  '국내외가맹점': '🏬',
  '모든가맹점': '🏬',

  // 교통
  '대중교통': '🚍',
  '고속버스': '🚍',
  '기차': '🚆',
  '교통': '🚍',
  '택시': '🚖',

  // 주유
  '주유소': '⛽',
  '주유': '⛽',
  '충전소': '⛽',

  // 통신
  'KT': '📱',
  'SKT': '📱',
  'LGU+': '📱',
  '통신': '📱',

  // 마트/편의점
  '편의점': '🛒',
  '대형마트': '🛒',
  'SSM': '🛒',
  '마트/편의점': '🛒',
  '전통시장': '🛒',

  // 쇼핑
  '쇼핑': '🎁',
  '홈쇼핑': '🎁',
  '온라인쇼핑': '🛍️',
  '소셜커머스': '🛍️',
  '아울렛': '🛍️',
  '백화점': '🛍️',
  '인테리어': '🛋️',
  'SPA브랜드': '👗',
  '면세점': '🛍️',

  // 푸드
  '저녁': '🍛',
  '일반음식점': '🍛',
  '패스트푸드': '🍔',
  '점심': '🍛',
  '패밀리레스토랑': '🍽️',
  '푸드': '🍛',
  '배달앱': '📲',

  // 카페/디저트
  '카페/디저트': '☕',
  '베이커리': '🥐',
  '카페': '☕',

  // 뷰티/피트니스
  '피트니스': '💪',
  '화장품': '💄',
  '드럭스토어': '💊',
  '헤어': '💇‍♀️',
  '뷰티/피트니스': '💄',

  // 무실적
  '적립': '💰',
  '해피포인트': '🎉',
  '무이자할부': '💸',
  '혜택 프로모션': '🎁',
  '무실적': '💰',
  '멤버십포인트': '🪙',
  '캐시백': '💸',
  'CJ ONE': '🎉',
  '지역': '🌍',
  '연회비지원': '💳',
  'BC TOP': '🔝',
  '할인': '💸',
  '제휴/PLCC': '🤝',
  'OK캐쉬백': '💳',

  // 공과금/렌탈
  '렌탈': '📃',
  '공과금/렌탈': '📃',
  '공과금': '📃',

  // 병원/약국
  '약국': '💊',
  '병원': '🏥',
  '병원/약국': '🏥',

  // 애완동물
  '동물병원': '🐾',
  '애완동물': '🐱',

  // 교육/육아
  '교육/육아': '✏️',
  '국민행복': '👶',
  '학원': '📚',
  '학습지': '📖',
  '어린이집': '🏫',
  '문화센터': '🏛️',
  '유치원': '🏫',
  '아이행복': '👶',

  // 자동차/하이패스
  '하이브리드': '🚗',
  '자동차/하이패스': '🚗',
  '자동차': '🚗',
  '하이패스': '🛣️',
  '정비': '🛠️',

  // 레저/스포츠
  '경기관람': '⚽',
  '골프': '🏌️‍♂️',
  '게임': '🎮',
  '레저/스포츠': '⚽',
  '테마파크': '🎢',

  // 영화/문화
  '공연/전시': '🎭',
  '음원사이트': '🎶',
  '도서': '📚',
  '영화': '🎬',
  '영화/문화': '🎬',

  // 간편결제
  '간편결제': '🤳',
  '네이버페이': '💳',
  '카카오페이': '💳',
  '삼성페이': '💳',
  'APP': '📱',

  // 항공마일리지
  '아시아나항공': '✈️',
  '대한항공': '✈️',
  '제주항공': '✈️',
  '항공마일리지': '✈️',
  '저가항공': '✈️',
  '진에어': '✈️',

  // 공항라운지/PP
  '라운지 키': '💺',
  '공항라운지': '💺',
  'PP': '💺',
  '공항라운지/PP': '💺',

  // 프리미엄
  '바우처': '💎',
  '프리미엄': '💎',
  '프리미엄 서비스': '💎',

  // 여행/숙박
  '여행사': '🧳',
  '항공권': '✈️',
  '온라인 여행사': '🧳',
  '여행/숙박': '🏨',
  '렌터카': '🚙',
  '리조트': '🏝️',
  '공항': '✈️',
  '호텔': '🏨',

  // 해외
  '해외직구': '🌏',
  '수수료우대': '💸',
  '해외이용': '🌏',
  '해외': '🌏',

  // 비지니스
  '비즈니스': '💼',

  // 기타
  '기타': '🎸',
  '선택형': '🎸',

  // 금융
  '보험': '💸',
  '은행사': '🏦',
  '카드사': '💳',
  '보험사': '💸',
  '금융': '💸',

  // 생활
  '생활': '🏃‍♂️',
  '디지털구독': '📱',
  '직장인': '💼'
  }
  return iconMap[category] || '💰' // 매핑되지 않은 카테고리는 기본 아이콘 반환
}

const cardData = computed(() => store.card)

const getCardName = computed(() => {
  return store.card.credit_card_name || store.card.check_card_name
})

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

.benefits-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.benefit-item {
  border: 1px solid #eee;
  border-radius: 12px;
  overflow: hidden;
}

.benefit-header {
  display: flex;
  align-items: center;
  padding: 16px 20px;
  background: #f8f9fa;
  cursor: pointer;
}

.benefit-icon {
  font-size: 20px;
  margin-right: 12px;
}

.benefit-header h3 {
  flex: 1;
  font-size: 16px;
  font-weight: 600;
  color: #333;
  margin: 0;
}

.toggle-btn {
  color: #666;
  transform: rotate(90deg);
}

.benefit-content {
  padding: 16px 20px;
  border-top: 1px solid #eee;
}

.benefit-content p {
  color: #495057;
  font-size: 14px;
  line-height: 1.5;
  margin: 0;
}

.benefit-detail {
  margin-top: 12px;
  color: #666;
  font-size: 13px;
  line-height: 1.6;
}

.benefit-item:hover {
  border-color: #4C6EF5;
  box-shadow: 0 2px 8px rgba(76, 110, 245, 0.1);
}
</style>