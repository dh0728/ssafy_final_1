<template>
  <div class="card-container">
    <!-- 상단 탭 -->
    <div class="tab-menu">
      <div class="tab-buttons">
        <button
            class="tab-btn"
            :class="{ active: selectedTab === 'credit' }"
            @click="changeTab('credit')"
        >신용카드</button>
        <button
            class="tab-btn"
            :class="{ active: selectedTab === 'check' }"
            @click="changeTab('check')"
        >체크카드</button>
      </div>
    </div>

    <!-- 필터 섹션 -->
    <div class="filter-section">
      <!-- 유형 필터 -->

      <!-- 혜택 필터 -->
      <div class="filter-group">
        <div class="filter-label">혜택</div>
        <swiper
            :modules="[FreeMode]"
            :slides-per-view="'auto'"
            :space-between="8"
            :free-mode="true"
            :loop="false"
            class="filter-swiper"
        >
          <swiper-slide v-for="item in category" :key="item.id">
            <button
                :class="['filter-btn', { active: selectedCategories.includes(item.id) }]"
                @click="toggleFilter('categories', item.id)"
            >
              {{ item.name }}
            </button>
          </swiper-slide>
        </swiper>
      </div>

      <!-- 카드사 필터 -->
      <div class="filter-group">
        <div class="filter-label">카드사</div>
        <swiper
            :modules="[FreeMode]"
            :slides-per-view="'auto'"
            :space-between="8"
            :free-mode="true"
            class="filter-swiper"
        >
          <swiper-slide v-for="company in cardCompany" :key="company.id">
            <button
                :class="['filter-btn', { active: selectedCompanies.includes(company.id) }]"
                @click="toggleFilter('companies', company.id)"
            >
              {{ company.name }}
            </button>
          </swiper-slide>
        </swiper>
      </div>
    </div>

    <CardList />

  </div>
</template>

<script setup>
import {onMounted, ref, watch} from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { FreeMode } from 'swiper/modules'
import 'swiper/css'
import CardList from "@/components/cards/CardList.vue";
import {useCardStore} from "@/stores/cards.js";

const store = useCardStore();

// 기본값: credit
const selectedTab = ref('credit')
const selectedCategories = ref([])
const selectedCompanies = ref([])

// 데이터는 그대로 사용
const cardCompany = ref([
  { id: 1, name: 'Sh수협은행' },
  { id: 2, name: '토스뱅크' },
  { id: 3, name: 'NH농협카드' },
  { id: 4, name: '우리카드' },
  { id: 5, name: 'BNK경남은행' },
  { id: 6, name: '현대카드' },
  { id: 7, name: 'Sc제일은행' },
  { id: 8, name: '롯데카드' },
  { id: 9, name: '전북은행' },
  { id: 10, name: '케이뱅크' },
  { id: 11, name: 'BC 바로카드' },
  { id: 12, name: '신한카드' },
  { id: 13, name: 'BNK부산은행' },
  { id: 14, name: '차이' },
  { id: 15, name: 'KB국민은행' },
  { id: 16, name: 'SSGPAY.CARD' },
  { id: 17, name: 'IBK기업은행' },
  { id: 18, name: '삼성카드' },
  { id: 19, name: '씨티카드' },
  { id: 20, name: 'DGB대구은행' },
  { id: 21, name: '하나카드' },
  { id: 22, name: '제주은행' },
  { id: 23, name: '현대백화점' },
  { id: 24, name: '광주은행' },
  { id: 25, name: '신협' },
])

const category = ref([
  { id: 1, name: '모든가맹점' },
  { id: 2, name: '교통' },
  { id: 3, name: '주유' },
  { id: 4, name: '통신' },
  { id: 5, name: '마트/편의점' },
  { id: 6, name: '쇼핑' },
  { id: 7, name: '푸드' },
  { id: 8, name: '카페/디저트' },
  { id: 9, name: '뷰티/피트니스' },
  { id: 10, name: '무실적' },
  { id: 11, name: '공과금/렌탈' },
  { id: 12, name: '병원/약국' },
  { id: 13, name: '애완동물' },
  { id: 14, name: '교육/육아' },
  { id: 15, name: '자동차/하이패스' },
  { id: 16, name: '레저/스포츠' },
  { id: 17, name: '영화/문화' },
  { id: 18, name: '간편결제' },
  { id: 19, name: '항공마일리지' },
  { id: 20, name: '공항라운지/PP' },
  { id: 21, name: '프리미엄' },
  { id: 22, name: '여행/숙박' },
  { id: 23, name: '해외' },
  { id: 24, name: '비지니스' },
  { id: 25, name: '기타' },
  { id: 26, name: '금융' },
  { id: 27, name: '생활' },
])


const toggleFilter = async (type, id) => {
  // 기존 배열 복사
  const targetRef = type === 'categories' ? selectedCategories : selectedCompanies

  const index = targetRef.value.indexOf(id)
  if (index === -1) {
    // 새로운 값 추가
    targetRef.value = [...targetRef.value, id]
  } else {
    // 기존 값 제거
    targetRef.value = targetRef.value.filter(item => item !== id)
  }

  // 필터가 선택된 경우에만 API 호출
  if (selectedCategories.value.length > 0 || selectedCompanies.value.length > 0) {
    // 새로운 API 호출 전에 store 초기화
    store.resetCards()
    await store.getCardsByCondition(
        selectedTab.value,
        [...selectedCategories.value], // 배열 복사하여 전달
        [...selectedCompanies.value]
    )
  } else {
    // 모든 필터가 해제된 경우 기본 목록 불러오기
    store.resetCards()
    await store.getCardList(selectedTab.value)
  }
}

// 탭 변경 시에도 필터 상태 고려
const changeTab = async (type) => {
  store.resetCards()
  selectedTab.value = type

  // 필터가 선택된 경우에만 조건 검색
  if (selectedCategories.value.length > 0 || selectedCompanies.value.length > 0) {
    await store.getCardsByCondition(
        type,
        selectedCategories.value,
        selectedCompanies.value
    )
  } else {
    await store.getCardList(type)
  }
}

onMounted(async () => {
  await store.getCardList(selectedTab.value)
})
</script>

<style scoped>
.card-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.tab-menu {
  margin-bottom: 2rem;
}

.tab-buttons {
  display: inline-flex;
  background: #f5f5f5;
  padding: 4px;
  border-radius: 50px;
}

.tab-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  color: #666;
  background: transparent;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-btn.active {
  background: white;
  color: #1a1438;
  font-weight: 500;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}



.company-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #f8f9fa;
  cursor: pointer;
}

.filter-section {
  background: white;
  border: 1px solid #eee;
  border-radius: 8px;
}

.filter-group {
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.filter-group:last-child {
  border-bottom: none;
}

.filter-label {
  font-weight: 500;
  margin-bottom: 0.8rem;
}

.filter-swiper {
  width: 100%;
}

:deep(.swiper-slide) {
  width: auto;
}

.filter-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #eee;
  border-radius: 20px;
  background: white;
  color: #666;
  font-size: 0.9rem;
  cursor: pointer;
  white-space: nowrap;
}

.filter-btn:hover {
  background-color: #f8f9fa;
}

.filter-btn.active {
  background-color: #1a1438;
  color: white;
  border-color: #1a1438;
}
</style>