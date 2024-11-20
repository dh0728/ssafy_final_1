<template>
  <div class="schedule-container">
    <div class="schedule-header">
      <h3>다가오는 금융 일정 📅</h3>
    </div>
    <div class="schedule-list">
      <div class="schedule-item">
        <div class="date">5일</div>
        <div class="schedule-content">
          <div class="title">넷플</div>
          <div class="amount">5,900원 / 지출</div>
        </div>
      </div>
      <div class="schedule-item">
        <div class="date">15일</div>
        <div class="schedule-content">
          <div class="title">월급</div>
          <div class="amount">100,000원 / 수입</div>
        </div>
      </div>
    </div>
    <button class="add-schedule-btn" @click="openScheduleModal">금융 일정 추가하기</button>
    <ScheduleAdd ref="scheduleModal" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ScheduleAdd from './ScheduleAdd.vue'

const scheduleModal = ref(null)

const openScheduleModal = () => {
  scheduleModal.value.openModal()
}
</script>

<style scoped>
.schedule-container {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 280px;
  margin-left: 24px;
}

.schedule-header {
  margin-bottom: 20px;
}

.schedule-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1438;
  margin: 0;
}

.schedule-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

.schedule-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
  border-radius: 8px;
  background: #f8f9fa;
}

.date {
  background: #1BBF83;
  color: white;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  min-width: 45px;
  text-align: center;
}

.schedule-content {
  flex: 1;
}

.title {
  font-size: 14px;
  font-weight: 500;
  color: #1a1438;
  margin-bottom: 4px;
}

.amount {
  font-size: 13px;
  color: #666;
}

.add-schedule-btn {
  width: 100%;
  padding: 12px;
  background: #f8f9fa;
  border: none;
  border-radius: 8px;
  color: #4C6EF5;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.add-schedule-btn:hover {
  background: #f1f3f5;
}
</style>