<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

const router = useRouter()
const store = useAccountStore()

const email = ref('')
const password = ref('')
const newPassword = ref('')
const username = ref('')
const birth = ref('')

onMounted(async () => {
  try {
    await store.getUserInfo()
    email.value = store.user.email
    username.value = store.user.username
    birth.value = store.user.birth || ''
  } catch (error) {
    console.error('사용자 정보 가져오기 실패:', error)
    alert('사용자 정보를 불러오는데 실패했습니다.')
    router.push('/')
  }
})

const updateProfile = async () => {
  try {
    const payload = {
      current_password: password.value,
      username: username.value,
      birth: birth.value
    }

    if (newPassword.value) {
      payload.new_password = newPassword.value
    }

    await store.updateProfile(payload)
    alert('프로필이 성공적으로 업데이트되었습니다.')
    router.push('/')
  } catch (error) {
    if (error.response?.status === 400) {
      alert('입력하신 정보를 다시 확인해주세요.')
    } else if (error.response?.status === 401) {
      alert('현재 비밀번호가 일치하지 않습니다.')
    } else {
      alert('프로필 업데이트에 실패했습니다.')
    }
    console.error('Update failed:', error)
  }
}

const cancel = () => {
  const confirmed = confirm('변경사항이 저장되지 않습니다. 취소하시겠습니까?')
  if (confirmed) {
    router.push('/')
  }
}
</script>

<template>
  <div class="profile-container">
    <h1 class="welcome-text">회원정보 수정</h1>

    <div class="profile-form">
      <form @submit.prevent="updateProfile">
        <div class="input-group">
          <label for="email">이메일</label>
          <input
              id="email"
              type="email"
              v-model="email"
              placeholder="이메일을 입력해 주세요"
              class="input-field"
              disabled
          >
        </div>

        <div class="input-group">
          <label for="current-password">현재 비밀번호</label>
          <input
              id="current-password"
              type="password"
              v-model="password"
              placeholder="현재 비밀번호를 입력해 주세요"
              class="input-field"
              required
          >
        </div>

        <div class="input-group">
          <label for="new-password">새 비밀번호</label>
          <input
              id="new-password"
              type="password"
              v-model="newPassword"
              placeholder="새 비밀번호를 입력해 주세요"
              class="input-field"
              pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
              title="최소 8자 이상, 영문과 숫자를 포함해야 합니다"
          >
        </div>

        <div class="input-group">
          <label for="username">사용자 이름</label>
          <input
              id="username"
              type="text"
              v-model="username"
              placeholder="이름을 입력해 주세요"
              class="input-field"
              required
              minlength="2"
              maxlength="10"
          >
        </div>

        <div class="input-group">
          <label for="birth">생년월일</label>
          <input
              id="birth"
              type="date"
              v-model="birth"
              class="input-field"
              required
          >
        </div>

        <div class="button-group">
          <button type="submit" class="submit-btn">수정하기</button>
          <button type="button" class="cancel-btn" @click="cancel">취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
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

.input-group {
  text-align: left;
  margin-bottom: 1rem;
}

.input-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
  color: #666;
}

.input-field {
  width: 100%;
  height: 50px;
  border-radius: 8px;
  font-size: 1rem;
  box-sizing: border-box;
  padding: 0 16px;
  border: 1px solid #eaeaea;
  background-color: #f8f9fa;
}

.input-field:disabled {
  background-color: #f1f1f1;
  cursor: not-allowed;
}

.input-field:focus {
  outline: none;
  border-color: #1a1438;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.submit-btn,
.cancel-btn {
  flex: 1;
  height: 50px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  border: none;
}

.submit-btn {
  background-color: #1a1438;
  color: white;
}

.submit-btn:hover {
  background-color: #13102b;
}

.cancel-btn {
  background-color: #f8f9fa;
  border: 1px solid #eaeaea;
  color: #666;
}

.cancel-btn:hover {
  background-color: #eaeaea;
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