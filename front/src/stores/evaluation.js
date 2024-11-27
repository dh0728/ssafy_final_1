import { defineStore } from 'pinia'
import axios from 'axios'
import {ref} from "vue";

export const useEvaluationStore = defineStore('evaluation', () => {
    const API_URL = 'http://127.0.0.1:8000'
    const evaluation = ref(null)
    const isLoading = ref(false)

    const getEvaluation = async () => {
        try {
            isLoading.value = true
            const response = await axios({
                method: 'get',
                url: `${API_URL}/account/books/evaluation/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                }
            })
            evaluation.value = response.data.comment
        } catch (error) {
            console.error('평가 가져오기 실패:', error)
        } finally {
            isLoading.value = false
        }
    }

    return {
        evaluation,
        isLoading,
        getEvaluation
    }
})