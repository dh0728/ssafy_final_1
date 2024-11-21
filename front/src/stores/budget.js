import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useBudgetStore = defineStore('budget', () => {
    const API_URL = 'http://127.0.0.1:8000'
    const currentBudget = ref(null)
    const budgetId = ref(null) // budget_id 저장용

    const getBudget = async () => {
        console.log(localStorage.getItem('auth'))
        try {
            const date = new Date()
            const response = await axios({
                method: 'GET',
                url: `${API_URL}/account/books/budget/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },

                params: {
                    year: date.getFullYear(),
                    month: date.getMonth() + 1
                }
            })

            if (response.status === 200) {
                currentBudget.value = response.data.value
                budgetId.value = response.data.budget_id
                return response.data
            }
        } catch (error) {
            console.error('예산 조회 실패:', error.response?.data)
            console.error('에러 상태:', error.response?.status)
            return null
        }
    }


    // 예산 설정
    const setBudget = async (amount) => {
        try {
            const date = new Date()
            const response = await axios({
                method: 'PUT',
                url: `${API_URL}/account/books/budget/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    year: date.getFullYear(),
                    month: date.getMonth() + 1,
                    budget_id: budgetId.value,
                    value: amount
                }
            })

            if (response.status === 200) {
                currentBudget.value = amount
                return true
            }
        } catch (error) {
            console.error('예산 설정 실패:', error)
            return false
        }
    }

    // const setBudget = async (amount) => {
    //     try {
    //         const date = new Date()
    //         const response = await axios({
    //             method: 'POST',
    //             url: `${API_URL}/account/books/budget/`,
    //             headers: {
    //                 'Authorization': `Token ${localStorage.getItem('auth')}`
    //             },
    //             data: {
    //                 year: date.getFullYear(),
    //                 month: date.getMonth() + 1,
    //                 value: amount
    //             }
    //         })
    //
    //         if (response.status === 200 || response.status === 201) {
    //             currentBudget.value = amount
    //             return true
    //         }
    //     } catch (error) {
    //         console.error('예산 설정 실패:', error)
    //         return false
    //     }
    // }

    return {
        currentBudget,
        budgetId,
        getBudget,
        setBudget
    }
}, { persist: true })