import { defineStore } from 'pinia'
import axios from 'axios'

export const useCalendarStore = defineStore('calendar', () => {
    const API_URL = 'http://127.0.0.1:8000'

    const addCalendar = async (calendarData) => {
        try {
            console.log(calendarData)
            const response = await axios({
                method: 'POST',
                url: `${API_URL}/account/books/write/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    year: calendarData.year,
                    month: calendarData.month,
                    day: calendarData.day,
                    is_income: calendarData.is_income,
                    payment: calendarData.payment,
                    store: calendarData.store,
                    category_id: calendarData.category_id,
                    account: calendarData.account,
                    memo: calendarData.memo
                }
            })

            if (response.status === 201) {
                return response.data
            }
        } catch (error) {
            console.error('가계부 작성 실패:', error)
            return null
        }
    }


    const updateCalendar = async (calendarData) => {
        try {
            const response = await axios({
                method: 'PUT',
                url: `${API_URL}/account/books/write/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    year: calendarData.year,
                    month: calendarData.month,
                    day: calendarData.day,
                    is_income: calendarData.is_income,
                    payment: calendarData.payment,
                    store: calendarData.store,
                    category_id: calendarData.category_id,
                    account: calendarData.account,
                    memo: calendarData.memo,
                    account_book_data_id: calendarData.account_book_data_id
                }
            })

            if (response.status === 200) {
                return response.data
            }
        } catch (error) {
            console.error('가계부 수정 실패:', error)
            return null
        }
    }

    const deleteCalendar = async (accountBookDataId) => {
        try {
            const response = await axios({
                method: 'DELETE',
                url: `${API_URL}/account/books/write/`,
                headers: {
                    'Authorization': `Token ${localStorage.getItem('auth')}`
                },
                data: {
                    account_book_data_id: accountBookDataId
                }
            })

            if (response.status === 200) {
                return true
            }
        } catch (error) {
            console.error('가계부 삭제 실패:', error)
            return false
        }
    }

    return {
        addCalendar,
        updateCalendar,
        deleteCalendar
    }
})