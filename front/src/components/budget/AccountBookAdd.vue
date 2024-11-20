<!-- ScheduleAddModal.vue -->
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
          <select v-model="category" class="select-field">
            <option value="">선택</option>
          </select>
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

      <button class="add-account-btn">
        다른 가계부 내역에 추가 +
      </button>

      <button class="submit-btn">작성 완료</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const isOpen = ref(false)
const amount = ref('')
const type = ref('expense')
const category = ref('')
const paymentMethod = ref('')
const storeName = ref('')
const memo = ref('')

const currentDate = computed(() => {
  const date = new Date()
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
  border: none;
  background: transparent;
  font-size: 16px;
  outline: none;
  text-align: right;
  padding-right: 50px;
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
</style>