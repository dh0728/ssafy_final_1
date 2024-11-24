<template>
  <div class="evaluation-content">
    <div class="character-section">
      <div class="character">
        <img src="@/assets/ping.webp" alt="GPT 캐릭터" class="character-image">
      </div>
      <div class="speech-bubble">
        <div class="evaluation-text" v-if="evaluationStore.evaluation">
          {{ evaluationStore.evaluation }}
        </div>
        <div class="loading" v-else>
          <span>소비 패턴을 분석하고 있어요</span>
          <div class="dots">
            <span>.</span>
            <span>.</span>
            <span>.</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useEvaluationStore } from '@/stores/evaluation.js'

const evaluationStore = useEvaluationStore()

onMounted(() => {
  // evaluationStore.getEvaluation()
})
</script>

<style scoped>
.character-section {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  margin-bottom: 32px;
}

.character {
  flex-shrink: 0;
  width: 120px;
  height: 120px;
  background: #f3f0ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(76, 110, 245, 0.15);
}

.character-image {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.speech-bubble {
  position: relative;
  background: #f8f9fa;
  padding: 24px;
  border-radius: 16px;
  flex: 1;
}

.speech-bubble::before {
  content: '';
  position: absolute;
  left: -12px;
  top: 24px;
  border-style: solid;
  border-width: 12px 12px 12px 0;
  border-color: transparent #f8f9fa transparent transparent;
}

.evaluation-text {
  font-size: 15px;
  line-height: 1.6;
  color: #1a1438;
  white-space: pre-line;
}

.loading {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #4B5563;
}

.dots span {
  animation: dots 1.5s infinite;
  opacity: 0;
}

.dots span:nth-child(2) {
  animation-delay: 0.5s;
}

.dots span:nth-child(3) {
  animation-delay: 1s;
}

@keyframes dots {
  0%, 100% { opacity: 0; }
  50% { opacity: 1; }
}

.action-section {
  display: flex;
  justify-content: center;
  margin-top: 24px;
}

.evaluate-btn {
  padding: 12px 24px;
  background: #4C6EF5;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(76, 110, 245, 0.2);
}

.evaluate-btn:hover {
  background: #4263eb;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 110, 245, 0.3);
}

.evaluate-btn:disabled {
  background: #9CA3AF;
  cursor: not-allowed;
  transform: none;
}
</style>