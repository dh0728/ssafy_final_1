<template>
  <div v-if="isOpen" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <div>
          <h2>{{ currentMonth }}월 예산 설정</h2>
          <p class="subtitle">이번 달도 잘 해내실거라고 생각해요! 저희가 응원합니다 💪</p>
        </div>
        <button class="close-btn" @click="closeModal">×</button>
      </div>

      <div class="budget-input">
        <input
            type="text"
            v-model="inputBudget"
            @input="onlyNumbers"
            placeholder="0"
            class="amount-input"
        >
        <span class="currency">원</span>
      </div>

<!--      <div class="budget-info">-->
<!--        <div class="info-row">-->
<!--          <span>지난 달 예산</span>-->
<!--          <span>{{ formatNumber(lastMonthBudget) }}원</span>-->
<!--        </div>-->
<!--        <div class="info-row">-->
<!--          <span>결과</span>-->
<!--          <span class="result">{{ formatNumber(remainingBudget) }}원 남음</span>-->
<!--        </div>-->
<!--      </div>-->

      <button class="submit-btn" @click="submitBudget">예산 수정</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useBudgetStore } from '@/stores/budget'

const emit = defineEmits(['budget-updated'])
const budgetStore = useBudgetStore()
const isOpen = ref(false)
const inputBudget = ref('')

const currentMonth = computed(() => {
  return new Date().getMonth() + 1
})

const onlyNumbers = (e) => {
  let value = e.target.value
  value = value.replace(/[^0-9]/g, '')
  value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  inputBudget.value = value
}

const submitBudget = async () => {
  const amount = Number(inputBudget.value.replace(/,/g, ''))
  const success = await budgetStore.setBudget(amount)
  if (success) {
    emit('budget-updated', amount)
    closeModal()
  }
}

const openModal = () => {
  isOpen.value = true
}

const closeModal = () => {
  isOpen.value = false
  inputBudget.value = ''
}

defineExpose({ openModal, closeModal })
</script>

<style scoped>
.subtitle {
  color: #666;
  font-size: 14px;
  margin-top: 8px;
}

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
  font-size: 20px;
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

.budget-input {
  position: relative;
  margin-bottom: 24px;
}

.amount-input {
  width: 100%;
  box-sizing: border-box; /* 추가 */
  padding: 12px 40px 12px 12px; /* 패딩 조정 */
  font-size: 20px; /* 폰트 크기 조정 */
  font-weight: 500;
  border: none;
  background: #f8f9fa;
  border-radius: 8px;
  text-align: right;
  outline: none;
}

.currency {
  position: absolute;
  right: 12px; /* 위치 조정 */
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  font-size: 14px; /* 폰트 크기 조정 */
}

.budget-info {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 24px;
}

.info-row {
  display: flex;
  justify-content: space-between;
  color: #666;
  font-size: 14px;
  padding: 8px 0;
}

.info-row:first-child {
  margin-bottom: 8px;
}

.result {
  color: #4C6EF5;
}

.submit-btn {
  width: 100%;
  padding: 16px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.submit-btn:hover {
  background: #4263eb;
}

.amount-input::placeholder {
  color: #999;
}
</style>