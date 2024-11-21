<template>
  <div class="receipt-container">
    <SideBar />
    <div class="receipt-content">
      <div class="upload-container">
        <div class="upload-box"
             @drop.prevent="handleDrop"
             @dragover.prevent
             @click="triggerFileInput">
          <input
              type="file"
              ref="fileInput"
              class="file-input"
              accept="image/*"
              @change="handleFileSelect"
              hidden
          >
          <div class="upload-content">
            <div class="upload-icon">📸</div>
            <h3>영수증 이미지를 업로드해주세요</h3>
            <p>이미지를 드래그하여 놓거나 클릭하여 선택해주세요</p>
            <p class="file-types">지원 형식: image/png, image/jpeg, image/jpg</p>
          </div>
        </div>

        <!-- 미리보기 영역 -->
        <div v-if="previewUrl" class="preview-container">
          <div class="preview-header">
            <h3>업로드된 영수증</h3>
            <button class="close-btn" @click="clearPreview">×</button>
          </div>
          <img :src="previewUrl" alt="영수증 미리보기" class="preview-image">
          <button class="submit-btn" @click="uploadReceipt" :disabled="isLoading">
            {{ isLoading ? '처리중...' : '인식하기' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useReceiptStore } from '@/stores/receipt'
import SideBar from "@/components/common/SideBar.vue"
import axios from "axios";

const router = useRouter()
const receiptStore = useReceiptStore()
const fileInput = ref(null)
const previewUrl = ref(null)
const selectedImage = ref(null)
const isLoading = ref(false)

const triggerFileInput = () => {
  fileInput.value.click()
}

const handleFileSelect = (event) => {
  const file = event.target.files[0]
  if (file) {
    selectedImage.value = file
    createPreview(file)
  }
}

const handleDrop = (event) => {
  const file = event.dataTransfer.files[0]
  if (file) {
    selectedImage.value = file
    createPreview(file)
  }
}

const createPreview = (file) => {
  previewUrl.value = URL.createObjectURL(file)
}

const clearPreview = () => {
  previewUrl.value = null
  fileInput.value.value = ''
  selectedImage.value = null
}

const uploadReceipt = async () => {
  if (!selectedImage.value) return

  const formData = new FormData()
  formData.append('image', selectedImage.value)

  try {
    receiptStore.setReceiptImage(selectedImage.value)

    const response = await axios.post('http://127.0.0.1:8000/account/books/receipt/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': `Token ${localStorage.getItem('auth')}`
      }
    })

    if (response.status === 200) {
      receiptStore.setOcrResult(response.data.data)
      router.push({name : 'ResultReceipt'})
    }
  } catch (error) {
    console.error('Upload error:', error)
  }
}
</script>



<style scoped>
.receipt-container {
  padding: 32px;
  margin-left: 440px;
  max-width: 1300px;
  background: white;
}

.receipt-content {
  padding: 20px;
  background: white;
}

.upload-container {
  margin-top: 24px;
  display: flex;
  gap: 24px;
}

.upload-box {
  flex: 1;
  min-height: 400px;
  border: 2px dashed #E5E7EB;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
}

.upload-box:hover {
  border-color: #4C6EF5;
  background: #f8f9fa;
}

.upload-content {
  text-align: center;
  padding: 24px;
}

.upload-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.upload-content h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 8px;
}

.upload-content p {
  color: #6B7280;
  margin-bottom: 8px;
}

.file-types {
  font-size: 14px;
  color: #9CA3AF;
}

.preview-container {
  width: 400px;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
}

.preview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.preview-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1438;
}

.preview-image {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 16px;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}

.submit-btn:disabled {
  background: #9CA3AF;
  cursor: not-allowed;
}

.submit-btn.loading {
  position: relative;
  color: transparent;
}

.submit-btn.loading::after {
  content: "";
  position: absolute;
  width: 16px;
  height: 16px;
  top: 50%;
  left: 50%;
  margin: -8px 0 0 -8px;
  border: 2px solid #ffffff;
  border-radius: 50%;
  border-right-color: transparent;
  animation: rotate 1s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>