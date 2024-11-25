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
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, registerables } from 'chart.js'
import { useDateChartStore } from '@/stores/dateChart'

const dateChartStore = useDateChartStore()
const monthlyData = ref(null)
const currentMonth = ref(new Date().getMonth() + 1)
const totalExpenditure = ref(0)


const customLabelStyles = {
  id: 'customLabelStyles',
  afterDraw: (chart) => {
    if (!chart || !chart.ctx) {
      return; // 차트가 유효하지 않다면 실행하지 않음
    }
    const ctx = chart.ctx;
    const xAxis = chart.scales.x;

    if (!xAxis) {
      return; // x축이 정의되지 않았다면 실행하지 않음
    }

    chart.data.labels.forEach((labelArray, index) => {
      const meta = chart.getDatasetMeta(0);
      const bar = meta.data[index];
      
      if (!bar) {
        return; // 데이터가 존재하지 않는다면 실행하지 않음
      }
      const x = bar.x;
      const y = xAxis.bottom + 10; // 바닥 축 바로 아래에 위치
      // 첫 번째 줄: 금액 (굵은 글씨, 검정색)
      ctx.font = 'bold 14px Apple SD Gothic Neo';
      ctx.fontWe
      ctx.fillStyle = '#333'; // 검정색
      ctx.textAlign = 'center';
      ctx.fillText(labelArray[0], x, y);
      // 두 번째 줄: 월 지출 (얇은 글씨, 회색)
      ctx.font = 'Apple SD Gothic Neo';
      ctx.fillStyle = '#999'; // 회색
      ctx.fillText(labelArray[1], x, y + 20);
      
    });
  }
};
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, customLabelStyles)

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
      // backgroundColor: '#FF8E99',
      backgroundColor: 'rgba(255, 142, 153, 0.5)', // 선 아래 영역의 배경색 (부드러운 핑크)
      pointBackgroundColor: '#FFFFFF', // 데이터 포인트 배경색
      pointBorderColor: '#FF8E99', // 데이터 포인트 테두리 색상
      pointRadius: 2, // 데이터 포인트 반지름
      pointBorderWidth: 1, // 데이터 포인트 테두리 두께
      pointHoverRadius: 7, // 마우스 오버 시 데이터 포인트 확대 크
      tension: 0.1,
      pointRadius: 2,
      borderWidth: 6
    }]
  }
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  layout: {
    padding: {
      right: 20  // 하단에 20px의 패딩 추가
    }
  },
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
    },
    customLabelStyles : false,
  },
  scales: {
    x: {
      grid: {
        display: false
      },
      ticks: {
        maxRotion:0, // 기울이기 싫어
        minRotation:0,
        autoSkip: false, 
        maxTicksLimit:2, //최대 레이블 수 
        callback: function(value, index, values) {
          // 첫 번째 레이블 "1일", 마지막 레이블 "말일"
          if (index === 0) {
            return '1일';
          } else if (index === values.length - 1) {
            return '말일';
          } else {
            return '';  // 중간 레이블은 표시하지 않음
          }
        }
      }
    },
    y: {
      suggestedMin :-1000,
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