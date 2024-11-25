<template>
<div class="home-container">
  <section class="main-banner">
    <div class="banner-content">
      <h1 class="main-title">
        영수증 한 장으로<br>
        시작되는<br>
        스마트한 금융생활
      </h1>
      <p class="sub-title">당신의 소비, 더 현명한 선택으로</p>
    </div>
    <div class="banner-image">
      <div class="card-visual">
        <div class="card-container">
          <div class="card-inner">
            <img src="../assets/white-card.png" alt="흰 카드 이미지" class="card-front">
            <img src="../assets/black-card.png" alt="검은 카드 이미지" class="card-back">
          </div>
        </div>
        <div class="shape-elements">
          <div class="shape shape-1"></div>
          <div class="shape shape-2"></div>
          <div class="shape shape-3"></div>
          <div class="shape shape-4"></div>
          <div class="shape shape-5"></div>
          <div class="shape shape-6"></div>
          <div class="shape shape-7"></div>
        </div>
      </div>
    </div>
  </section>

    <!-- 주요 기능 섹션 -->
    <section class="features">
      <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>스마트한 분석</h3>
        <p>AI가 분석하는 맞춤형 소비 패턴</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">💳</div>
        <h3>카드 추천</h3>
        <p>나의 소비에 최적화된 카드 추천</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">📱</div>
        <h3>간편한 관리</h3>
        <p>영수증 촬영으로 쉬운 가계부 작성</p>
      </div>
    </section>

  <section class="service-section">
    <div class="service-content">
      <div class="service-text">
        <h2>맞춤 금융 가이드</h2>
        <div class="title-group">
          <h3>영수증 속</h3>
          <h3>숨겨진 혜택,</h3>
          <h3>저희가 찾아드릴게요</h3>
        </div>
      </div>

      <div class="service-cards">
        <RouterLink to="/calendar" class="service-card">
          <div class="card-icon">
            <i class="ph ph-device-mobile"></i>
          </div>
          <div class="card-text">
            <h4>CALENDAR</h4>
            <p>휘리릭 기록되는 나의 소비</p>
          </div>
        </RouterLink>

        <RouterLink to="/search" class="service-card">
          <div class="card-icon">
            <i class="ph ph-smiley"></i>
          </div>
          <div class="card-text">
            <h4>SEARCH</h4>
            <p>클릭 한 번으로 찾는 카드</p>
          </div>
        </RouterLink>

        <RouterLink to="/analysis" class="service-card">
          <div class="card-icon">
            <i class="ph ph-chart-line"></i>
          </div>
          <div class="card-text">
            <h4>ANALYSIS</h4>
            <p>당신의 소비를 읽어드립니다</p>
          </div>
        </RouterLink>

        <RouterLink to="/recommend" class="service-card">
          <div class="card-icon">
            <i class="ph ph-star"></i>
          </div>
          <div class="card-text">
            <h4>RECOMMEND</h4>
            <p>더 현명한 선택을 위한 제안</p>
          </div>
        </RouterLink>
      </div>
    </div>
  </section>
</div>
<footer class="footer-container">
    <div class="footer-content">
        <div class="contact-info">
            <p>고객센터</p>
            <p>전화: 1661-7654(24시간 연중무휴)</p>
            <p>해외전화: +82-2-6975-9000</p>
            <p>이메일: help@tossbank.com</p>
        </div>
        <div class="company-info">
            <p>등록번호: 462-86-01671</p>
            <p>주소: 06133 서울특별시 강남구 테헤란로 131, 13층 (삼성, 한국지사사이트)</p>
            <p>대표: 이민이</p>
        </div>
        <div class="links">
            <a href="#"><img src="" alt="social_icon_1"></a>
            <a href="#"><img src="" alt="social_icon_2"></a>
            <a href="#"><img src="" alt="social_icon_3"></a>
            <a href="#"><img src="" alt="social_icon_4"></a>
        </div>
    </div>
</footer>
</template>


<style scoped>
.home-container {
  max-width: 1200px;
  margin: 0 auto;
}

.card-container {
  width: 600px;
  height: 380px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  cursor: pointer;
  animation: float 6s ease-in-out infinite;
  transform-style: preserve-3d;
  perspective: 1000px;
  z-index: 2;
}

.main-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 600px;
  margin-bottom: 10px;
}

.banner-content {
  flex: 1;
  padding-right: 60px;
}

.main-title {
  font-size: 48px;
  font-weight: 700;
  color: #1a1438;
  line-height: 1.3;
  margin-bottom: 24px;
}

.sub-title {
  font-size: 20px;
  color: #666;
  margin-bottom: 40px;
}

.banner-image {
  flex: 1;
  position: relative;
}

.card-visual {
  position: relative;
  height: 600px;
}

