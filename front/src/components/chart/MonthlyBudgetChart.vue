<template>
  <div class="charts-container">
    <!-- 3개월 지출 그래프 -->
    <div class="chart-wrapper">
      <h3>11월 분석</h3>
      <div class="subtitle">이번 달에는 지난 달 보다 385,879원 더 많이 쓰이고</div>
      <Bar :data="monthlyData" :options="monthlyOptions" class="monthly-chart" />
    </div>

    <!-- 예산 대비 지출 그래프 -->
    <div class="chart-section">
      <Bar :data="budgetData" :options="budgetOptions" class="budget-chart" />
    </div>
  </div>
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js'
import {useDateChartStore} from "@/stores/dateChart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const dateChartStore = useDateChartStore();

const monthlyData = {
  labels: ['9월 지출', '10월 지출', '11월 지출'],
  datasets: [{
    data: [0, 123333, 509212],
    backgroundColor: '#4C6EF5',
    borderRadius: 8,
    barThickness: 40
  }]
}

const budgetData = {
  labels: ['11월 예산', '11월 지출'],
  datasets: [{
    data: [0, -509212],
    backgroundColor: ['#1BBF83', '#1BBF83'],
    borderRadius: 8,
    barThickness: 40
  }]
}

const monthlyOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${context.formattedValue}원`
      }
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        callback: value => `${value}원`
      }
    }
  }
}

const budgetOptions = {
  responsive: true,
  maintainAspectRatio: false,
  indexAxis: 'y',
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${Math.abs(context.raw)}원`
      }
    }
  },
  scales: {
    x: {
      beginAtZero: true,
      ticks: {
        callback: value => `${Math.abs(value)}원`
      }
    }
  }
}
</script>

<style scoped>
.charts-container {
  display: flex;
  gap: 24px;
  align-items: center;
}

.chart-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.chart-section {
  flex: 1;
  margin-bottom: 16px;
  position: relative;
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
  height: 120px !important; /* 높이 조정 */
}

.budget-chart {
  height: 80px !important; /* 높이 조정 */
}

/* 차트 옵션 조정 */
:deep(.chartjs-render-monitor) {
  max-height: 100%;
}
</style>