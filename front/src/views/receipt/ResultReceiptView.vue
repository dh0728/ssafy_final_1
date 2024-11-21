<template>
  <div class="ocr-result-container">
    <SideBar />
    <div class="result-content">
      <!-- 왼쪽: 업로드된 이미지 표시 -->
      <div class="uploaded-image-section">
        <div class="image-container">
          <h3>업로드된 영수증</h3>
          <img :src="previewUrl" alt="업로드된 영수증" class="receipt-image">
        </div>
      </div>

      <!-- 오른쪽: OCR 결과 폼 -->
      <div class="ocr-form-section">
        <h3>인식된 데이터</h3>
        <div class="form-content">
          <div class="form-group">
            <label>날짜</label>
            <div class="date-group">
              <input
                  type="text"
                  v-model="ocrData.year"
                  class="date-input"
                  :readonly="!isEditing"
                  :class="{ 'editable': isEditing }"
              >
              <span class="date-separator">년</span>
              <input
                  type="text"
                  v-model="ocrData.month"
                  class="date-input"
                  :readonly="!isEditing"
                  :class="{ 'editable': isEditing }"
              >
              <span class="date-separator">월</span>
              <input
                  type="text"
                  v-model="ocrData.day"
                  class="date-input"
                  :readonly="!isEditing"
                  :class="{ 'editable': isEditing }"
              >
              <span class="date-separator">일</span>
            </div>
          </div>

          <div class="form-group">
            <label>금액</label>
            <input
                type="text"
                v-model="ocrData.account"
                class="input-field"
                :readonly="!isEditing"
                :class="{ 'editable': isEditing }"
                @input="onlyNumbers"
            >
          </div>

          <div class="form-group">
            <label>분류</label>
            <select
                v-if="isEditing"
                v-model="ocrData.is_income"
                class="input-field"
            >
              <option :value="false">지출</option>
              <option :value="true">수입</option>
            </select>
            <input
                v-else
                type="text"
                :value="ocrData.is_income ? '수입' : '지출'"
                class="input-field"
                readonly
            >
          </div>

          <div class="form-group">
            <label>결제수단</label>
            <select
                v-if="isEditing"
                v-model="ocrData.payment"
                class="input-field"
            >
              <option value="현금">현금</option>
              <option value="카드">카드</option>
              <option value="이체">이체</option>
            </select>
            <input
                v-else
                type="text"
                v-model="ocrData.payment"
                class="input-field"
                readonly
            >
          </div>

          <div class="form-group">
            <label>거래처</label>
            <input
                type="text"
                v-model="ocrData.store"
                class="input-field"
                :readonly="!isEditing"
                :class="{ 'editable': isEditing }"
            >
          </div>

          <div class="form-group">
            <label>카테고리</label>
            <select
                v-if="isEditing"
                v-model="ocrData.category_id"
                class="input-field"
            >
              <option v-for="category in categories"
                      :key="category.id"
                      :value="category.id"
              >
                {{ category.name }}
              </option>
            </select>
            <input
                v-else
                type="text"
                :value="getCategoryName(ocrData.category_id)"
                class="input-field"
                readonly
            >
          </div>

          <div class="form-group">
            <label>메모</label>
            <input
                type="text"
                v-model="ocrData.memo"
                class="input-field"
                :readonly="!isEditing"
                :class="{ 'editable': isEditing }"
            >
          </div>

          <div class="form-actions">
            <button
                class="modify-btn"
                @click="modifyData"
            >
              {{ isEditing ? '수정 완료' : '수정하기' }}
            </button>
            <button
                class="save-btn"
                @click="saveData"
                :disabled="isEditing"
            >저장하기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useReceiptStore } from '@/stores/receipt'
import { useCalendarStore } from '@/stores/calendar'
import SideBar from "@/components/common/SideBar.vue";

const router = useRouter()
const receiptStore = useReceiptStore()
const calendarStore = useCalendarStore()

const previewUrl = ref(null)
const ocrData = ref({
  year: '',
  month: '',
  day: '',
  account: '',
  is_income: false,
  payment: '',
  store: '',
  category_id: '',
  memo: ''
})