.shape-elements {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.shape {
  position: absolute;
  border-radius: 50%;
}

.shape-1 {
  width: 80px;
  height: 80px;
  background: #FFB946;
  top: 10%;
  right: 20%;
}

.shape-2 {
  width: 60px;
  height: 60px;
  background: #4C6EF5;
  bottom: 20%;
  left: 10%;
}

.shape-3 {
  width: 40px;
  height: 40px;
  background: #1BBF83;
  top: 30%;
  left: 15%;
}

.shape-4 {
  width: 70px;
  height: 70px;
  background: #FF8E99;
  bottom: 15%;
  right: 15%;
}

.shape-5 {
  width: 50px;
  height: 50px;
  background: #845EF7;
  top: 20%;
  left: 25%;
}

.shape-6 {
  width: 45px;
  height: 45px;
  background: #339AF0;
  bottom: 35%;
  right: 25%;
}

.shape-7 {
  width: 35px;
  height: 35px;
  background: #51CF66;
  top: 40%;
  right: 10%;
}

.features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 0px;
}

.feature-card {
  background: white;
  padding: 32px;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
}

.feature-icon {
  font-size: 40px;
  margin-bottom: 16px;
}

.feature-card h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 12px;
}

.feature-card p {
  color: #666;
  font-size: 16px;
  line-height: 1.5;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 1.0s;
  transform-style: preserve-3d;
  z-index: 1;
}

.card-container:hover {
  animation-play-state: paused;
}

.card-container:hover .card-inner {
  transform: rotateY(360deg);
}

.card-front,
.card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  object-fit: contain;
  pointer-events: none;
  -webkit-backface-visibility: hidden; /* Safari 지원 */
  z-index: 2;
}

.card-front {
  transform: rotateY(0deg);
}

.card-back {
  transform: rotateY(180deg);
}

.card-visual {
  position: relative;
  height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
}

@keyframes float {
  0%, 100% {
    transform: translate(-50%, -50%);
  }
  50% {
    transform: translate(-50%, -60%);
  }
}

@media (max-width: 768px) {
  .main-banner {
    flex-direction: column;
    text-align: center;
  }

  .banner-content {
    padding-right: 0;
    margin-bottom: 40px;
  }

  .features {
    grid-template-columns: 1fr;
  }
}

/* 호버 시 float 애니메이션 일시 정지 */
.card-container:hover {
  animation-play-state: paused;
}

.service-section {
  padding: 160px 0; /* 더 넓은 상하 여백 */
  margin: 80px 0;
  background: #fff;
}

.service-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex; /* 변경: flex로 변경하여 나란히 배치 */
  align-items: flex-start; /* 상단 정렬 */
  gap: 60px; /* 섹션 간격 */
}

.service-text {
  flex: 1; /* 텍스트 영역 비율 */
}

.service-text h2 {
  color: #666;
  letter-spacing: -0.02em; /* 글자 간격 축소 */
}


.title-group h3 {
  margin-top: 20px;
  font-size: 40px;
  font-weight: 700;
  color: #1a1438;
  line-height: 1.1; /* 줄 간격 축소 */
  letter-spacing: -1.5px;
}

.service-section {
  padding: 120px 0; /* 180px에서 줄임 */
  background: #fff;
}

.service-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.service-text {
  flex: 1;
  opacity: 0;
  transform: translateY(-20px);
  animation: slideDown 0.8s ease forwards;
}

.service-text h2 {
  font-size: 20px; /* 24px에서 줄임 */
  color: #666;
  margin-bottom: 16px; /* 20px에서 줄임 */
}

.title-group h3 {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: 40px;
  font-weight: 700;
  color: #1a1438;
  line-height: 1.1;
  letter-spacing: -1.5px;
  opacity: 0;
  transform: translateY(-20px);
}

.title-group h3:nth-child(1) {
  animation: slideDown 0.6s ease forwards 0.2s;
}

.title-group h3:nth-child(2) {
  animation: slideDown 0.6s ease forwards 0.4s;
}

.title-group h3:nth-child(3) {
  animation: slideDown 0.6s ease forwards 0.6s;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.service-cards {
  flex: 1.2;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px; /* 카드 간격 축소 */
  max-width: 500px; /* 카드 영역 전체 너비 제한 */
}

.service-card {
  background: #f8f9fa;
  padding: 20px; /* 패딩 축소 */
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.3s ease;
}

.card-icon {
  font-size: 20px; /* 아이콘 크기 축소 */
  color: #4C6EF5;
  margin-bottom: 12px;
}

.card-text h4 {
  font-size: 20px; /* 제목 크기 축소 */
  font-weight: 600;
  color: #1a1438;
  margin-bottom: 6px;
}

.card-text p {
  font-size: 14px; /* 설명 텍스트 크기 축소 */
  color: #666;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .service-content {
    flex-direction: column;
    gap: 40px;
  }

  .service-cards {
    width: 100%;
    max-width: 100%;
  }
}

.footer-container {
    background-color: #2c2c2c; /* 다크 그레이 배경 */
    color: white;
    padding: 30px;
    font-size: 14px;
    line-height: 1.6;
    width: 100vw; 
    
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    max-width: 1440px;
    margin: 0 auto;
}

.contact-info p, .company-info p {
    margin: 5px 0;
}

.links a {
    margin: 0 10px;
}

.links img {
    width: 24px; /* 소셜 아이콘 크기 조정 */
    height: auto;
}

</style>