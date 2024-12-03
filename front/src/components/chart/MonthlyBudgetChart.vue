<template>
  <div class="charts-container">
    <!-- 3개월 지출 그래프 -->
    <div class="chart-wrapper">
      <h3>11월 분석</h3>
      <div class="subtitle">
        이번 달에는 지난 달 보다
        {{ formatDifference(chartData.total_expenditure - chartData.total_expenditure_age_1) }}원
        {{ chartData.total_expenditure > chartData.total_expenditure_age_1 ? '더' : '덜' }} 사용했어요 !
      </div>
      <div style="width: 100% ;height:100%;display: flex;box-sizing: border-box; ">
        <div style="flex: 2; padding: 10px; border-right: 1px solid #ddd ;">
          <Bar :data="monthlyData" :options="monthlyOptions" class="monthly-chart" />
        </div >
        <div style="flex: 1; padding: 10px;">
          <Bar :data="budgetData" :options="budgetOptions" class="budget-chart" />
        </div>
      </div>  
      
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend , Chart, registerables} from 'chart.js'
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
    [`${formatNumber(chartData.value.total_expenditure_age_2)}원`,`${currentMonth - 2}월 지출`],
    [`${formatNumber(chartData.value.total_expenditure_age_1)}원`,`${currentMonth - 1}월 지출`],
    [`${formatNumber(chartData.value.total_expenditure)}원`,`${currentMonth}월 지출`]
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
  labels: [
    [`${formatNumber(budgetStore.currentBudget)}원`,`${new Date().getMonth() + 1}월 예산`], 
    [`${formatNumber(chartData.value.total_expenditure_age_2)}원`,`${new Date().getMonth() + 1}월 지출`],
  ],
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


const customLabelStyles = {
  id: 'customLabelStyles',
  afterDraw: (chart) => {
    const ctx = chart.ctx;
    const xAxis = chart.scales.x;

    chart.data.labels.forEach((labelArray, index) => {
      const meta = chart.getDatasetMeta(0);
      const bar = meta.data[index];
      
      if (bar) {
        const x = bar.x;
        const y = xAxis.bottom + 10; // 바닥 축 바로 아래에 위치

        // 첫 번째 줄: 금액 (굵은 글씨, 검정색)
        ctx.font = 'bold 14px Apple SD Gothic Neo';
        ctx.fontWe
        ctx.fillStyle = '#333'; // 검정색
        ctx.textAlign = 'center';
        ctx.fillText(labelArray[0], x, y);

        // 두 번째 줄: 월 지출 (얇은 글씨, 회색)
        ctx.font = '10px Apple SD Gothic Neo';
        ctx.fillStyle = '#999'; // 회색
        ctx.fillText(labelArray[1], x, y + 20);
      }
    });
  }
};

Chart.register(...registerables,customLabelStyles)

const monthlyOptions = {
  responsive: true,
  maintainAspectRatio: false,
  layout: {
    padding: {
      bottom: 40 // 아래쪽에 40px 정도의 여백 추가
    }
  },
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${formatNumber(context.raw)}원`
      }
    },
    customLabelStyles // 플러그인 추가
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
      },
      ticks:{
        display :false
      }
    }
  },
}

const budgetOptions = {
  responsive: true,
  maintainAspectRatio: false,
  layout: {
    padding: {
      bottom: 40 // 아래쪽에 40px 정도의 여백 추가
    }
  },
  indexAxis: 'x',  // 세로 막대로 변경
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${formatNumber(Math.abs(context.raw))}원`
      }
    },
    customLabelStyles,
  },
  
  scales: {
    x: {
      display: true,  // x축 숨기기
      grid: {
        display: false
      },
      ticks:{
        display :false
      }
    },
    y: {
      display: false,  // y축 숨기기
      beginAtZero: true  // 0부터 시작하도록 설정
    },
    
  },
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
  width: 100%;
}

.chart-section {
  border-left: 1px solid #ddd;
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

.monthly-chart {
  width: 80%;
  height: 80%;
}

.budget-chart {
  width: 50%;
}

</style>