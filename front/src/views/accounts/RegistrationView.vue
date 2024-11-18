<script setup>
import {ref} from "vue";
import {useAccountStore} from "@/stores/accounts.js";

const email = ref(null)
const password = ref(null)
const username = ref(null)
const birth = ref(null)

const store = useAccountStore()

const registration = () => {
  console.log('registration', email.value, password.value, username.value, birth.value)
  const payload = {
    email: email.value,
    password: password.value,
    username: username.value,
    birth: birth.value,
  }
  store.register(payload)
}
</script>

<template>
  <div class="signup-container">
    <h1 class="welcome-text">회원 가입</h1>

    <button class="google-btn">
      <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg"
           alt="Google"
           class="google-icon"/>
      구글로 로그인하기
    </button>

    <div class="divider">OR</div>

    <div class="signup-form">
      <form @submit.prevent="registration">
        <input
            type="email"
            v-model="email"
            placeholder="이메일을 입력해 주세요"
            class="input-field"
            required
        >
        <input
            type="password"
            v-model="password"
            placeholder="비밀번호를 입력해 주세요"
            class="input-field"
            required
            minlength="8"
            pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
            title="최소 8자 이상, 영문과 숫자를 포함해야 합니다"
        >
        <input
            type="text"
            v-model="username"
            placeholder="닉네임을 입력해 주세요"
            class="input-field"
            required
            minlength="2"
            maxlength="10"
        >
        <input
            type="date"
            v-model="birth"
            placeholder="생년월일을 선택해 주세요"
            class="input-field"
            required
        >
        <button type="submit" class="submit-btn">가입하기</button>
      </form>
    </div>

    <p class="login-link">
      이미 계정이 있으신가요?
      <RouterLink to="/accounts/login" class="link">로그인</RouterLink>
    </p>
  </div>
</template>

<style scoped>
.signup-container {
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

.google-icon {
  width: 18px;
  height: 18px;
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

.login-link {
  margin-top: 1.5rem;
  color: #666;
  font-size: 0.9rem;
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

input[type="date"] {
  color: #666;
}

input[type="date"]::-webkit-calendar-picker-indicator {
  cursor: pointer;
  filter: invert(0.5);
}

.input-field::placeholder {
  color: #999;
}
</style>