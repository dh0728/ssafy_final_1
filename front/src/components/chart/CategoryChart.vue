<template>
  <div class="category-chart">
    <h3>2024년 11월</h3>
    <h4>카테고리별 분석</h4>
    <div class="chart-container">
      <div class="chart-wrapper">
        <Doughnut
            v-if="isReady"
            :data="chartData"
            :options="chartOptions"
        />
      </div>
      <div class="category-items">
        <div v-for="(item, index) in filteredCategories"
             :key="index"
             class="category-item">
          <div class="category-info">
            <span class="color-dot" :style="{ backgroundColor: chartColors[index] }"></span>
            <span class="category-name">{{ getCategoryName(item.category_id) }}</span>
          </div>
          <div class="amount"
               @click="selectCategory(item)"
               style="cursor: pointer">
            {{ formatNumber(item.total_amount) }}원 >
          </div>
        </div>
      </div>
      <div class="divider"></div>
      <div class="total">총 {{ formatNumber(totalAmount) }}원</div>
    </div>
  </div>
</template>

<script setup>
import {ref, computed, onMounted} from 'vue'
import {Doughnut} from 'vue-chartjs'
import {Chart as ChartJS, ArcElement, Tooltip} from 'chart.js'
import {useCategoryChartStore} from '@/stores/categoryChart'

ChartJS.register(ArcElement, Tooltip)

const isReady = ref(false)
const categoryData = ref([])

const emit = defineEmits(['select-category'])

const selectCategory = (category) => {
  emit('select-category', category)
}

const chartColors = [
  '#4C6EF5', // 파란색
  '#FFB946', // 주황색
  '#1BBF83', // 초록색
  '#FF8E99', // 분홍색
  '#845EF7', // 보라색
  '#339AF0', // 하늘색
  '#FF6B6B', // 빨간색
  '#94D82D', // 연두색
  '#F06595', // 진한 분홍색
  '#FCC419', // 노란색
  '#51CF66', // 밝은 초록색
  '#22B8CF', // 청록색
  '#FF922B', // 진한 주황색
  '#20C997', // 민트색
  '#5C7CFA', // 연한 파란색
  '#BE4BDB', // 자주색
  '#FF9787', // 연한 빨간색
  '#69DB7C', // 연두색
  '#A9E34B', // 라임색
  '#748FFC', // 연한 남색
  '#9775FA', // 연한 보라색
  '#63E6BE', // 연한 민트색
  '#FFA94D', // 연한 주황색
  '#4DABF7', // 하늘색
  '#CED4DA', // 회색
  '#868E96', // 진한 회색
  '#495057'  // 더 진한 회색
]

const categories = ref([
  { id: 1, name: '🏬 모든가맹점' },
  { id: 2, name: '🚍 교통' },
  { id: 3, name: '⛽ 주유' },
  { id: 4, name: '📱 통신' },
  { id: 5, name: '🛒 마트/편의점' },
  { id: 6, name: '🎁 쇼핑' },
  { id: 7, name: '🍛 푸드' },
  { id: 8, name: '☕ 카페/디저트' },
  { id: 9, name: '💄 뷰티/피트니스' },
  { id: 10, name: '💰 무실적' },
  { id: 11, name: '📃 공과금/렌탈' },
  { id: 12, name: '🏥 병원/약국' },
  { id: 13, name: '🐱 애완동물' },
  { id: 14, name: '✏ 교육/육아' },
  { id: 15, name: '🚗 자동차/하이패스' },
  { id: 16, name: '⚽ 레저/스포츠' },
  { id: 17, name: '🎬 영화/문화' },
  { id: 18, name: '🤳 간편결제' },
  { id: 19, name: '✈ 항공마일리지' },
  { id: 20, name: '💺 공항라운지/PP' },
  { id: 21, name: '💎 프리미엄' },
  { id: 22, name: '🧳 여행/숙박' },
  { id: 23, name: '🌏 해외' },
  { id: 24, name: '💼 비지니스' },
  { id: 25, name: '🎸 기타' },
  { id: 26, name: '💸 금융' },
  { id: 27, name: '🏃‍♂️ 생활' },
])

const filteredCategories = computed(() => {
  return categoryData.value.filter(item => item.total_amount > 0)
})

const totalAmount = computed(() => {
  return filteredCategories.value.reduce((sum, item) => sum + item.total_amount, 0)
})

const chartData = computed(() => ({
  labels: filteredCategories.value.map(item => getCategoryName(item.category_id)),
  datasets: [{
    data: filteredCategories.value.map(item => item.total_amount),
    backgroundColor: chartColors,
    borderWidth: 0,
    borderRadius: 4
  }]
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  cutout: '75%',
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      enabled: true,
      callbacks: {
        label: (context) => `${formatNumber(context.raw)}원`
      }
    }
  }
}

const getCategoryName = (id) => {
  const category = categories.value.find(cat => cat.id === id)
  return category ? category.name : '기타'
}
const formatNumber = (value) => new Intl.NumberFormat('ko-KR').format(value)

onMounted(async () => {
  const store = useCategoryChartStore()
  const data = await store.getCategoryChart()
  if (data) {
    categoryData.value = data
    isReady.value = true
  }
})
</script>

<style scoped>
.category-chart {
  padding: 20px;
  text-align: center;
}

.chart-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.chart-wrapper {
  width: 300px;
  height: 300px;
}

.category-items {
  width: 100%;
  max-width: 300px;
  margin-top: 25px;
  max-height: 180px; /* 스크롤을 활성화할 높이 제한 */
  overflow-y: auto; /* 수직 스크롤 활성화 */
  padding-right: 10px; /* 스크롤바와 텍스트 간의 간격을 위해 패딩 추가 */
}

.category-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
}


/* 스크롤바 숨기기 */
.category-items::-webkit-scrollbar {
  display: none; /* 웹킷 기반 브라우저에서 스크롤바 숨기기 */
}

.category-items {
  -ms-overflow-style: none;  /* IE 및 Edge에서 스크롤바 숨기기 */
  scrollbar-width: none; /* Firefox에서 스크롤바 숨기기 */
}

.category-info {
  display: flex;
  align-items: center;
  gap: 8px;
}


.color-dot {
  width: 12px;
  height: 12px;
  border-radius: 2px;
  flex-shrink: 0;
}

.category-name {
  font-size: 14px;
}

.amount {
  font-size: 14px;
  font-weight: 500;
}

.divider {
  padding-left: 10px;
  height: 1px;
  width: 300px;
  background-color: #eee;
  margin: 12px 0;
}

.total {
  padding-left: 10px;
  width: 300px;
  text-align: right;
  font-weight: 500;
}
</style>