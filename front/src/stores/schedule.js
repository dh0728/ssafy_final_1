import { defineStore } from 'pinia'
import axios from 'axios'

export const useScheduleStore = defineStore('schedule', () => {
    const API_URL = 'http://127.0.0.1:8000'

    const getSchedules = async () => {
        try {
            const response = await axios({
                method: 'GET',
                url: `${API_URL}/account/books/schedule/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                }
            })

            if (response.status === 200) {
                return response.data
            }
        } catch (error) {
            console.error('일정 조회 실패:', error)
            return null
        }
    }

    const addSchedule = async (scheduleData) => {
        try {
            const response = await axios({
                method: 'POST',
                url: `${API_URL}/account/books/schedule/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    name: scheduleData.name,
                    day: scheduleData.day,
                    value: scheduleData.value,
                    category_id: scheduleData.category_id,
                    is_income: scheduleData.is_income
                }
            })

            if (response.status === 201) {
                return response.data
            }
        } catch (error) {
            console.error('일정 추가 실패:', error)
            return null
        }
    }

    const updateSchedule = async (scheduleData) => {
        try {
            const response = await axios({
                method: 'PUT',
                url: `${API_URL}/account/books/schedule/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    name: scheduleData.name,
                    day: scheduleData.day,
                    value: scheduleData.value,
                    category_id: scheduleData.category_id,
                    is_income: scheduleData.is_income,
                    schedule_id: scheduleData.schedule_id
                }
            })

            if (response.status === 200) {
                return response.data
            }
        } catch (error) {
            console.error('일정 수정 실패:', error)
            return null
        }
    }


    const deleteSchedule = async (scheduleId) => {
        try {
            const response = await axios({
                method: 'DELETE',
                url: `${API_URL}/account/books/schedule/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    schedule_id: scheduleId
                }
            })

            if (response.status === 200) {
                return true
            }
        } catch (error) {
            console.error('일정 삭제 실패:', error)
            return false
        }
    }

    return {
        getSchedules,
        addSchedule,
        updateSchedule,
        deleteSchedule
    }
})