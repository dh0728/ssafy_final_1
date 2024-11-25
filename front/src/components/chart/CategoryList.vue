<template>
  <div class="category-list-container">
    <div v-if="selectedCategory" class="list-header">
      <div>
        <h3>{{ getCategoryName(selectedCategory.category_id) }} 상세 내역</h3>
        <div class="total-info">
          총 {{ selectedCategory.details.length }}건 
        </div>
      </div>
      
      <div class="actions">
        <button class="write-btn" @click="go_history">가계부 수정하기 📝</button>
      </div>
      
    </div>
    

    <div v-if="selectedCategory" class="table-container">
      <table class="history-table">
        <thead>
        <tr>
          <th>날짜</th>
          <th>카테고리</th>
          <th>결제수단</th>
          <th>거래처</th>
          <th>금액</th>
          <th>메모</th>
        </tr>
        </thead>
        <tbody class="scrollable-tbody">
        <tr v-for="detail in selectedCategory.details" :key="detail.day">
          <td>{{ detail.day }}일</td>
          <td>{{ getCategoryName(selectedCategory.category_id) }}</td>
          <td>{{ detail.payment }}</td>
          <td>{{ detail.store }}</td>
          <td class="amount">{{ formatNumber(detail.account) }}원</td>
          <td>{{ truncateMemo(detail.memo) }}</td>
        </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="no-data">
      <p>카테고리를 선택하면 상세 내역이 표시됩니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useCategoryChartStore } from '@/stores/categoryChart'

const selectedCategory = ref(null)

const router = useRouter()

const categories = ref([
  { id: 1, name: '🏬 모든가맹점' },
  { id: 2, name: '🚍 교통' },
  { id: 3, name: '⛽ 주유' },
  { id: 4, name: '📱 통신' },
  { id: 5, name: '🛒 마트/편의점' },
  { id: 6, name: '🎁 쇼핑' },
  { id: 7, name: '🍛 푸드' },
  { id: 8, name: '☕ 카페/디저트' },
  { id: 9, name: '💄 뷰티/피트니스' },
  { id: 10, name: '💰 무실적' },
  { id: 11, name: '📃 공과금/렌탈' },
  { id: 12, name: '🏥 병원/약국' },
  { id: 13, name: '🐱 애완동물' },
  { id: 14, name: '✏ 교육/육아' },
  { id: 15, name: '🚗 자동차/하이패스' },
  { id: 16, name: '⚽ 레저/스포츠' },
  { id: 17, name: '🎬 영화/문화' },
  { id: 18, name: '🤳 간편결제' },
  { id: 19, name: '✈ 항공마일리지' },
  { id: 20, name: '💺 공항라운지/PP' },
  { id: 21, name: '💎 프리미엄' },
  { id: 22, name: '🧳 여행/숙박' },
  { id: 23, name: '🌏 해외' },
  { id: 24, name: '💼 비지니스' },
  { id: 25, name: '🎸 기타' },
  { id: 26, name: '💸 금융' },
  { id: 27, name: '🏃‍♂️ 생활' },
])

const go_history = () => {
  return router.push({name: 'CalendarHistory'})
}

const getCategoryName = (id) => {
  const category = categories.value.find(cat => cat.id === id)
  return category ? category.name : '기타'
}

const formatNumber = (value) => new Intl.NumberFormat('ko-KR').format(value)

// 이벤트 핸들러 추가
const updateSelectedCategory = (category) => {
  selectedCategory.value = category
}

const truncateMemo = (memo) => {
  return memo.length > 15 ? memo.slice(0, 10) + '...' : memo;
}

// CategoryChart에서 emit할 이벤트를 받아서 처리하도록 expose
defineExpose({
  updateSelectedCategory
})
</script>

<style scoped>

h3 {
  margin-bottom: 5px;
}
.category-list-container {
  padding: 20px;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;
  margin-bottom: 20px;
}

.total-info {
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.table-container {
  overflow-x: auto;
}

.history-table {
  width: 100%;
  border-collapse: collapse;
}

.history-table th,
.history-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.history-table th {
  font-weight: 500;
  color: #666;
  background: #f8f9fa;
}

.amount {
  font-weight: 500;
  color: #FF8E99;
}

.no-data {
  text-align: center;
  padding: 40px;
  color: #666;
}

.scrollable-tbody {
  display: block;
  max-height: 480px; /* 원하는 높이 설정 */
  overflow-y: auto; /* 수직 스크롤 활성화 */
}

.history-table thead,
.scrollable-tbody tr {
  display: table;
  width: 100%;
  table-layout: fixed; /* 고정된 테이블 레이아웃을 유지하기 위해 설정 */
}

.history-table {
  width: 100%;
}

.scrollable-tbody {
  width: 100%;
}

/* 스크롤바 숨기기 */
.scrollable-tbody::-webkit-scrollbar {
  display: none; /* 웹킷 기반 브라우저에서 스크롤바 숨기기 */
}

.scrollable-tbody {
  -ms-overflow-style: none;  /* IE 및 Edge에서 스크롤바 숨기기 */
  scrollbar-width: none; /* Firefox에서 스크롤바 숨기기 */
}

.write-btn {
  padding: 8px 16px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}

</style>