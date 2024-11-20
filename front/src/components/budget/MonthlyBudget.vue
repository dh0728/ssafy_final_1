<template>
  <div class="budget-view">
    <!-- 상단 헤더 -->
    <div class="header">
      <div class="user-select">
        <span class="user-icon">👤 </span>
        <span>이지연 님의 가계부</span>
      </div>
      <div class="actions">
        <button class="write-btn">가계부 작성하기</button>
      </div>
    </div>

    <!-- 예산 요약 카드 -->
    <div class="budget-card">
      <div class="budget-info">
        <div class="info-item">
          <div class="item-content">
            <span class="label">이번 달 지출</span>
            <div class="amount">509,212원</div>
            <a href="#" class="link">
              지출 분석하러 가기
              <span class="arrow">→</span>
            </a>
          </div>
        </div>
        <div class="divider"></div>
        <div class="info-item">
          <div class="item-content">
            <span class="label">이번 달 수입</span>
            <div class="amount">30,111원</div>
            <a href="#" class="link">
              수입 분석하러 가기
              <span class="arrow">→</span>
            </a>
          </div>
        </div>
        <div class="divider"></div>
        <div class="info-item">
          <div class="item-content">
            <span class="label">예산</span>
            <div class="amount">1,000,000원</div>
            <a href="#" class="link">
              예산 설정하러 가기
              <span class="arrow">→</span>
            </a>
          </div>
        </div>
      </div>
    </div>
    <Calendar />
  </div>
</template>

<style scoped>
.budget-view {
  padding: 0px 32px;
  width: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.left-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-name {
  font-size: 16px;
  font-weight: 500;
  color: #1a1438;
}

.left-section input[type="checkbox"] {
  width: 18px;
  height: 18px;
  border-radius: 4px;
  border: 2px solid #ddd;
  cursor: pointer;
}

.right-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.icon-btn {
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  color: #666;
  transition: all 0.2s;
}

.icon-btn:hover {
  background: #f8f9fa;
}

.write-btn {
  padding: 8px 16px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 6px;
}

.write-btn:hover {
  background: #4263eb;
  transform: translateY(-1px);
}

.budget-card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  width: 100%;
  transition: all 0.3s;
}

.budget-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.budget-info {
  display: flex;
  min-height: 160px;
}

.info-item {
  flex: 1;
  padding: 10px;
  position: relative;
}

.item-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.label {
  color: #666;
  font-size: 15px;
  margin-bottom: 12px;
}

.amount {
  font-size: 28px;
  font-weight: 600;
  color: #1a1438;
  margin: 8px 0 16px;
}

.link {
  color: #4C6EF5;
  text-decoration: none;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
  margin-top: auto;
}

.link:hover {
  color: #4263eb;
}

.arrow {
  font-size: 16px;
  transition: transform 0.2s;
}

.link:hover .arrow {
  transform: translateX(4px);
}

.divider {
  width: 1px;
  background: #f1f3f5;
  margin: 24px 0;
}

@media (max-width: 768px) {
  .budget-info {
    flex-direction: column;
  }

  .divider {
    width: 100%;
    height: 1px;
    margin: 0;
  }

  .info-item {
    padding: 20px;
  }
}
</style>
<script setup lang="ts">
import Calendar from "@/components/budget/Calendar.vue";
</script>