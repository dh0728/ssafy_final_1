<template>
  <div class="calendar-container">
    <div class="calendar-header">
      <div class="month-selector">
        <span>{{ currentMonthLabel }}</span>
        <div class="calendar-legend">
          <span class="income">● 수입</span>
          <span class="expense">● 지출</span>
        </div>
      </div>
      <div class="month-controls">
        <button class="control-btn" @click="prevMonth">←</button>
        <button class="control-btn" @click="nextMonth">→</button>
      </div>

    </div>

    <FullCalendar
        ref="calendarRef"
        :options="calendarOptions"
        class="calendar"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

const calendarRef = ref(null)
const currentDate = ref(new Date())

const currentMonthLabel = computed(() => {
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long'
  }).format(currentDate.value)
})

const prevMonth = () => {
  const calendarApi = calendarRef.value.getApi()
  calendarApi.prev()
  currentDate.value = calendarApi.getDate()
}

const nextMonth = () => {
  const calendarApi = calendarRef.value.getApi()
  calendarApi.next()
  currentDate.value = calendarApi.getDate()
}

const calendarOptions = ref({
  plugins: [dayGridPlugin, interactionPlugin],
  initialView: 'dayGridMonth',
  locale: 'ko',
  headerToolbar: false,
  dayHeaderFormat: { weekday: 'short' },
  height: 'auto',
  firstDay: 1,
  selectable: true,
  editable: false,
  fixedWeekCount: false,
  dayCellContent: (arg) => {
    return arg.dayNumberText.replace('일', '')
  },
  events: [
    {
      title: '8,000',
      date: '2024-11-02',
      classNames: ['expense-event']
    },
    {
      title: '30,000',
      date: '2024-11-02',
      classNames: ['income-event']
    },
    {
      title: '500,000',
      date: '2024-11-08',
      classNames: ['expense-event']
    },
    {
      title: '1,212',
      date: '2024-11-14',
      classNames: ['expense-event']
    },
    {
      title: '111',
      date: '2024-11-13',
      classNames: ['income-event']
    }
  ],
  dateClick: function(info) {
    console.log('날짜 클릭:', info.dateStr)
  }
})
</script>

<style scoped>
.calendar-container {
  max-width: 820px;
  margin: 0;
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  margin-top: 24px;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.month-selector {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 18px;
  font-weight: 500;
}

.month-controls {
  display: flex;
  gap: 8px;
}

.control-btn {
  padding: 4px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
}

.calendar-legend {
  display: flex;
  gap: 16px;
  font-size: 14px;
}

.income {
  color: #FF8E99;
}

.expense {
  color: #1BBF83;
}

/* FullCalendar 커스텀 스타일 */
:deep(.fc) {
  font-family: inherit;
}

:deep(.fc-theme-standard td) {
  border: 1px solid #eee;
}

:deep(.fc-theme-standard th) {
  border: 1px solid #eee;
  padding: 8px 0;
  font-weight: 500;
  color: #666;
}

:deep(.fc-scrollgrid) {
  border: none !important;
}

:deep(.fc-daygrid-day-number) {
  font-size: 14px;
  padding: 8px;
  color: #333;
}

:deep(.fc-day-sat .fc-daygrid-day-number) {
  color: #D10000;
}

:deep(.fc-day-sun .fc-daygrid-day-number) {
  color: #D10000;
}

:deep(.fc-daygrid-day-frame) {
  padding: 8px;
  min-height: 100px;
}

:deep(.fc-daygrid-day-events) {
  margin-top: 4px;
}

:deep(.fc-event) {
  background: none;
  border: none;
}

:deep(.expense-event .fc-event-title) {
  color: #1BBF83;
  font-size: 13px;
  font-weight: 500;
}

:deep(.income-event .fc-event-title) {
  color: #FF8E99;
  font-size: 13px;
  font-weight: 500;
}

:deep(.fc-daygrid-event-dot) {
  display: none;
}

:deep(.fc-day-today) {
  background: #f8f9fa !important;
}

:deep(.fc-highlight) {
  background: rgba(76, 110, 245, 0.05);
}

:deep(.fc-daygrid-day.fc-day-today) {
  background-color: #f8f9fa !important;
}

</style>