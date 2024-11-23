<script setup>
import { useAccountStore } from '@/stores/accounts'
import { storeToRefs } from 'pinia'
import CardRecommend from "@/components/cards/CardRecommend.vue";
import {ref} from "vue";

const showRecommendModal = ref(false)

const accountStore = useAccountStore()
const { isAuthenticated } = storeToRefs(accountStore)

const openRecommendModal = () => {
  showRecommendModal.value = true
}

const closeRecommendModal = () => {
  showRecommendModal.value = false
}
</script>

<template>
  <nav class="navbar">
    <RouterLink to="/" class="logo">가계북</RouterLink>
    <div class="nav-links">
      <RouterLink :to="{ name: 'CardList'}" class="nav-link">카드 찾기</RouterLink>
      <RouterLink :to="{ name: 'Budget' }" class="nav-link">내 가계부</RouterLink>
      <RouterLink :to="{ name: 'DateChart'}" class="nav-link">소비 분석</RouterLink>
      <button class="nav-link recommend-btn" @click="openRecommendModal">
        카드 추천 서비스
      </button>

      <!--   단순 페이지 이동은 link, 상태 변경이 일어나는 로그아웃은 button     -->
      <template v-if="isAuthenticated">
        <RouterLink to="/accounts/profile" class="nav-link">마이페이지</RouterLink>
        <button @click="accountStore.logout" class="login-btn">로그아웃</button>
      </template>
      <template v-else>
        <RouterLink to="/accounts/login" class="login-btn">로그인</RouterLink>
      </template>

    </div>
  </nav>
  <CardRecommend
      v-if="showRecommendModal"
      @close="closeRecommendModal"
  />
</template>

<style scoped>

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #ffffff;
  border-bottom: 1px solid #eaeaea;
}

.logo {
  font-weight: bold;
  font-size: 1.5rem;
  color: #1a1438;
  text-decoration: none;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-link {
  text-decoration: none;
  color: #333;
  font-size: 0.9rem;
}

.login-btn {
  background-color: #1a1438;
  color: white;
  padding: 0.5rem 1.5rem;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  font-size: 0.9rem;
  text-decoration: none;
}

.recommend-btn {
  background: none;
  border: none;
  padding: 0;
  font: inherit;
  cursor: pointer;
  text-decoration: none;
  color: #333;
  font-size: 0.9rem;
}

.recommend-btn:hover {
  color: #1a1438;
}
</style>