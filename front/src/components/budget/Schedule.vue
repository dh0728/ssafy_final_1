<template>
  <div class="schedule-container">
    <div class="schedule-header">
      <h3>다가오는 금융 일정 📅</h3>
    </div>
    <div class="schedule-list">
      <div v-for="schedule in schedules" :key="schedule.schedule_id" class="schedule-item">
        <div class="schedule-content-wrapper" @click="openEditModal(schedule)">
          <div class="date" :style="{ background: schedule.is_income ? '#1BBF83' : '#ff6b6b' }">
            {{ schedule.day }}일
          </div>
          <div class="schedule-content">
            <div class="title">{{ schedule.name }}</div>
            <div class="amount">
              {{ formatNumber(schedule.value) }}원 / {{ schedule.is_income ? '수입' : '지출' }}
            </div>
          </div>
        </div>
        <button class="delete-btn" @click.stop.prevent="deleteSchedule(schedule.schedule_id)">×</button>
      </div>
    </div>
    <button class="add-schedule-btn" @click="openScheduleModal">금융 일정 추가하기</button>
    <ScheduleAdd ref="scheduleModal" @schedule-added="fetchSchedules" />
    <ScheduleEdit ref="editModal" :schedule="selectedSchedule" @schedule-updated="fetchSchedules" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useScheduleStore } from '@/stores/schedule'
import ScheduleAdd from './ScheduleAdd.vue'
import ScheduleEdit from './ScheduleEdit.vue'

const store = useScheduleStore()
const scheduleModal = ref(null)
const schedules = ref([])

const openScheduleModal = () => {
  scheduleModal.value.openModal()
}

const fetchSchedules = async () => {
  const result = await store.getSchedules()
  if (result) {
    schedules.value = result
  }
}

const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

onMounted(() => {
  fetchSchedules()
})

const deleteSchedule = async (scheduleId) => {
  if (confirm('정말 삭제하시겠습니까?')) {
    const success = await store.deleteSchedule(scheduleId)
    if (success) {
      await fetchSchedules()
    }
  }
}

const editModal = ref(null)
const selectedSchedule = ref(null)

const openEditModal = (schedule) => {
  selectedSchedule.value = schedule
  editModal.value.openModal()
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

.schedule-content-wrapper {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  flex: 1;
  cursor: pointer;
}

.schedule-item {
  display: flex;
  align-items: flex-start;
  padding: 12px;
  border-radius: 8px;
  background: #f8f9fa;
  position: relative;
}

.date {
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

.delete-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: none;
  border: none;
  color: #666;
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  transition: all 0.2s;
  z-index: 2; /* 삭제 버튼을 더 위로 올림 */
}

.delete-btn:hover {
  color: #ff6b6b;
  background: rgba(255, 107, 107, 0.1); /* 호버 시 배경색 추가 */
}
</style>