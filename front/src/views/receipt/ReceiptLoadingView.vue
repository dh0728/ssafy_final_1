<template>
  <div class="loading-container">
    <SideBar />
    <div class="loading-content">
      <div class="loading-box">
        <div class="loading-spinner"></div>
        <h2>영수증을 인식하고 있습니다</h2>
        <p>잠시만 기다려주세요...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import SideBar from "@/components/common/SideBar.vue"
</script>

<style scoped>
.loading-container {
  padding: 32px;
  margin-left: 440px;
  max-width: 1300px;
  background: white;
}

.loading-content {
  padding: 20px;
  background: white;
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-box {
  text-align: center;
}

.loading-spinner {
  width: 60px;
  height: 60px;
  margin: 0 auto 24px;
  border: 4px solid #E5E7EB;
  border-radius: 50%;
  border-top-color: #4C6EF5;
  animation: spin 1s linear infinite;
}

.loading-box h2 {
  font-size: 24px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 12px;
}

.loading-box p {
  color: #6B7280;
  font-size: 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>