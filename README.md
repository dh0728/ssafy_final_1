# 📅 가계북
<p align="center">
  <img src="./images/logo.png" width="100%" height="100%" title="px(픽셀) 크기 설정"     alt="logo"></img>
</p>

## ⏳ 프로젝트 진행과정 ##
> SSAFY 12기 1학기 관통 프로젝트<br>
> 개발기간: 2024.11.18 ~ 2024.11.27

## 🔥 가계북 개발 배경
현재에 가계부 서비스는 사용하기가 어렵다는 단점이 있습니다. 이에 저희 팀은 OCR 기술을 도입하여 사용자가 영수증만으로 손쉽게 소비내역을 등록하고 소비 내역을 바탕으로 카드를 추천 받을 수 있는 서비스를 개발하기 위해 이번 프로젝트를 기획하게 되었습니다. 

## 🔧 개발 환경 및 기술 스택 ##

### Frontend ###
<img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"> 
<img src="https://img.shields.io/badge/Chart.js-4FC08D?style=for-the-badge&logo=Chart.js&logoColor=white"> 
<img src="https://img.shields.io/badge/Font Awesome-092E20?style=for-the-badge&logo=Font AWESOME&logoColor=white">

### Backend ###
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=LangChain&logoColor=white">
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white">

### 버전/이슈관리 ###
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">

## 협업 ##
<img src="https://img.shields.io/badge/MATTERMOTST-0058CC?style=for-the-badge&logo=MATTERMOST&logoColor=white">
<img src="https://img.shields.io/badge/DISCORD-5865F2?style=for-the-badge&logo=DISCORD&logoColor=white">

## ERD ##
  <img src="./images/ERD.png" width="100%" height="100%" title="px(픽셀) 크기 설정"     alt="logo"></img>


## REST API URL

### auth ###
<p align="center">
  <img src="./images/accounts.png" width="80%" height="80%" title="px(픽셀) 크기 설정"     alt="logo"></img>
</p>

### 가계부 ###
<p align="center">
  <img src="./images/account.png" width="80%" height="80%" title="px(픽셀) 크기 설정"     alt="logo"></img>
</p>

### 카드 ###
<p align="center">
  <img src="./images/cards.png" width="80%" height="80%" title="px(픽셀) 크기 설정"     alt="logo"></img>
</p>

## 가계북 주요 기능 ##


### 🔔메인페이지 ###

<br>

<p>
  <img src="./images/가계북_메인페이지.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

<hr>

### 📌카드 조회 ###

<br>

#### 카드 조회 ####

<p>
  <img src="./images/가계북_카드조회.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 카테고리별 필터링과 검색 기능을 통해 원하는 카드를 쉽게 찾을 수 있습니다. 각 카드의 주요 혜택과 기본 정보를 카드 리스트에서 바로 확인할 수 있습니다.

#### 카드 상세 페이지 ####

<p>
  <img src="./images/가계북_카드상세페이지.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 선택한 카드의 상세 혜택, 연회비, 전월실적 등 자세한 정보를 제공합니다. 카드사 바로가기를 통해 즉시 카드 신청도 가능합니다.

<hr>

### 📅 캘린더 ###

<br>

#### 달력 ####

<p>
  <img src="./images/가계북_캘린더_기본.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 월별 수입/지출 내역을 캘린더 형태로 시각화하여 제공합니다. 날짜별 거래 내역을 한눈에 파악할 수 있습니다.

#### 내역 ####

<p>
  <img src="./images/가계북_캘린더_내역추가.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 거래 내역을 쉽게 추가하고 관리할 수 있습니다. 수입/지출, 카테고리, 금액, 메모 등 상세 정보를 기록할 수 있습니다.

#### 예산 ####

<p>
  <img src="./images/가계북_캘린더_예산.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 월별 예산을 설정하고 관리할 수 있습니다. 설정된 예산 대비 실제 지출 현황을 추적할 수 있습니다.

#### 금융일정 ####

<p>
  <img src="./images/가계북_캘린더_금융일정.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 정기적인 수입/지출 일정을 등록하고 관리할 수 있습니다. 월세, 공과금 등의 고정 지출을 자동으로 기록할 수 있습니다.

<hr>

### 📝 내역 ###

<br>

#### 내역 조회 ####

<p>
  <img src="./images/가계북_내역_기본.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 전체 거래 내역을 리스트 형태로 확인할 수 있습니다. 카테고리별 필터링과 검색 기능을 제공합니다.

#### 내역 수정삭제 ####

<p>
  <img src="./images/가계북_내역_수정삭제.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 등록된 거래 내역을 간편하게 수정하거나 삭제할 수 있습니다. 잘못 입력된 정보를 즉시 수정할 수 있습니다.

<hr>

### 📸 영수증 인식 ###

<p>
  <img src="./images/가계북_영수증인식.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> OCR 기술을 활용하여 영수증을 자동으로 인식하고 거래 내역을 등록할 수 있습니다. 수기, 전자, 종이영수증 모두 지원합니다.

<hr>

### 📊 주간 월별 분석 ###
<p>
  <img src="./images/가계북_월별일별분석.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 기간별 소비 패턴을 다양한 차트로 분석하여 제공합니다. 지출 추이와 카테고리별 분석을 통해 효율적인 자금 관리가 가능합니다.

<hr>

### 🔍 카테고리별 분석 ###

<p>
  <img src="./images/가계북_카테고리분석.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 카테고리별 지출 현황을 도넛 차트로 시각화하여 제공합니다. 각 카테고리별 상세 내역도 함께 확인할 수 있습니다.

<hr>

### 💳 내카드 목록 ###

<p>
  <img src="./images/가계북_내카드등록.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 사용중인 카드를 등록하고 관리할 수 있습니다. 등록된 카드의 혜택을 쉽게 확인하고 활용할 수 있습니다.

<hr>

### 💸 스마트한 카드 추천 ###

<p>
  <img src="./images/가계북_카드추천.gif" width="50%" height="50%"title="px(픽셀) 크기 설정"alt="main_page"></img>
</p>

> 사용자의 소비 패턴을 분석하여 최적의 카드를 추천해줍니다. 추천된 카드의 상세 정보를 바로 확인하고 신청할 수 있습니다.

<hr>

## 🤬 프로젝트 진행중 어려웠던 점

## 💡 개선하고 싶은 점

## 📝 소감 및 느낀 점

## :family: 팀원 소개 ##
<table align="center">
  <tr>
    <td><div align="center"><b>이지연</div></td>
    <td><div align="center"><b>송동현</div></td>
  </tr>
  <tr>
    <td><img src="/cookiewalk/public/images/임민형.png"></td>
    <td><img src="/cookiewalk/public/images/송동현.png"></td>
  </tr>
  <tr>
    <td><div align="center">프론트엔드</div></td>
    <td><div align="center">백엔드</div></td>
  </tr>
</table>
