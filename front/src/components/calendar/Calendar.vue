<template>
  <div class="calendar-container">
    <!-- 캘린더 헤더 -->
    <div class="calendar-header">
      <div class="month-selector">
        <span>{{ currentMonthLabel }}</span>
        <div class="calendar-legend">
          <span class="income">● 수입</span>
          <span class="expense">● 지출</span>
        </div>
      </div>
      <div class="month-controls">
        <button class="control-btn" @click="prevMonth">
          <i class="fas fa-chevron-left"><</i>
        </button>
        <button class="control-btn" @click="nextMonth">
          <i class="fas fa-chevron-right">></i>
        </button>
      </div>
    </div>

    <!-- 캘린더 본문 -->
    <FullCalendar
        ref="calendarRef"
        :options="calendarOptions"
        class="calendar"
    />

    <!-- 가계부 작성 모달 -->
    <CalendarAdd ref="addModalRef" :selected-date="selectedDate" @write-completed="onWriteCompleted" />
    <CalendarDayDetail :selected-date="selectedDate" :day-data="selectedDayData" :is-open="showDetailModal" @close="showDetailModal = false"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCalendarStore } from "@/stores/calendar.js"
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import CalendarAdd from './CalendarAdd.vue'
import CalendarDayDetail from "@/components/calendar/CalendarDayDetail.vue";

const showDetailModal = ref(false)
const selectedDayData = ref(null)

const calendarStore = useCalendarStore()
const calendarRef = ref(null)
const addModalRef = ref(null)
const currentDate = ref(new Date())
const selectedDate = ref(null)

// 현재 월 표시
const currentMonthLabel = computed(() => {
  return new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long'
  }).format(currentDate.value)
})

// 캘린더 데이터 가져오기
const fetchCalendarData = async () => {
  const year = currentDate.value.getFullYear()
  const month = currentDate.value.getMonth() + 1

  const result = await calendarStore.getCalendarData(year, month)
  if (result) {
    const events = []
    result.day_data.forEach(dayData => {
      const date = `${year}-${String(month).padStart(2, '0')}-${String(dayData.day).padStart(2, '0')}`

      if (dayData.income > 0) {
        events.push({
          title: new Intl.NumberFormat('ko-KR').format(dayData.income),
          date: date,
          classNames: ['income-event']
        })
      }
      if (dayData.expenditure > 0) {
        events.push({
          title: new Intl.NumberFormat('ko-KR').format(dayData.expenditure),
          date: date,
          classNames: ['expense-event']
        })
      }
    })
    calendarOptions.value.events = events
  }
}

// 월 이동 핸들러
const prevMonth = () => {
  const calendarApi = calendarRef.value.getApi()
  calendarApi.prev()
  currentDate.value = calendarApi.getDate()
  fetchCalendarData()
}

const nextMonth = () => {
  const calendarApi = calendarRef.value.getApi()
  calendarApi.next()
  currentDate.value = calendarApi.getDate()
  fetchCalendarData()
}

// 캘린더 옵션
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
  events: [],
  dayCellDidMount: (arg) => {
    // console.log('Day cell mount:', arg); 
    const editButton = document.createElement('button')
    editButton.className = 'edit-button'
    editButton.innerHTML = '✏️'

    editButton.onclick = (e) => {
      e.preventDefault()
      e.stopPropagation()  // 이벤트 전파 중지
      selectedDate.value = arg.date
      addModalRef.value?.openModal()
    }

    const cellContent = arg.el.querySelector('.fc-daygrid-day-top')
    cellContent.appendChild(editButton)
    // if (cellContent) {
    //   cellContent.appendChild(editButton);
    //     console.log('Edit button added to:', cellContent); // 추가 확인용 로그
    //   } else {
    //     console.warn('Cell content not found for:', arg.el); // 문제가 있는 경우 경고 출력
    //   }
  },

  // dateClick 이벤트 수정
  dateClick: async (info) => {
    // 연필 버튼이나 그 하위 요소를 클릭한 경우 무시
    if (info.jsEvent.target.closest('.edit-button')) {
      return
    }


    // 날짜 영역 클릭 시 CalendarDayDetail 모달 처리
    const date = info.date
    const year = date.getFullYear()
    const month = date.getMonth() + 1
    const day = date.getDate()

    const dayHistory = await calendarStore.getDayHistory(year, month, day)
    if (dayHistory && dayHistory.length > 0) {
      selectedDate.value = date
      selectedDayData.value = dayHistory
      showDetailModal.value = true
    }
  }
})

const onWriteCompleted = () => {
  fetchCalendarData()
}

onMounted(() => {
  fetchCalendarData()
})
</script>

<style scoped>
.calendar-container {
  max-width: 820px;
  margin: 0;
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.month-selector {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 20px;
  font-weight: 600;
  color: #1a1438;
}


.calendar-legend {
  display: flex;
  gap: 16px;
  font-size: 14px;
}

.month-controls {
  display: flex;
}

.income { color: #1BBF83; }
.expense { color: #FF8E99; }

/* FullCalendar 커스텀 스타일 */
:deep(.fc-theme-standard td) {
  border-left: none !important;
  border-right: none !important;
  border-bottom: 1px solid #eee;
}

:deep(.fc-theme-standard th) {
  border-left: none !important;
  border-right: none !important;
  border-bottom: 1px solid #eee;
  padding: 8px 0;
}

:deep(.fc-daygrid-day-top) {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 8px;
  flex-direction: row;
}

:deep(.fc-daygrid-day-number) {
  padding: 2px 4px;
  margin: 0;
  line-height: 1;
  font-size: 14px;
}

:deep(.edit-button) {
  position: absolute;
  z-index: 10; /* 버튼을 달력위로 올리기*/
  right: 10px;
  top: 16px;
  opacity: 0;
  background: none;
  border: none;
  padding: 4px;
  cursor: pointer;
  font-size: 12px;
  border-radius: 50%;
  transition: all 0.2s ease;
}

:deep(.fc-daygrid-day:hover .edit-button) {
  opacity: 1;
  background: rgba(76, 110, 245, 0.1);
}

:deep(.fc-event) {
  background: none !important;  /* 이벤트 배경색 완전 제거 */
  border: none;
}

:deep(.expense-event .fc-event-title) {
  color: #FF8E99;
  font-size: 13px;
  font-weight: 500;
  background: none !important;  /* 지출 이벤트 배경색 제거 */
}

:deep(.income-event .fc-event-title) {
  color: #1BBF83;
  font-size: 13px;
  font-weight: 500;
  background: none !important;  /* 수입 이벤트 배경색 제거 */
}

/* 호버 시에도 배경색이 나타나지 않도록 */
:deep(.fc-event:hover) {
  background: none !important;
}

.control-btn {
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 50%;
  background: #f8f9fa;
  color: #4C6EF5;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.control-btn:hover {
  background: #4C6EF5;
  color: white;
  transform: translateY(-1px);
}

/* FullCalendar 커스텀 스타일 */
:deep(.fc-theme-standard th) {
  border: none !important;
  padding: 12px 0;
  font-weight: 500;
  color: #868e96;
}

:deep(.fc-theme-standard td) {
  border: none !important;
}

:deep(.fc-scrollgrid) {
  border: none !important;
}

:deep(.fc-day-today) {
  background: #f8f9fa !important;
  border-radius: 8px;
}

:deep(.fc-col-header-cell) {
  padding: 8px 0 !important;
}

/* 날짜 셀 스타일 개선 */
:deep(.fc-daygrid-day) {
  padding: 4px;
}

:deep(.fc-daygrid-day-frame) {
  min-height: 80px;
}
</style>