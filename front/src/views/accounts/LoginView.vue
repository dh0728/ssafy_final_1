<script setup>
import { ref } from 'vue'
import {useAccountStore} from "@/stores/accounts.js";

const email = ref(null)
const password = ref(null)

const store = useAccountStore();

const login = () => {
  console.log('Login ', email.value, password.value)
  const payload = {
    email: email.value,
    password: password.value,
  }
  store.login(payload)
}
</script>

<template>
  <div class="login-container">
    <h1 class="welcome-text">당신과 함께하는 Pay Flow</h1>

    <button class="google-btn">
      <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
           alt="Google"
           class="google-icon" />
      구글로 로그인하기
    </button>

    <div class="divider">OR</div>

    <form @submit.prevent="login">
      <input
          type="email"
          v-model="email"
          placeholder="이메일 주소"
          class="input-field"
          required
      >
      <input
          type="password"
          v-model="password"
          placeholder="비밀번호"
          class="input-field"
          required
          minlength="8"
      >
      <button type="submit" class="submit-btn">로그인</button>
    </form>
    <div class="signup-link">
      아직 계정이 없으신가요? <RouterLink to="/accounts/registration" class="link">회원가입</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.google-icon {
  width: 18px;
  height: 18px;
}

.login-container {
  max-width: 400px;
  margin: 4rem auto;
  padding: 2rem;
  text-align: center;
}

.welcome-text {
  font-size: 2rem;
  font-weight: bold;
  color: #1a1438;
  margin-bottom: 2rem;
}

.google-btn,
.input-field,
.submit-btn {
  width: 100%;
  height: 50px;
  border-radius: 8px;
  font-size: 1rem;
  box-sizing: border-box;
  padding: 0 16px;
  margin-bottom: 1rem;
}

.google-btn {
  border: 1px solid #eaeaea;
  background-color: white;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  cursor: pointer;
}

.divider {
  margin: 1.5rem 0;
  color: #666;
  position: relative;
  font-size: 0.9rem;
}

.divider::before,
.divider::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 45%;
  height: 1px;
  background-color: #eaeaea;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
}

.input-field {
  border: 1px solid #eaeaea;
  background-color: #f8f9fa;
}

.input-field:focus {
  outline: none;
  border-color: #1a1438;
}

.submit-btn {
  background-color: #1a1438;
  color: white;
  border: none;
  cursor: pointer;
  font-weight: 500;
}

.submit-btn:hover {
  background-color: #13102b;
}

.signup-link {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #666;
}

.link {
  color: #1a1438;
  text-decoration: none;
  font-weight: 500;
  margin-left: 0.5rem;
}

.link:hover {
  text-decoration: underline;
}
</style>