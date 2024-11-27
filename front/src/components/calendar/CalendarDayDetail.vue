<template>
  <div v-if="isOpen" class="modal-overlay" @click="closeModal">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h3>{{ formattedDate }} 가계부 내역</h3>
        <button class="close-btn" @click="closeModal">×</button>
      </div>

      <div v-if="dayData && dayData.length > 0">
        <div class="total-amount">
          총 {{ dayData.length }}건
        </div>

        <!-- 테이블 형식으로 변경 -->
        <div class="table-container">
          <table class="history-table">
            <thead>
            <tr>
              <th>분류</th>
              <th>날짜</th>
              <th>카테고리</th>
              <th>결제수단</th>
              <th>거래처</th>
              <th>금액</th>
              <th>메모</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in dayData" :key="item.id">
              <td>
                  <span :class="['type-badge', item.is_income ? 'income' : 'expense']">
                    {{ item.is_income ? '수입' : '지출' }}
                  </span>
              </td>
              <td>{{ formattedDate }}</td>
              <td>{{ getCategoryName(item.category_id) }}</td>
              <td>{{ item.payment }}</td>
              <td>{{ item.store }}</td>
              <td :class="['amount', item.is_income ? 'income' : 'expense']">
                {{ formatNumber(item.account) }}원
              </td>
              <td>{{ truncateMemo(item.memo) }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div v-else class="no-data">
        <p>해당 날짜의 내역이 없습니다.</p>
      </div>


        <div class="modal-footer">
        <button class="detail-btn" @click="goToDetail">내역 수정하러 가기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  selectedDate: {
    type: [Date, null],
    default: null
  },
  dayData: {
    type: Array,
    default: () => []
  },
  isOpen: {
    type: Boolean,
    default: false
  }
})

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

const getCategoryName = (id) => {
  const category = categories.value.find(cat => cat.id === id)
  return category ? category.name : '기타'
}

const emit = defineEmits(['close'])
const router = useRouter()

const formattedDate = computed(() => {
  if (!props.selectedDate) return ''
  return `${props.selectedDate.getMonth() + 1}월 ${props.selectedDate.getDate()}일`
})

const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

const truncateMemo = (memo) => {
  return memo.length > 15 ? memo.slice(0, 18) + '...' : memo;
}


const closeModal = () => {
  emit('close')
}

const goToDetail = () => {
  router.push('/history')
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  width: 90%;
  max-width: 1000px;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-header {
  padding: 20px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.total-amount {
  padding: 16px 20px;
  font-size: 14px;
  color: #666;
  border-bottom: 1px solid #eee;
}

.table-container {
  padding: 20px;
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
}

.type-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.type-badge.income {
  color: #1BBF83;
  border: 1px solid #1BBF83;
}

.type-badge.expense {
  color: #FF8E99;
  border: 1px solid #FF8E99;
}

.amount {
  font-weight: 500;
}

.amount.income {
  color: #1BBF83;
}

.amount.expense {
  color: #FF8E99;
}

.modal-footer {
  padding: 20px;
  text-align: center;
  border-top: 1px solid #eee;
}

.detail-btn {
  padding: 12px 24px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.detail-btn:hover {
  background: #4263eb;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}

.no-data {
  padding: 40px 20px;
  text-align: center;
  color: #666;
}
</style>