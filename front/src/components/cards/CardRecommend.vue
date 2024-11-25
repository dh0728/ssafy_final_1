<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h2>스마트한 카드 추천</h2>
        <button class="close-btn" @click="$emit('close')">×</button>
      </div>

      <div class="modal-body">
        <div class="recommendation-section">
          <div id="cardCarousel" class="carousel">
            <div class="carousel-inner">
              <!-- 신용카드 -->
              <div v-for="(card, index) in allCards"
                   :key="card.id"
                   :class="['carousel-item', index === 0 ? 'active' : '']">
                <div class="card-item">
                  <div class="card-image">
                    <div :class="['benefit-tag', card.type]">
                      {{ card.type === 'credit' ? '추천 신용카드' : '추천 체크카드' }}
                    </div>
                    <img :src="card.img_path" :alt="card.name">
                  </div>
                  <div class="card-info">
                    <h4>{{ card.name }}</h4>
                    <span class="card-brand">{{ card.brand }}</span>
                    <div class="button-group">
                      <RouterLink
                          :to="{ name: 'CardDetail', params: { type: card.type, cardId: card.id }}"
                          class="detail-btn">
                        자세히 보기
                      </RouterLink>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <button class="carousel-control prev" @click="prevSlide">
              <span class="carousel-control-prev-icon">←</span>
            </button>
            <button class="carousel-control next" @click="nextSlide">
              <span class="carousel-control-next-icon">→</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue'
import { useCardStore } from "@/stores/cards.js"

const store = useCardStore()
const currentIndex = ref(0)

const allCards = computed(() => {
  const creditCards = store.recommendCards?.credit_cards?.map(card => ({
    ...card,
    type: 'credit',
    id: card.credit_card_id,
    name: card.credit_card_name
  })) || []

  const checkCards = store.recommendCards?.check_cards?.map(card => ({
    ...card,
    type: 'check',
    id: card.check_card_id,
    name: card.check_card_name
  })) || []

  return [...creditCards, ...checkCards]
})

const prevSlide = () => {
  const items = document.querySelectorAll('.carousel-item')
  items[currentIndex.value].classList.remove('active')
  currentIndex.value = (currentIndex.value - 1 + items.length) % items.length
  items[currentIndex.value].classList.add('active')
}

const nextSlide = () => {
  const items = document.querySelectorAll('.carousel-item')
  items[currentIndex.value].classList.remove('active')
  currentIndex.value = (currentIndex.value + 1) % items.length
  items[currentIndex.value].classList.add('active')
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
  width: 400px;
  min-height: 600px;
  max-height: 90vh;
  overflow-y: auto;
}

.recommendation-section {
  padding: 0px;
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

.card-item {
  background: white;
  border-radius: 14px;
  padding: 20px;
  height: 380px; /* 높이 조정 */
  display: flex;
  flex-direction: column;
  position: relative;
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
  padding-top: 20px;
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

.button-group {
  display: flex;
  gap: 8px;
  margin-top: auto; /* 버튼을 하단에 배치 */
  position: absolute;
  bottom: 16px;
  left: 16px;
  right: 16px;
}

.detail-btn, .register-btn {
  flex: 1;
  padding: 8px 0;
  border-radius: 8px;
  font-size: 11px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.detail-btn {
  background: #f8f9fa;
  color: #1a1438;
  border: 1px solid #e9ecef;
  text-decoration: none;
}


.detail-btn:hover {
  background: #2d1d5c;
}

.register-btn:hover {
  background: #e9ecef;
}

.benefit-tag.credit {
  background: #f3f0ff;
  color: #845ef7;
}

.benefit-tag.check {
  background: #e7f5ff;
  color: #339af0;
}

.carousel {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
}

.carousel-inner {
  position: relative;
  width: 100%;
  height: 100%;
}

.carousel-item {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease;
  display: flex;
  justify-content: center;
}

.carousel-item.active {
  opacity: 1;
}

.carousel-control {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  background: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 2;
}

.carousel-control.prev {
  left: 20px;
}

.carousel-control.next {
  right: 20px;
}

.card-item {
  width: 300px;
  margin: 0 auto;
}

</style>