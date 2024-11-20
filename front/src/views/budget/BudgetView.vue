<template>
  <div class="budget-container">
    <!-- 왼쪽 사이드바 -->
    <SideBar />
    <MonthlyBudget />
    <!-- 메인 컨텐츠 영역 -->
  </div>
  <div class="main-content">
      <RouterView />
  </div>
</template>

<script setup>
import SideBar from '@/components/common/SideBar.vue'
import MonthlyBudget from "@/components/budget/MonthlyBudget.vue";
</script>

<style scoped>
.budget-container {
  display: flex;
  gap: 2rem;
  max-width: 1300px;
  margin-top:0px;
  margin-left: 400px;

  padding: 2rem;
}

.main-content {
  margin-left: 440px; /* sidebar width(240px) + left(150px) + gap(50px) */
  flex: 1;
  min-width: 0;
}


</style>