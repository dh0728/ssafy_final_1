<template>
  <div class="history-container">
    <SideBar />

    <div class="history2-container">
      <!-- 상단 필터 영역 -->
      <div class="filter-header">
        <div class="left-section">
          <button class="filter-btn active">
            <span class="check-icon">✓</span>
            이지연 님의 가계부
          </button>
          <button class="more-btn">⋯</button>
        </div>
        <div class="right-section">
          <button class="write-btn">가계부 작성하기 📝</button>
        </div>
      </div>

      <!-- 메인 필터 -->
      <div class="main-filters">
        <div class="filter-tabs">
          <button class="tab-btn active">내역 전체보기 ▾</button>
          <button class="tab-btn">카테고리 전체보기 ▾</button>
        </div>
      </div>

      <!-- 테이블 헤더 -->
      <div class="table-container">
        <table class="history-table">
          <thead>
          <tr>
            <th class="checkbox-col">
              <input type="checkbox">
            </th>
            <th>분류</th>
            <th>날짜</th>
            <th>카테고리</th>
            <th>결제수단</th>
            <th>가게지</th>
            <th>금액</th>
            <th>메모</th>
            <th>작성자</th>
            <th>액션</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="item in historyItems" :key="item.id">
            <td><input type="checkbox"></td>
            <td>
              <span :class="['type-badge', item.type]">
                {{ item.type === 'income' ? '수입' : '지출' }}
              </span>
            </td>
            <td>{{ item.date }}</td>
            <td>{{ item.category }}</td>
            <td>{{ item.payment }}</td>
            <td>{{ item.store }}</td>
            <td :class="['amount', item.type]">
              {{ formatNumber(item.amount) }}원
            </td>
            <td>{{ item.memo }}</td>
            <td>{{ item.writer }}</td>
            <td class="action-buttons">
              <button class="action-btn">수정하기</button>
              <button class="action-btn">삭제하기</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>

      <!-- 페이지네이션 -->
      <div class="pagination">
        <button class="page-btn">←</button>
        <button class="page-btn active">1</button>
        <button class="page-btn">→</button>
      </div>
    </div>
    </div>
</template>

<script setup>
import SideBar from "@/components/common/SideBar.vue";

</script>

<style scoped>
.history-container {
  padding: 32px;
  margin-left: 440px;
  max-width: 1300px;
  background: white;
}

.history2-container {
  padding: 20px;
  background: white;
}

.filter-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.left-section {
  display: flex;
  gap: 8px;
  align-items: center;
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

.write-btn {
  padding: 8px 16px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
}

.main-filters {
  margin-bottom: 20px;
}

.filter-tabs {
  display: flex;
  gap: 12px;
}

.tab-btn {
  padding: 8px 16px;
  border: none;
  background: none;
  cursor: pointer;
}

.tab-btn.active {
  font-weight: 600;
  border-bottom: 2px solid #4C6EF5;
}

.history-table {
  width: 100%;
  border-collapse: collapse;
}

.history-table th,
.history-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.type-badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.type-badge.income {
  background: #e8f5e9;
  color: #1BBF83;
}

.type-badge.expense {
  background: #ffebee;
  color: #ff6b6b;
}

.amount.income {
  color: #1BBF83;
}

.amount.expense {
  color: #ff6b6b;
}

.action-buttons {
  display: flex;
  gap: 8px;
}

.action-btn {
  padding: 4px 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  color: #666;
  font-size: 12px;
}

.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 20px;
}

.page-btn {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
}

.page-btn.active {
  background: #4C6EF5;
  color: white;
  border-color: #4C6EF5;
}
</style>