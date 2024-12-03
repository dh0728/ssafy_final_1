<template>
  <div class="budget-view">
    <!-- 상단 헤더 -->
    <div class="header">
      <div class="user-select">
        <button class="filter-btn active">
        <span class="user-icon">👤 </span>
        <span v-if="accountStore.username">{{ accountStore.username }} 님의 가계부</span>
        <span v-else>가계부</span>
          </button>
      </div>
      <div class="actions">
        <button @click="openCalendarModal" class="write-btn">가계부 작성하기 📝</button>
      </div>
    </div>

    <!-- 예산 요약 카드 -->
    <div class="budget-card">
      <div class="budget-info">
        <div class="info-item">
          <div class="item-content">
            <span class="label">이번 달 지출</span>
            <div class="amount">{{ formatNumber(monthlyStats.expense) }}원</div>
            <RouterLink :to="{ name: 'DateChart' }" class="link">
              지출 분석하러 가기
              <span class="arrow">→</span>
            </RouterLink>
          </div>
        </div>
        <div class="divider"></div>
        <div class="info-item">
          <div class="item-content">
            <span class="label">이번 달 수입</span>
            <div class="amount">{{ formatNumber(monthlyStats.income) }}원</div>
            <RouterLink :to="{ name: 'DateChart' }" class="link">
              수입 분석하러 가기
              <span class="arrow">→</span>
            </RouterLink>
          </div>
        </div>
        <div class="divider"></div>
        <div class="info-item">
          <div class="item-content">
            <span class="label">예산</span>
            <div v-if="currentBudget" class="amount">
              {{ formatNumber(currentBudget) }}원
            </div>
            <div v-else class="amount no-budget">
              설정된 예산이 없습니다.<br>
              예산을 설정하고 계획적으로 관리 해보세요!
            </div>
            <a href="#" class="link" @click.prevent="openBudgetModal">
              예산 설정하러 가기
              <span class="arrow">→</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="calendar-schedule-container">
      <Calendar />
      <Schedule />
    </div>
    <CalendarAdd ref="calendarModal" :selected-date="new Date()" @write-completed="onWriteCompleted" />
    <BudgetSettingModal ref="budgetModal" @budget-updated="refreshBudget" />
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import { useBudgetStore } from '@/stores/budget'

import Calendar from "@/components/calendar/Calendar.vue";
import Schedule from "@/components/schedule/Schedule.vue";
import BudgetSettingModal from '@/components/budget/BudgetSetting.vue'
import {useCalendarStore} from "@/stores/calendar.js";
import {useAccountStore} from "@/stores/accounts.js";
import CalendarAdd from "@/components/calendar/CalendarAdd.vue";

const budgetModal = ref(null)
const calendarModal = ref(null)
const store = useBudgetStore()
const calendarStore = useCalendarStore();
const accountStore = useAccountStore();
const currentBudget = ref(null)
const monthlyStats = ref({
  income: 0,
  expense: 0
})

const fetchBudget = async () => {
  await accountStore.getUserInfo()

  const date = new Date()
  const year = date.getFullYear()
  const month = date.getMonth() + 1

  const budgetData = await store.getBudget()
  if (budgetData) {
    currentBudget.value = budgetData.value
  }

  const calendarData = await calendarStore.getCalendarData(year, month)
  if (calendarData) {
    monthlyStats.value = {
      income: calendarData.total_income,
      expense: calendarData.total_expenditure
    }
  }
}

// 컴포넌트 마운트 시 예산 정보 가져오기
onMounted(fetchBudget)

const openBudgetModal = () => {
  budgetModal.value.openModal()
}

const refreshBudget = (newBudget) => {
  currentBudget.value = newBudget
  fetchBudget()
}

const openCalendarModal = () => {
  calendarModal.value.openModal()
}

// 작성 완료 후 처리 함수 추가
const onWriteCompleted = () => {
  fetchBudget()
}

// 숫자 포맷팅 함수
const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}
</script>

<style scoped>
.budget-view {
  padding: 0px 20px;
  width: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-name {
  font-size: 16px;
  font-weight: 500;
  color: #1a1438;
}

.left-section input[type="checkbox"] {
  width: 18px;
  height: 18px;
  border-radius: 4px;
  border: 2px solid #ddd;
  cursor: pointer;
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

.write-btn:hover {
  background: #4263eb;
  transform: translateY(-1px);
}

.budget-card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  width: 100%;
  transition: all 0.3s;
}

.budget-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.budget-info {
  display: flex;
  min-height: 160px;
  padding: 0;
}

.info-item {
  flex: 1;
  position: relative;
  display: flex; /* 추가 */
  flex-direction: column
}

.item-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 36px 30px;
  flex: 1; /* 추가 */
}

.label {
  color: #666;
  font-size: 15px;
  margin-bottom: 12px;
}

.amount {
  font-size: 28px;
  font-weight: 600;
  color: #1a1438;
  margin: 2px 0;
}

.link {
  color: #4263eb;
  text-decoration: none;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
  margin-top: auto; /* 하단 정렬 유지 */
  position: relative; /* 추가 */
  bottom: 0;
}

.link:hover {
  color: #4263eb;
}

.arrow {
  font-size: 16px;
  transition: transform 0.2s;
}

.link:hover .arrow {
  transform: translateX(4px);
}

.divider {
  width: 1px;
  background: #f1f3f5;
  margin: 20px 0;
  align-self: stretch;
}

.amount.no-budget {
  font-size: 14px; /* label보다 작은 크기 */
  font-weight: normal;
  color: #666; /* label과 동일한 색상 */
  line-height: 1.5;
}

@media (max-width: 768px) {
  .budget-info {
    flex-direction: column;
  }

  .divider {
    width: 100%;
    height: 1px;
    margin: 0;
  }

  .info-item {
    padding: 20px;
  }
}

.calendar-schedule-container {
  display: flex;
  gap: 24px;
  margin-top: 24px;
}



.filter-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: #f8f9fa;
  border: none;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 500;
  color: #1a1438;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  background: white;
  transform: translateY(-1px);
}

.filter-btn.active {
  background: aliceblue;
  color: #9CA3AF;
}

.user-icon {
  font-size: 18px;
  color: #4C6EF5;
}

.write-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(76, 110, 245, 0.2);
}

.write-btn:hover {
  background: #4263eb;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 110, 245, 0.3);
}
</style>
