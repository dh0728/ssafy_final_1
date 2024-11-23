<template>
  <div class="">
    <!-- 왼쪽 사이드바 -->
    <div class="sidebar">
      <div class="menu-section">
        <div class="menu-title">내 가계부</div>
        <ul class="menu-list">
          <li>
            <RouterLink :to="{ name: 'Budget' }" class="menu-item" active-class="active">
              <span class="icon">📅</span>
              캘린더
            </RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'CalendarHistory' }" class="menu-item" active-class="active">
              <span class="icon">📝</span>
              내역
            </RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'Receipt' }" class="menu-item" active-class="active">
              <span class="icon">📸</span>
              영수증 인식하기
            </RouterLink>
          </li>
        </ul>
      </div>

      <div class="menu-section">
        <div class="menu-title">분석</div>
        <ul class="menu-list">
          <li>
            <RouterLink :to="{ name: 'DateChart' }" class="menu-item" active-class="active">
              <span class="icon">📊</span>
              주간 월별 분석
            </RouterLink>
          </li>
          <li>
            <RouterLink :to="{ name: 'CategoryChart' }" class="menu-item" active-class="active">
              <span class="icon">🔍</span>
              카테고리별 분석
            </RouterLink>
          </li>
          <li>
            <RouterLink to="/budget/yearly" class="menu-item" active-class="active">
              <span class="icon">📈</span>
              연간 통계
            </RouterLink>
          </li>
        </ul>
      </div>

      <div class="menu-section">
        <div class="menu-title">설정</div>
        <ul class="menu-list">
          <li>
            <button class="menu-item" @click="openMyCardModal">
              <span class="icon">💳</span>
              내 카드 목록
            </button>
          </li>
          <li>
            <button class="menu-item" @click="openRecommendModal">
              <span class="icon">💸</span>
              카드 추천 서비스
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <MyCardRegister
      v-if="showMyCardModal"
      @close="closeMyCardModal"
  />
  <CardRecommend
      v-if="showRecommendModal"
      @close="closeRecommendModal"
  />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MyCardRegister from "@/components/cards/MyCardRegister.vue";
import {ref} from "vue";
import CardRecommend from "@/components/cards/CardRecommend.vue";

const showMyCardModal = ref(false)
const showRecommendModal = ref(false)

const openMyCardModal = () => {
  showMyCardModal.value = true
}

const closeMyCardModal = () => {
  showMyCardModal.value = false
}

const openRecommendModal = () => {
  showRecommendModal.value = true
}

const closeRecommendModal = () => {
  showRecommendModal.value = false
}
</script>


<style scoped>
.budget-container {
  display: flex;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.card-detail-container {
  display: flex;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.sidebar {
  width: 240px;
  flex-shrink: 0;
  position: fixed; /* sticky에서 fixed로 변경 */
  left: 150px; /* 왼쪽에서 150px 위치에 고정 */
  top: 100px; /* 네비게이션 바 고려한 상단 여백 */
  height: calc(100vh - 120px); /* 화면 높이에서 상하단 여백 제외 */
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  overflow-y: auto; /* 내용이 많을 경우 스크롤 */
}

.menu-section {
  margin-bottom: 2rem;
}

.menu-section:last-child {
  margin-bottom: 0;
}

.menu-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #f5f5f5;
}

.menu-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  color: #666;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.menu-item:hover {
  background: #f8f9fa;
  color: #1a1438;
}

.menu-item.active {
  background: #1a1438;
  color: white;
}

.icon {
  font-size: 1.2rem;
  width: 24px;
  text-align: center;
}

.main-content {
  margin-left: 440px; /* sidebar width(240px) + left(150px) + gap(50px) */
  flex: 1;
  min-width: 0;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .card-detail-container {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    position: static;
    margin-bottom: 1rem;
  }
}

button.menu-item {
  width: 100%;
  border: none;
  background: none;
  text-align: left;
  font-size: inherit;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  color: #666;
  border-radius: 8px;
  transition: all 0.2s ease;
}

button.menu-item:hover {
  background: #f8f9fa;
  color: #1a1438;
}
</style>