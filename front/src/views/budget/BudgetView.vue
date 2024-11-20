<template>
  <div class="budget-container">
    <!-- 왼쪽 사이드바 -->
    <SideBar />
    <CalendarView />
  </div>
  <!-- 메인 컨텐츠 영역 -->
  <div class="main-content">
    <RouterView />
  </div>
</template>

<script setup>
import SideBar from '@/components/common/SideBar.vue'
import CalendarView from "@/views/budget/CalendarView.vue";
</script>

<style scoped>
.budget-container {
  display: flex;
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.main-content {
  margin-left: 440px; /* sidebar width(240px) + left(150px) + gap(50px) */
  flex: 1;
  min-width: 0;
}
</style>