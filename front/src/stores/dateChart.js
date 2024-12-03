import { defineStore } from 'pinia'
import axios from 'axios'

export const useDateChartStore = defineStore('dateChart', () => {
    const API_URL = 'http://127.0.0.1:8000'

    const getMonthlyChart = async () => {
        try {
            const date = new Date()

            const response = await axios({
                method: 'GET',
                url: `${API_URL}/account/books/analyze/time/`,

                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },

                params: {
                    year: date.getFullYear(),
                    month: date.getMonth() + 1
                }
            })

            if (response.status === 200) {
                return response.data
            }
            console.log(response.data)
        } catch (error) {
            console.error('월 총지출 분석:', error.response?.data)
            return null
        }

    }

    return {
        getMonthlyChart,

    }
})