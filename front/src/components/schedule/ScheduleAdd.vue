<!-- ScheduleAddModal.vue -->
<template>
  <div v-if="isOpen" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h2>금융 일정 추가</h2>
        <button class="close-btn" @click="closeModal">×</button>
      </div>

      <div class="form-group">
        <div class="form-item">
          <label>날짜</label>
          <div class="date-input">
            <input type="text" v-model="month" class="month-input" placeholder="매달">
            <span>일</span>
          </div>
        </div>

        <div class="form-item">
          <label>분류</label>
          <div class="type-buttons">
            <button
                :class="['type-btn', { active: type === 'expense' }]"
                @click="type = 'expense'"
            >지출</button>
            <button
                :class="['type-btn', { active: type === 'income' }]"
                @click="type = 'income'"
            >수입</button>
          </div>
        </div>

        <div class="form-item">
          <label>일정 이름</label>
          <input type="text" v-model="scheduleName" class="input-field">
        </div>

        <div class="form-item">
          <label>금액</label>
          <input
              type="text"
              v-model="amount"
              @input="onlyNumbers"
              placeholder="0"
              class="input-field"
          >
          <p class="amount-note">* 정기적인 지출, 수입을 저장해두고, 효과적으로 관리해보세요!</p>
        </div>
      </div>

      <button class="submit-btn" @click="addSchedule">
        <span class="plus-icon">+</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useScheduleStore} from "@/stores/schedule.js";

const store = useScheduleStore()
const emit = defineEmits(['schedule-added'])

const isOpen = ref(false)
const month = ref('')
const type = ref('expense')
const scheduleName = ref('')
const amount = ref('')

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
  month.value = ''
  type.value = 'expense'
  scheduleName.value = ''
  amount.value = ''
}

const addSchedule = async () => {
  try {
    const scheduleData = {
      name: scheduleName.value,
      day: Number(month.value),
      value: Number(amount.value.replace(/,/g, '')),
      category_id: 1,
      is_income: type.value === 'income'
    }

    const result = await store.addSchedule(scheduleData)
    if (result) {
      closeModal()
      emit('schedule-added')
    }
  } catch (error) {
    console.error('일정 추가 실패:', error)
  }
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

.form-group {
  display: flex;
  flex-direction: column;
  gap: 20px;
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

.date-input {
  display: flex;
  align-items: center;
  gap: 8px;
}

.month-input {
  width: 100px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
}

.type-buttons {
  display: flex;
  gap: 8px;
}

.type-btn {
  flex: 1;
  padding: 8px 16px;
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

.input-field {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 6px;
}

.amount-note {
  font-size: 12px;
  color: #666;
  margin-top: 4px;
}

.submit-btn {
  width: 48px;
  height: 48px;
  border-radius: 24px;
  background: #4C6EF5;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 24px auto 0;
}

.plus-icon {
  font-size: 24px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}
</style>