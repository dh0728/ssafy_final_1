<template>
  <div class="budget-view">
    <!-- 상단 헤더 -->
    <div class="header">
      <div class="left-section">
        <input type="checkbox" checked>
        <span>이지연 님의 가계부</span>
      </div>
      <div class="right-section">
        <button class="icon-btn">⋯</button>
        <button class="icon-btn">+</button>
        <button class="write-btn">가계부 작성하기</button>
      </div>
    </div>

    <!-- 예산 요약 카드 -->
    <div class="budget-card">
      <div class="budget-info">
        <div class="info-item">
          <span class="label">이번 달 지출</span>
          <div class="amount">509,212원</div>
          <a href="#" class="link">지출 분석하러 가기 ></a>
        </div>
        <div class="divider"></div>
        <div class="info-item">
          <span class="label">이번 달 수입</span>
          <div class="amount">30,111원</div>
          <a href="#" class="link">수입 분석하러 가기 ></a>
        </div>
        <div class="divider"></div>
        <div class="info-item">
          <span class="label">예산</span>
          <div class="amount">1,000,000원</div>
          <a href="#" class="link">예산 설정하러 가기 ></a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.budget-view {
  padding: 20px 32px;
  width: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 8px;
}

.left-section input[type="checkbox"] {
  width: 16px;
  height: 16px;
}

.right-section {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon-btn {
  padding: 8px;
  background: none;
  border: none;
  cursor: pointer;
  color: #666;
}

.write-btn {
  padding: 8px 16px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
}

.budget-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
}

.budget-info {
  display: flex;
  height: 140px;
}

.info-item {
  flex: 1;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.label {
  color: #666;
  font-size: 14px;
}

.amount {
  font-size: 24px;
  font-weight: 600;
  color: #1a1438;
  margin: 12px 0;
}

.link {
  color: #4C6EF5;
  text-decoration: none;
  font-size: 14px;
}

.divider {
  width: 1px;
  background: #eee;
  margin: 24px 0;
}

@media (max-width: 768px) {
  .budget-info {
    flex-direction: column;
    height: auto;
  }

  .divider {
    width: 100%;
    height: 1px;
    margin: 0;
  }

  .info-item {
    padding: 16px;
  }
}
</style>