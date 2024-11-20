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
    const card = ref(null)

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


    // 조건 검색
    const getCardsByCondition = async (type, categories, companies) => {
        try {
            currentType.value = type
            const cardType = type === 'credit' ? 1 : 2

            const params = new URLSearchParams()

            categories?.forEach(category => {
                params.append('categories', category)
            })
            companies?.forEach(company => {
                params.append('companies', company)
            })

            // 실제 요청 URL 확인
            const requestUrl = `${API_URL}/cards/${cardType}/search/condition?${params.toString()}`
            console.log('요청 URL:', requestUrl)

            const response = await axios({
                method: 'get',
                url: `${API_URL}/cards/${cardType}/search/condition`,
                params
            })

            cards.value = response.data
        } catch (error) {
            console.error('카드 검색 실패:', error)
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

    // 단일 카드 검색
    const getCardDetail = async (type, cardId) => {
        try {
            currentType.value = type
            const cardType = type === 'credit' ? 1 : 2
            console.log(cardType)

            const response = await axios({
                method: 'get',
                url: `${API_URL}/cards/${cardType}/detail/${cardId}`,
            })

             card.value = response.data
        } catch (error) {
            console.error('단일 카드 조회 실패:', error)
        }
    }

    const resetCards = () => {
        cards.value = []
        hasMoreCards.value = true
    }

    return {
        cards,
        card,
        hasMoreCards,
        currentType,
        getCardList,
        getMoreCards,
        getCardsByCondition,
        getCardDetail,
        resetCards
    }
}, { persist: true })