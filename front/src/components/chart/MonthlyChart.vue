<template>
  <div class="monthly-container" v-if="chartData">
    <div class="total-amount">
      <div class="amount-label">🔎{{ currentMonth }}월 총 지출</div>
      <div class="amount">{{ formatNumber(totalExpenditure) }}원</div>
      <div class="amount-desc">{{ getComparisonText() }}</div>
    </div>
    <Line :data="chartData" :options="chartOptions" class="line-chart" />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import { useDateChartStore } from '@/stores/dateChart'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const dateChartStore = useDateChartStore()
const monthlyData = ref(null)
const currentMonth = ref(new Date().getMonth() + 1)
const totalExpenditure = ref(0)

const chartData = computed(() => {
  if (!monthlyData.value) return null

  // 일별 데이터 배열 초기화 (1-31일)
  const dailyData = Array(31).fill(0)

  // day_data에서 실제 지출 데이터 매핑
  monthlyData.value.day_data.forEach(item => {
    dailyData[item.day - 1] = item.expenditure
  })

  return {
    labels: Array.from({ length: 31 }, (_, i) => i + 1),
    datasets: [{
      label: '일별 지출',
      data: dailyData,
      borderColor: '#FF8E99',
      backgroundColor: '#FF8E99',
      tension: 0.1,
      pointRadius: 0,
      borderWidth: 1.5
    }]
  }
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      enabled: true,
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      titleColor: '#fff',
      bodyColor: '#fff',
      padding: { top: 8, right: 12, bottom: 8, left: 12 },
      displayColors: false,
      cornerRadius: 4,
      caretSize: 6,
      callbacks: {
        title: function(context) {
          return `${context[0].label}일`;
        },
        label: function(context) {
          return `◽ ${context.formattedValue}원`;
        },
        labelTextColor: function() {
          return '#fff';
        }
      }
    }
  },
  scales: {
    x: {
      grid: {
        display: false
      },
      ticks: {
        display: false
      }
    },
    y: {
      grid: {
        display: false
      },
      ticks: {
        display: false
      }
    }
  },
  interaction: {
    intersect: false,
    mode: 'index'
  }
}

const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

const getComparisonText = () => {
  if (!monthlyData.value) return ''

  if (!monthlyData.value.total_expenditure_age_1) {
    return '지난 달 지출이 없어요!'
  }

  const diff = monthlyData.value.total_expenditure - monthlyData.value.total_expenditure_age_1
  return `지난 달보다 ${formatNumber(Math.abs(diff))}원 ${diff > 0 ? '더' : '덜'} 썼어요`
}

onMounted(async () => {
  const data = await dateChartStore.getMonthlyChart()
  if (data) {
    monthlyData.value = data
    totalExpenditure.value = data.total_expenditure
  }
})
</script>

<style scoped>
.monthly-container {
  max-height: 300px;
  width: 400px;
  background: white;
  border-radius: 12px;
  padding: 20px;
  height: 260px;
  position: relative;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

}

.total-amount {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 1;
  background: white;
  border-radius: 8px;
  width: calc(100% - 40px);
}

.amount-label {
  font-size: 14px;
  color: #666;
  margin-bottom: 4px;
  white-space: nowrap;
}

.amount {
  font-size: 24px;
  font-weight: 600;
  color: #333;
  margin-bottom: 4px;
}

.amount-desc {
  font-size: 12px;
  color: #888;
}

.line-chart {
  height: 160px !important;
  margin-top: 100px; /* 상단 여백 */
  margin-bottom: 10px; /* 하단 여백 추가 */
  transform: translateY(-20px);
}
</style>