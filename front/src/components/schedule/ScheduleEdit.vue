<template>
  <div v-if="isOpen" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h2>금융 일정 수정</h2>
        <button class="close-btn" @click="closeModal">×</button>
      </div>

      <div class="form-group">
        <div class="form-item">
          <label>날짜</label>
          <div class="date-input">
            <input type="text" v-model="formData.day" class="month-input">
            <span>일</span>
          </div>
        </div>

        <div class="form-item">
          <label>분류</label>
          <div class="type-buttons">
            <button
                :class="['type-btn', { active: !formData.is_income }]"
                @click="formData.is_income = false"
            >지출</button>
            <button
                :class="['type-btn', { active: formData.is_income }]"
                @click="formData.is_income = true"
            >수입</button>
          </div>
        </div>

        <div class="form-item">
          <label>일정 이름</label>
          <input type="text" v-model="formData.name" class="input-field">
        </div>

        <div class="form-item">
          <label>금액</label>
          <input
              type="text"
              v-model="amount"
              @input="onlyNumbers"
              class="input-field"
          >
          <p class="amount-note">* 정기적인 지출, 수입을 저장해두고, 효과적으로 관리해보세요!</p>
        </div>
      </div>

      <button class="submit-btn" @click="updateSchedule">
        +
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useScheduleStore } from '@/stores/schedule.js'

const props = defineProps({
  schedule: Object
})

const emit = defineEmits(['schedule-updated'])
const store = useScheduleStore()
const isOpen = ref(false)
const amount = ref('')

const formData = ref({
  name: '',
  day: '',
  value: 0,
  category_id: 1,
  is_income: false,
  schedule_id: ''
})

watch(() => props.schedule, (newSchedule) => {
  if (newSchedule) {
    formData.value = { ...newSchedule }
    amount.value = newSchedule.value.toLocaleString()
  }
}, { deep: true })

const onlyNumbers = (e) => {
  let value = e.target.value
  value = value.replace(/[^0-9]/g, '')
  value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  amount.value = value
  formData.value.value = Number(value.replace(/,/g, ''))
}

const updateSchedule = async () => {
  const success = await store.updateSchedule(formData.value)
  if (success) {
    emit('schedule-updated')
    closeModal()
  }
}

const openModal = () => {
  isOpen.value = true
}

const closeModal = () => {
  isOpen.value = false
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