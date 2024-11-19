import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCardStore = defineStore('cards', () => {
    const router = useRouter()
    const API_URL = 'http://127.0.0.1:8000'
    // 불러올 카드 데이터가 존재하는지 확인
    const hasMoreCards = ref(true)
    const currentType = ref('credit')


    const cards = ref([])

    const getCardList = async (cardType) => {
        try {
            currentType.value = cardType
            const type = cardType === 'credit' ? 1 : 2
            const response = await axios({
                method: 'get',
                url: `${API_URL}/cards/${type}/search/1`,
            })
             cards.value = response.data
        } catch (error) {
            console.error(error)
        }
    }

    // 추가 카드 로드
    const getMoreCards = async (lastId) => {
        if (!hasMoreCards.value) return

        try {
            const type = currentType.value === 'credit' ? 1 : 2
            const response = await axios({
                method: 'get',
                url: `${API_URL}/cards/${type}/search/${lastId}`
            })

            if (!response.data || response.data.length < 20) {
                hasMoreCards.value = false
            }

            if (response.data && response.data.length > 0) {
                cards.value = [...cards.value, ...response.data]
            }
        } catch (error) {
            console.error('추가 카드 로딩 실패:', error)
            hasMoreCards.value = false
        }
    }

    const resetCards = () => {
        cards.value = []
        hasMoreCards.value = true
    }

    return {
        cards,
        hasMoreCards,
        getCardList,
        getMoreCards,
        resetCards
    }
}, { persist: true })