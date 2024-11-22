<template>
  <div class="analysis-container">
    <SideBar />

    <div class="filter-header">
      <div class="left-section">
        <button class="filter-btn active">
          <span class="check-icon">✓</span>
          이지연 님의 가계부 분석
        </button>
      </div>
    </div>

    <div class="analysis-content">
      <!-- 1. 월별 총액 요약 컨테이너 -->
      <div class="summary-container">
        <div class="month-label">11월 분석</div>
        <div class="total-amount">이번 달에는 지난 달 보다 509,212원 더 쓰이고</div>
      </div>

      <!-- 2. 주간별 분석 그래프 컨테이너 -->
      <div class="weekly-chart-container">
        <div class="chart-header">
          <h3>주간별 분석</h3>
          <div class="chart-legend">
            <span class="income">● 수입</span>
            <span class="expense">● 지출</span>
          </div>
        </div>
        <div class="chart-content">
          <!-- 차트가 들어갈 자리 -->
        </div>
      </div>

      <!-- 3. 주간별 상세 내역 컨테이너 -->
      <div class="weekly-details-container">
        <div class="week-details">
          <div class="week-row">
            <div class="week-label">11월 1주 (11/01 - 11/07)</div>
            <div class="week-amount">8,000원</div>
            <div class="week-bar"></div>
          </div>
          <!-- 다른 주차 내역들 -->
        </div>
      </div>

      <!-- 4. 고정 지출 분석 컨테이너 -->
      <div class="fixed-expense-container">
        <h3>11월 고정지출</h3>
        <div class="fixed-expense-content">
          <div class="fixed-expense-total">총 127,303원</div>
          <div class="fixed-expense-count">총 2건</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import SideBar from "@/components/common/SideBar.vue";
</script>

<style scoped>
.analysis-container {
  padding: 32px;
  margin-left: 440px;
  max-width: 1300px;
  background: white;
}

.analysis-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.filter-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.filter-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 20px;
  background: white;
}

.filter-btn.active {
  background: #f0f0f0;
}

/* 1. 월별 총액 요약 컨테이너 */
.summary-container {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* 2. 주간별 분석 그래프 컨테이너 */
.weekly-chart-container {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* 3. 주간별 상세 내역 컨테이너 */
.weekly-details-container {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* 4. 고정 지출 분석 컨테이너 */
.fixed-expense-container {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* 공통 스타일 */
h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 16px;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.chart-legend {
  display: flex;
  gap: 16px;
  font-size: 14px;
}

.income { color: #1BBF83; }
.expense { color: #FF8E99; }
</style>
