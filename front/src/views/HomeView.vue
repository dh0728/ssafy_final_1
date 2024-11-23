<template>
  <div class="landing-container">
    <div class="landing-content">
      <!-- 텍스트 섹션 -->
      <div class="text-section">
        <h1>
          <div>영수증 한 장으로</div>
          <div>시작되는</div>
          <div>스마트한 금융생활</div>
        </h1>
        <div class="subtitle">당신의 소비, 더 현명한 선택으로</div>
      </div>

      <!-- 카드 섹션 -->
      <div class="card-section">
        <div class="card">
          <video
              class="card-video"
              autoplay
              loop
              muted
              playsinline
          >
            <source src="https://static.toss.im/3d/Card_m_FFFFF-02.mp4" type="video/mp4">
          </video>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.landing-container {
  width: 100%;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding-top: 100px;
}

.landing-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  width: 100%;
  position: relative;
}

.text-section {
  flex: 1;
  position: relative;
  z-index: 2; /* 텍스트를 비디오 위로 올림 */
}

.card-section {
  position: absolute;
  right: -100px; /* 오른쪽으로 더 밀어냄 */
  top: 50%;
  transform: translateY(-50%);
}

.card {
  width: 500px;
  height: 500px;
  position: relative;
  background: none; /* 배경 제거 */
  box-shadow: none; /* 그림자 제거 */
}

.card-video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  opacity: 0.8; /* 비디오 투명도 조절 */
}


h1 {
  font-size: 48px;
  font-weight: 700;
  color: #1a1438;
  line-height: 1.3;
  margin-bottom: 24px;
}

.subtitle {
  font-size: 20px;
  color: #666;
}

/* 카드 섹션 스타일 */


/* 반응형 스타일 */
@media (max-width: 768px) {
  .landing-content {
    flex-direction: column;
    text-align: center;
    gap: 40px;
  }

  h1 {
    font-size: 36px;
  }

  .card-section {
    height: 400px;
  }

  .card {
    width: 280px;
    height: 175px;
  }
}
</style>