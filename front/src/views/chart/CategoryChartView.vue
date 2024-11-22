<template>
  <div class="analysis-container">
    <SideBar />

    <div class="content-wrapper">
      <div class="filter-header">
        <div class="left-section">
          <button class="filter-btn active">
            <span class="check-icon">✓</span>
            이지연 님의 소비 분석
          </button>
        </div>
      </div>

      <div class="category-analysis">
        <!-- 카테고리 도넛 차트 섹션 -->
        <div class="chart-section">
          <div class="donut-container">
            <h3>카테고리별 분석</h3>
            <div class="chart-wrapper">
              <!-- 도넛 차트가 들어갈 자리 -->
            </div>
          </div>

          <!-- 카테고리 목록 -->
          <div class="category-list">
            <!-- 카테고리 아이템들이 들어갈 자리 -->
          </div>
        </div>

        <!-- 상세 내역 테이블 섹션 -->
        <div class="details-section">
          <table class="details-table">
            <thead>
            <tr>
              <th>날짜</th>
              <th>카테고리</th>
              <th>결제수단</th>
              <th>거래처</th>
              <th>금액</th>
              <th>메모</th>
            </tr>
            </thead>
            <tbody>
            <!-- 상세 내역이 들어갈 자리 -->
            </tbody>
          </table>
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
  display: flex;
  min-height: 100vh;
  background: #f8f9fa;
}

.content-wrapper {
  flex: 1;
  padding: 32px;
  margin-left: 450px;
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

.category-analysis {
  display: flex;
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.chart-section {
  border: solid 1px black;
  display: flex;
  margin-bottom: 32px;
}

.donut-container {
  width: 300px;
}

.chart-wrapper {
  height: 300px;
  /* margin-top: 16px; */
}

h3 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
}

.category-list {
  flex: 1;
  padding: 20px 0;
}

.details-table {
  width: 100%;
  border-collapse: collapse;
}

.details-table th,
.details-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.details-table th {
  font-weight: 500;
  color: #666;
  background: #f8f9fa;
}

.details-section {
  border: 1px solid black;
  /* margin-top: 24px; */
  margin-left: 50px;
  width: 800px;
}
</style>