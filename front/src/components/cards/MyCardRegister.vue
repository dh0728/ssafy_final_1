<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h2>내 카드 설정</h2>
        <button class="close-btn" @click="$emit('close')">×</button>
      </div>
      <div class="modal-body">
        <div class="my-cards">
          <div v-if="store.myCard && store.myCard.length > 0" class="cards-grid">
            <div v-for="card in store.myCard" :key="card.id" class="card-item">
              <div class="card-image">
                <img :src="card.img_path" :alt="card.name">
              </div>
              <div class="card-info">
                <h3>{{ card.name }}</h3>
                <span class="card-brand">{{ card.brand }}</span>
                <div class="card-type">
                  {{ card.card_type === 1 ? '신용카드' : '체크카드' }}
                </div>
                <button class="delete-btn" @click="deleteCard(card)">삭제</button>
              </div>
            </div>
          </div>
          <div v-else class="no-cards">
            <p>등록된 카드가 없습니다.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCardStore } from "@/stores/cards.js"

const store = useCardStore()

const deleteCard = async (card) => {
  if (confirm('카드를 삭제하시겠습니까?')) {
    await store.deleteMyCard(card.card_type, card.id)
    await store.getMyCards()
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
  padding: 20px 0;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 24px;
  padding: 20px;
}

.delete-btn {
  margin-top: 12px;
  padding: 6px 12px;
  background: #ff4757;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: background 0.2s ease;
}

.delete-btn:hover {
  background: #ff6b81;
}

.card-item {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.2s ease;
  position: relative;
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
</style>