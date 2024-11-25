<template>
  <div class="weekly-container">
    <h3>주간별 분석</h3>
    <Bar :data="chartData" :options="chartOptions" class="bar-chart" />
    <div class="weekly-total">주간 평균 {{ formatNumber(weeklyAverage) }}원</div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js'
import { useDateChartStore } from '@/stores/dateChart'


const dateChartStore = useDateChartStore()
const weeklyData = ref(null)

const customLabelStyles = {
  id: 'customLabelStyles',
  afterDraw: (chart) => {
    const ctx = chart.ctx;
    const yAxis = chart.scales.y; // 수평 바 차트에서는 y축을 사용


    chart.data.labels.forEach((label, index) => {
      const meta = chart.getDatasetMeta(0);
      const bar = meta.data[index];
      
      if (bar) {
        const x = yAxis.left - 10; 
        const y = bar.y + bar.height / 2;  // 바닥 축 바로 아래에 위치
        const [mainLabel, detailLabel] = label.split('(');

        // 첫 번째 줄: 금액 (굵은 글씨, 검정색)
        ctx.font = 'bold 14px Apple SD Gothic Neo';
        ctx.fontWe
        ctx.fillStyle = '#333'; // 검정색
        ctx.textAlign = 'right';
        ctx.textBaseline = 'middle';
        ctx.fillText(mainLabel.trim(), x, y);

        if (detailLabel) {
          // 두 번째 줄: 상세 라벨 (예: "(11/01 - 11/07)")
          ctx.font = 'normal 12px Apple SD Gothic Neo';
          ctx.fillStyle = '#999'; // 회색
          ctx.fillText(`(${detailLabel.trim()}`, x, y + 18);
        }
      }
    });
  }
};
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend , customLabelStyles)

const chartData = computed(() => ({
  labels: getWeekLabels(),
  datasets: [{
    data: weeklyData.value?.weekly_data.map(week => week.expenditure) || [],
    backgroundColor: '#FFB946',
    borderRadius: 4,
    barThickness: 12,
  }]
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  indexAxis: 'y',
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      enabled: true,
      backgroundColor: 'rgba(0, 0, 0, 0.8)',
      titleColor: '#fff',
      bodyColor: '#fff',
      padding: 8,
      displayColors: false,
      callbacks: {
        label: (context) => `${context.formattedValue}원`
      }
    },
    customLabelStyles : false
  },
  scales: {
    x: {
      display: false,
      grid: {
        display: false
      }
    },
    y: {
      grid: {
        display: false
      },
      ticks: {
        font: {
          size: 12
        },
        color: '#666'
      }
    }
  }
}

const getWeekLabels = () => {
  const today = new Date()
  const year = today.getFullYear()
  const month = today.getMonth() + 1

  // 해당 월의 첫 날
  const firstDay = new Date(year, month - 1, 1)

  const weeks = []
  let currentDay = new Date(firstDay)

  while (currentDay.getMonth() === month - 1) {
    const weekStart = new Date(currentDay)
    const weekEnd = new Date(currentDay)
    weekEnd.setDate(weekEnd.getDate() + 6)

    // 월의 마지막 날 체크
    const lastDayOfMonth = new Date(year, month, 0)
    const endDay = weekEnd > lastDayOfMonth ? lastDayOfMonth : weekEnd

    weeks.push({
      start: weekStart,
      end: endDay
    })

    // 다음 주 시작일
    currentDay.setDate(currentDay.getDate() + 7)
  }

  // 라벨 생성
  return weeks.map((week, index) => {
    const startDate = `${String(week.start.getDate()).padStart(2, '0')}`
    const endDate = `${String(week.end.getDate()).padStart(2, '0')}`
    return `${month}월 ${index + 1}주 (${month}/${startDate} - ${month}/${endDate})`
  })
}

const weeklyAverage = computed(() => {
  if (!weeklyData.value?.weekly_data.length) return 0
  const total = weeklyData.value.weekly_data.reduce((sum, week) => sum + week.expenditure, 0)
  return Math.floor(total / weeklyData.value.weekly_data.length)
})

const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

onMounted(async () => {
  const data = await dateChartStore.getMonthlyChart()
  if (data) {
    weeklyData.value = data
  }
})
</script>

<style scoped>
.weekly-container {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 400px;
}

h3 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 0px;
}

.bar-chart {
  height: 200px;
  margin-bottom: 10px;
}

.weekly-total {
  text-align: right;
  font-size: 14px;
  color: #666;
}
</style>