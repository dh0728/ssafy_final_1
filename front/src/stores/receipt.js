import { defineStore } from 'pinia'
import axios from 'axios'
import {ref} from "vue";

export const useReceiptStore = defineStore('receipt', () => {
    const API_URL = 'http://127.0.0.1:8000'

    // 영수증 이미지와 OCR 결과 저장
    const receiptImage = ref(null)
    const ocrResult = ref(null)

    // Add these methods to handle image and OCR result
    const setReceiptImage = (image) => {
        receiptImage.value = image
    }

    const setOcrResult = (result) => {
        ocrResult.value = result
    }

    // OCR 처리 함수
    const uploadImage = async (formData) => {
        try {
            const response = await axios({
                method: 'POST',
                url: `${API_URL}/account/books/receipt/`,
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: formData
            })

            if (response.status === 200) {
                ocrResult.value = response.data.data
                return response.data
            }
        } catch (error) {
            console.error('영수증 처리 실패:', error)
            return null
        }
    }

    return {
        receiptImage,
        ocrResult,
        uploadImage,
        setReceiptImage,
        setOcrResult
    }
})