// 카테고리 목록
const categories = ref([
  { id: 1, name: '🏬 모든가맹점' },
  { id: 2, name: '🚍 교통' },
  { id: 3, name: '⛽ 주유' },
  { id: 4, name: '📱 통신' },
  { id: 5, name: '🛒 마트/편의점' },
  { id: 6, name: '🎁 쇼핑' },
  { id: 7, name: '🍛 푸드' },
  { id: 8, name: '☕ 카페/디저트' },
  { id: 9, name: '💄 뷰티/피트니스' },
  { id: 10, name: '💰 무실적' },
  { id: 11, name: '📃 공과금/렌탈' },
  { id: 12, name: '🏥 병원/약국' },
  { id: 13, name: '🐱 애완동물' },
  { id: 14, name: '✏ 교육/육아' },
  { id: 15, name: '🚗 자동차/하이패스' },
  { id: 16, name: '⚽ 레저/스포츠' },
  { id: 17, name: '🎬 영화/문화' },
  { id: 18, name: '🤳 간편결제' },
  { id: 19, name: '✈ 항공마일리지' },
  { id: 20, name: '💺 공항라운지/PP' },
  { id: 21, name: '💎 프리미엄' },
  { id: 22, name: '🧳 여행/숙박' },
  { id: 23, name: '🌏 해외' },
  { id: 24, name: '💼 비지니스' },
  { id: 25, name: '🎸 기타' },
  { id: 26, name: '💸 금융' },
  { id: 27, name: '🏃‍♂️ 생활' }
])

onMounted(() => {
  // receipt store에서 이미지와 OCR 결과 가져오기
  if (receiptStore.receiptImage) {
    previewUrl.value = URL.createObjectURL(receiptStore.receiptImage)
  }

  if (receiptStore.ocrResult) {
    const result = receiptStore.ocrResult
    ocrData.value = {
      year: result.year,
      month: result.month,
      day: result.day,
      account: result.account,
      is_income: result.is_income,
      payment: result.payment,
      store: result.store,
      category_id: result.category_id,
      memo: result.memo
    }
  } else {
    // OCR 결과가 없으면 이전 페이지로 이동
    router.push('/receipt')
  }
})

const saveData = async () => {
  try {
    // 데이터 형식 변환
    const formData = {
      year: ocrData.value.year,
      month: ocrData.value.month,
      day: ocrData.value.day,
      is_income: ocrData.value.is_income,
      payment: ocrData.value.payment,
      store: ocrData.value.store,
      category_id: ocrData.value.category_id,
      account: Number(ocrData.value.account.replace(/,/g, '')), // 콤마 제거 후 숫자로 변환
      memo: ocrData.value.memo
    }

    const result = await calendarStore.addCalendar(formData)
    if (result) {
      // 저장 성공 시 내역 페이지로 이동
      router.push('/history')
    }
  } catch (error) {
    console.error('저장 실패:', error)
  }
}

// formatNumber 함수 추가
const formatNumber = (value) => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

// getCategoryName 함수 추가
const getCategoryName = (categoryId) => {
  const category = categories.value.find(cat => cat.id === categoryId)
  return category ? category.name : ''
}

// 수정 모드 상태 추가
const isEditing = ref(false)

// 수정하기 버튼 클릭 핸들러
const modifyData = () => {
  isEditing.value = !isEditing.value
}
</script>

<style scoped>
.ocr-result-container {
  padding: 32px;
  margin-left: 440px;
  max-width: 1300px;
  background: white;
}

.result-content {
  display: flex;
  gap: 32px;
}

.uploaded-image-section,
.ocr-form-section {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.receipt-image {
  width: 100%;
  max-height: 600px;
  object-fit: contain;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-size: 14px;
  font-weight: 500;
  color: #4B5563;
}

.input-field {
  width: 100%;
  height: 48px;
  padding: 8px 16px;
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  font-size: 15px;
  color: #1F2937;
  background: #f8f9fa;
}

.date-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.date-input {
  width: 80px;
  height: 48px;
  padding: 8px;
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  text-align: center;
  background: #f8f9fa;
}

.form-actions {
  display: flex;
  gap: 12px;
  margin-top: 32px;
}

.modify-btn,
.save-btn {
  flex: 1;
  height: 48px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
}

.modify-btn {
  background: white;
  border: 1px solid #E5E7EB;
  color: #4B5563;
}

.save-btn {
  background: #4C6EF5;
  border: none;
  color: white;
}

h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 24px;
}

.input-field.editable {
  background: white;
  border-color: #4C6EF5;
  cursor: text;
}

.input-field.editable:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(76, 110, 245, 0.1);
}

.date-input.editable {
  background: white;
  border-color: #4C6EF5;
  cursor: text;
}

select.input-field {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 8L2 4h8z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 32px;
}

.save-btn:disabled {
  background: #9CA3AF;
  cursor: not-allowed;
}
</style>