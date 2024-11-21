<template>
  <div v-if="isOpen" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h2>{{ currentDate }} 가계부 작성</h2>
        <button class="close-btn" @click="closeModal">×</button>
      </div>

      <div class="amount-input">
        <input
            type="text"
            v-model="amount"
            @input="onlyNumbers"
            placeholder="0"
            class="input-field"
        >
        <span class="currency">원</span>
        <button class="edit-btn">✎</button>
      </div>

      <div class="type-selector">
        <button
            class="type-btn"
            :class="{ active: type === 'expense' }"
            @click="type = 'expense'"
        >지출</button>
        <button
            class="type-btn"
            :class="{ active: type === 'income' }"
            @click="type = 'income'"
        >수입</button>
      </div>

      <div class="form-group">
        <div class="form-item">
          <label>카테고리</label>
          <div class="select-wrapper" @click="showCategoryModal = true">
            <input
                type="text"
                :value="category"
                readonly
                placeholder="선택해주세요"
                class="input-field"
            >
            <span class="select-arrow">▼</span>
          </div>
        </div>

        <div class="form-item">
          <label>결제 수단</label>
          <select v-model="paymentMethod" class="select-field">
            <option value="">선택</option>
          </select>
        </div>

        <div class="form-item">
          <label>가게명</label>
          <input type="text" v-model="storeName" placeholder="입력해주세요" class="input-field">
        </div>

        <div class="form-item">
          <label>메모</label>
          <input type="text" v-model="memo" placeholder="입력해주세요" class="input-field">
        </div>
      </div>

      <button class="submit-btn">작성 완료</button>

      <div v-if="showCategoryModal" class="category-modal">
        <div class="category-modal-content">
          <div class="modal-header">
            <h3>카테고리 선택</h3>
            <button class="close-btn" @click="showCategoryModal = false">×</button>
          </div>
          <div class="category-list">
            <button
                v-for="selectedCategory in categories"
                :key="selectedCategory.id"
                class="category-item"
                @click="selectCategory(selectedCategory)"
            >
              {{ selectedCategory.name }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  selectedDate: {
    type: Date,
    required: true
  }
})

const isOpen = ref(false)
const amount = ref('')
const type = ref('expense')
const category = ref('')
const paymentMethod = ref('')
const storeName = ref('')
const memo = ref('')

const showCategoryModal = ref(false)
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




const currentDate = computed(() => {
  if (!props.selectedDate) return ''
  const date = props.selectedDate
  return `${date.getMonth() + 1}월 ${date.getDate()}일`
})

const onlyNumbers = (e) => {
  let value = e.target.value
  value = value.replace(/[^0-9]/g, '')
  value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  amount.value = value
}

const openModal = () => {
  isOpen.value = true
}

const closeModal = () => {
  isOpen.value = false
  resetForm()
}

const resetForm = () => {
  amount.value = ''
  type.value = 'expense'
  category.value = ''
  paymentMethod.value = ''
  storeName.value = ''
  memo.value = ''
}

const selectCategory = (cat) => {
  category.value = cat.name
  showCategoryModal.value = false
}

defineExpose({ openModal, closeModal })
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
  border-radius: 16px;
  padding: 24px;
  width: 360px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.modal-header h2 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}

.amount-input {
  position: relative;
  margin-bottom: 24px;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 12px;
  display: flex;
  align-items: center;
}

.input-field {
  width: 100%;
  height: 40px;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  box-sizing: border-box;
}

.currency {
  position: absolute;
  right: 40px;
  color: #666;
}

.edit-btn {
  background: none;
  border: none;
  color: #666;
  cursor: pointer;
  padding: 4px;
}

.type-selector {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.type-btn {
  flex: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.type-btn.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}

.form-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-item label {
  font-size: 14px;
  color: #666;
}

.select-field,
.input-field {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.add-account-btn {
  width: 100%;
  padding: 12px;
  background: #f8f9fa;
  border: none;
  border-radius: 8px;
  color: #4C6EF5;
  font-size: 14px;
  cursor: pointer;
  margin-bottom: 16px;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

.select-wrapper {
  position: relative;
  cursor: pointer;
}

.select-arrow {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  pointer-events: none;
}

.category-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1100;
}

.category-modal-content {
  background: white;
  border-radius: 16px;
  padding: 24px;
  width: 300px;
}

.category-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-top: 16px;
}

.category-item {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}

.category-item:hover {
  background: #f8f9fa;
  border-color: #4C6EF5;
  color: #4C6EF5;
}
</style>