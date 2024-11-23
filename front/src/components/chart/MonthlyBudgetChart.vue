<template>
  <div class="charts-container">
    <!-- 3개월 지출 그래프 -->
    <div class="chart-wrapper">
      <h3>11월 분석</h3>
      <div class="subtitle">
        이번 달에는 지난 달 보다
        {{ formatDifference(chartData.total_expenditure - chartData.total_expenditure_age_1) }}원
        {{ chartData.total_expenditure > chartData.total_expenditure_age_1 ? '더' : '덜' }} 쓰이고
      </div>
        <Bar :data="monthlyData" :options="monthlyOptions" class="monthly-chart" />
    </div>

    <!-- 예산 대비 지출 그래프 -->
    <div class="chart-section">
      <Bar :data="budgetData" :options="budgetOptions" class="budget-chart" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js'
import { useDateChartStore } from "@/stores/dateChart.js"
import {useBudgetStore} from "@/stores/budget.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const dateChartStore = useDateChartStore()
const budgetStore = useBudgetStore();

const chartData = ref({
  total_expenditure: 0,
  total_expenditure_age_1: 0,
  total_expenditure_age_2: 0
})

const monthlyLabels = computed(() => {
  const currentMonth = new Date().getMonth() + 1
  return [
    `${currentMonth - 2}월 지출`,
    `${currentMonth - 1}월 지출`,
    `${currentMonth}월 지출`
  ]
})

const monthlyData = computed(() => ({
  labels: monthlyLabels.value,  // monthLabels -> monthlyLabels
  datasets: [{
    data: [
      chartData.value.total_expenditure_age_2,
      chartData.value.total_expenditure_age_1,
      chartData.value.total_expenditure
    ],
    backgroundColor: '#4C6EF5',
    borderRadius: 8,
    barThickness: 30,
    maxBarThickness: 30,
    barPercentage: 0.3,
    categoryPercentage: 0.3
  }]
}))



const budgetData = computed(() => ({
  labels: [`${new Date().getMonth() + 1}월 예산`, `${new Date().getMonth() + 1}월 지출`],
  datasets: [{
    data: [budgetStore.currentBudget || 0, chartData.value.total_expenditure],
    backgroundColor: ['#1BBF83', '#1BBF83'],
    borderRadius: 8,
    barThickness: 30,
    maxBarThickness: 30,
    barPercentage: 0.5,
    categoryPercentage: 0.5
  }]
}))


const monthlyOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${formatNumber(context.raw)}원`
      }
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        display: false  // y축 그리드 제거
      },
      ticks: {
        display: false
      }
    },
    x: {
      grid: {
        display: false  // x축 그리드 제거
      }
    }
  }
}

const budgetOptions = {
  responsive: true,
  maintainAspectRatio: false,
  indexAxis: 'x',  // 세로 막대로 변경
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${formatNumber(Math.abs(context.raw))}원`
      }
    }
  },
  scales: {
    x: {
      display: true,  // x축 숨기기
      grid: {
        display: false
      }
    },
    y: {
      display: false,  // y축 숨기기
      beginAtZero: true  // 0부터 시작하도록 설정
    }
  }
}

const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

const formatDifference = (value) => {
  return formatNumber(Math.abs(value))
}



onMounted(async () => {
  await budgetStore.getBudget()  // 예산 데이터 로드
  const data = await dateChartStore.getMonthlyChart()
  if (data) {
    chartData.value = data
  }
})
</script>

<style scoped>
.charts-container {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  height: 100%;
}

.chart-wrapper {
  flex: 2;
  height: 75%;
}

.chart-section {
  flex: 1;
  height: 75%;
  margin-top: 63px;
}

h3 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 4px;
}

.subtitle {
  font-size: 14px;
  color: #666;
  margin-bottom: 12px;
}

.monthly-chart, .budget-chart {
  height: 100% !important;
}
/* .monthly-chart{
  border-right: 1px solid black;
} */

.budget-chart {
  height: 80% !important;  /* 차트 높이 조정 */
  margin-top: 54px;  /* 추가 여백 */
  width: 80%;
}
</style>