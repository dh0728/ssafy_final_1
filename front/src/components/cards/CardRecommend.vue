<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h2>스마트한 카드 추천</h2>
        <button class="close-btn" @click="$emit('close')">×</button>
      </div>

      <div class="modal-body">
        <!-- 신용카드 섹션 -->
        <div v-if="store.recommendCards?.credit_cards?.length > 0" class="recommendation-section">
          <h3>추천 신용카드</h3>
          <div class="card-list">
            <div v-for="card in store.recommendCards.credit_cards"
                 :key="card.credit_card_id"
                 class="card-item">
              <div class="card-image">
                <img :src="card.img_path" :alt="card.credit_card_name">
              </div>
              <div class="card-info">
                <h4>{{ card.credit_card_name }}</h4>
                <span class="card-brand">{{ card.brand }}</span>
                <div class="benefit-tag">추천 신용카드</div>
                <div class="button-group">
                  <RouterLink
                      :to="{ name: 'CardDetail', params: { type: 'credit', cardId: card.credit_card_id }}"
                      class="detail-btn">
                    자세히 보기
                  </RouterLink>
                  <button @click="registerCard(1, card.credit_card_id)" class="register-btn">
                    내 카드 등록
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 체크카드 섹션 -->
        <div v-if="store.recommendCards?.check_cards?.length > 0" class="recommendation-section">
          <h3>추천 체크카드</h3>
          <div class="card-list">
            <div v-for="card in store.recommendCards.check_cards"
                 :key="card.check_card_id"
                 class="card-item">
              <div class="card-image">
                <img :src="card.img_path" :alt="card.check_card_name">
              </div>
              <div class="card-info">
                <h4>{{ card.check_card_name }}</h4>
                <span class="card-brand">{{ card.brand }}</span>
                <div class="benefit-tag">추천 체크카드</div>
                <div class="button-group">
                  <RouterLink
                      :to="{ name: 'CardDetail', params: { type: 'check', cardId: card.check_card_id }}"
                      class="detail-btn">
                    자세히 보기
                  </RouterLink>
                  <button @click="registerCard(2, card.check_card_id)" class="register-btn">
                    내 카드 등록
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 추천 카드가 없는 경우 -->
        <div v-if="!store.recommendCards?.credit_cards?.length && !store.recommendCards?.check_cards?.length"
             class="no-cards">
          <p>추천 카드를 불러오는 중입니다...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import {useCardStore} from "@/stores/cards.js"

const store = useCardStore()

const registerCard = async (cardType, cardId) => {
  try {
    const result = await store.registerMyCard(cardType, cardId)
    if (result.success) {
      alert(result.message)
      // 성공 후 내 카드 목록 새로고침
      await store.getMyCards()
    } else {
      alert(result.message)
    }
  } catch (error) {
    alert('카드 등록 중 오류가 발생했습니다.')
    console.error('카드 등록 실패:', error)
  }
}

onMounted(async () => {
  await store.getRecommendCards()
})
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 32px;
  border-radius: 12px;
  width: 900px;
  min-height: 600px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #eee;
}

.modal-header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #1a1438;
}

.close-btn {
  background: none;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #666;
}

.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 24px;
  padding: 20px;
}

.card-item {
  background: #f8f9fa;
  border-radius: 16px;
  padding: 20px;
  transition: all 0.2s ease;
}

.card-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.card-image {
  width: 100%;
  height: 160px;
  margin-bottom: 16px;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: 8px;
}

.card-info h4 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 8px;
}

.card-brand {
  display: block;
  color: #666;
  font-size: 14px;
  margin-bottom: 12px;
}

.benefit-tag {
  display: inline-block;
  padding: 4px 12px;
  background: #f3f0ff;
  color: #845ef7;
  border-radius: 20px;
  font-size: 14px;
  margin-bottom: 16px;
}

.benefits {
  margin-bottom: 20px;
}

.benefit-item {
  margin-bottom: 8px;
  color: #495057;
  font-size: 14px;
}

.button-group {
  display: flex;
  gap: 8px;
}

.detail-btn, .register-btn {
  flex: 1;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.detail-btn {
  background: #1a1438;
  color: white;
  text-decoration: none;
  text-align: center;
}

.register-btn {
  background: #f8f9fa;
  color: #1a1438;
  border: 1px solid #e9ecef;
}

.detail-btn:hover {
  background: #2d1d5c;
}

.register-btn:hover {
  background: #e9ecef;
}

.no-cards {
  text-align: center;
  padding: 40px;
  color: #666;
}
</style>