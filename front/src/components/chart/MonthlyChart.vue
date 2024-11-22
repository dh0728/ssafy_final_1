<template>
  <div class="analysis-container">
    <!-- 총 지출 차트 -->
    <div class="chart-section">
      <div class="total-amount">
        <div class="amount-label">11월 총 지출</div>
        <div class="amount">{{ formatNumber(chartData.total_expenditure) }}원</div>
        <div class="amount-desc">
          {{ getPreviousMonthComparison() }}
        </div>
      </div>
      <Line :data="dailyChartData" :options="dailyChartOptions" class="line-chart" />
    </div>

    <!-- 월별 비교 차트 -->
    <div class="chart-section">
      <h3>11월 분석</h3>
      <Bar :data="monthlyCompareData" :options="monthlyCompareOptions" class="bar-chart" />
    </div>

    <!-- 주간별 분석 -->
    <div class="chart-section">
      <h3>주간별 분석</h3>
      <div class="weekly-bars">
        <div v-for="week in chartData.weekly_data" :key="week.week" class="week-row">
          <div class="week-label">11월 {{ week.week }}주</div>
          <div class="week-amount">{{ formatNumber(week.expenditure) }}원</div>
          <div
              class="week-bar"
              :style="{ width: `${getWeekPercentage(week.expenditure)}%` }"
          ></div>
        </div>
      </div>
    </div>

    <!-- 고정 지출 분석 -->
    <div class="chart-section">
      <h3>11월 고정지출</h3>
      <div class="fixed-expense">
        <div class="fixed-total">총 {{ formatNumber(chartData.total_schedules) }}원</div>
        <div class="fixed-count">총 {{ schedulesCount }}건</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { Line, Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend } from 'chart.js'
import { useDateChartStore } from '@/stores/dateChart'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend)

const dateChartStore = useDateChartStore()
const chartData = ref({})

const schedulesCount = computed(() => {
  return chartData.value?.schedules?.length || 0
})

// 일별 차트 데이터
const dailyChartData = computed(() => ({
  labels: Array.from({ length: 31 }, (_, i) => i + 1),
  datasets: [{
    label: '일별 지출',
    data: Array.from({ length: 31 }, (_, i) => {
      const dayData = chartData.value.day_data?.find(d => d.day === i + 1)
      return dayData ? dayData.expenditure : 0
    }),
    borderColor: '#FF8E99',
    backgroundColor: '#FF8E99',
    tension: 0.1,
    pointRadius: 0,
    borderWidth: 1.5
  }]
}))

// 월별 비교 차트 데이터
const monthlyCompareData = computed(() => ({
  labels: ['9월 지출', '10월 지출', '11월 지출', '11월 예산', '11월 지출'],
  datasets: [{
    data: [
      chartData.value.total_expenditure_age_2,
      chartData.value.total_expenditure_age_1,
      chartData.value.total_expenditure,
      0,
      -chartData.value.total_expenditure
    ],
    backgroundColor: ['#6E7BF2', '#6E7BF2', '#6E7BF2', '#1BBF83', '#1BBF83']
  }]
}))

// 차트 옵션
const dailyChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      callbacks: {
        label: (context) => `${context.parsed.y.toLocaleString()}원`
      }
    }
  },
  scales: {
    x: { grid: { display: false }, ticks: { display: false } },
    y: { grid: { display: false }, ticks: { display: false } }
  }
}

const monthlyCompareOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: { legend: { display: false } },
  scales: {
    y: { beginAtZero: true }
  }
}

// 유틸리티 함수
const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

const getPreviousMonthComparison = () => {
  if (!chartData.value.total_expenditure_age_1) {
    return '동월런 지난 달 지출이 없어요!'
  }
  const diff = chartData.value.total_expenditure - chartData.value.total_expenditure_age_1
  return `지난 달보다 ${formatNumber(Math.abs(diff))}원 ${diff > 0 ? '더' : '덜'} 썼어요`
}

const getWeekPercentage = (expenditure) => {
  const maxExpenditure = Math.max(...chartData.value.weekly_data.map(w => w.expenditure))
  return (expenditure / maxExpenditure) * 100
}

// 데이터 로드
onMounted(async () => {
  const result = await dateChartStore.getMonthlyChart()
  if (result) {
    chartData.value = result
  }
})
</script>

<style scoped>
.analysis-container {
  display: grid;
  gap: 24px;
  padding: 24px;
}

.chart-section {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.line-chart {
  height: 200px;
}

.bar-chart {
  height: 300px;
}

.weekly-bars {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.week-row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.week-bar {
  height: 8px;
  background: #4C6EF5;
  border-radius: 4px;
  transition: width 0.3s ease;
}

.fixed-expense {
  display: flex;
  gap: 24px;
  align-items: center;
}

.fixed-total {
  font-size: 24px;
  font-weight: 600;
}

.fixed-count {
  color: #666;
}
</style>