<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h2>등록된 카드 목록</h2>
        <button class="close-btn" @click="$emit('close')">×</button>
      </div>
      <div class="modal-body">
        <div class="my-cards">
          <!-- 신용카드 섹션 -->
          <div v-if="myCards.credit_cards && myCards.credit_cards.length > 0">
            <h3 class="section-title">신용카드</h3>
            <div class="cards-grid">
              <div v-for="card in myCards.credit_cards" :key="card.credit_card_id" class="card-item">
                <button class="delete-btn" @click="deleteCard(1, card.credit_card_id)">×</button>
                <div class="card-image">
                  <img :src="card.img_path" :alt="card.credit_card_name">
                </div>
                <div class="card-info">
                  <h3>{{ card.credit_card_name }}</h3>
                  <span class="card-brand">{{ card.brand }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 체크카드 섹션 -->
          <div v-if="myCards.check_cards && myCards.check_cards.length > 0">
            <h3 class="section-title">체크카드</h3>
            <div class="cards-grid">
              <div v-for="card in myCards.check_cards" :key="card.check_card_id" class="card-item">
                <button class="delete-btn" @click="deleteCard(2, card.check_card_id)">×</button>
                <div class="card-image">
                  <img :src="card.img_path" :alt="card.check_card_name">
                </div>
                <div class="card-info">
                  <h3>{{ card.check_card_name }}</h3>
                  <span class="card-brand">{{ card.brand }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 카드가 없는 경우 -->
          <div v-if="(!myCards.credit_cards?.length && !myCards.check_cards?.length)" class="no-cards">
            <p>등록된 카드가 없습니다.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCardStore } from "@/stores/cards.js"
import { storeToRefs } from 'pinia'

const store = useCardStore()
const { myCard: myCards } = storeToRefs(store)

const deleteCard = async (cardType, cardId) => {
  if (confirm('정말 이 카드를 삭제하시겠습니까?')) {
    try {
      await store.deleteMyCard(cardType, cardId)
      await store.getMyCards()
      alert('카드가 삭제되었습니다.')
    } catch (error) {
      alert('카드 삭제에 실패했습니다.')
      console.error('카드 삭제 실패:', error)
    }
  }
}

onMounted(async () => {
  await store.getMyCards()
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
  min-height: 800px;
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
  color: #333;
}

.close-btn {
  background: none;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #666;
}

.modal-body {
  padding: 0px 0;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 24px;
  padding: 20px;
}

.delete-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 24px;
  height: 24px;
  background: none;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  font-size: 16px;
  color: #666;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  z-index: 2;
}

.delete-btn:hover {
  background: #ff4757;
  color: white;
}

.card-item {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}


.card-item:hover {
  transform: translateY(-5px);
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

.card-info {
  text-align: left;
}

.card-info h3 {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
}

.card-brand {
  display: block;
  color: #666;
  font-size: 14px;
  margin-bottom: 8px;
}

.card-type {
  display: inline-block;
  padding: 4px 12px;
  background: #1a1438;
  color: white;
  border-radius: 20px;
  font-size: 12px;
}

.no-cards {
  text-align: center;
  padding: 40px;
  color: #666;
}

.section-title {
  font-size: 20px;
  font-weight: 600;
  color: #333;
  margin: 24px 0 16px;
  padding-left: 20px;
}
</style>