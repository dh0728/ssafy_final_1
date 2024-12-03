# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# 크롬 드라이버의 시작과 중지를 담당하는 서비스 클래스
from selenium.webdriver.chrome.service import Service as ChromeService

# 웹의 버전과 dirver의 버전 관리 해주는 라이브러리
from webdriver_manager.chrome import ChromeDriverManager

# 페이지가 완전히 로딩되기 까지 기다릴 수 있게 하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait

# 브라우저 자동 꺼짐 방지 옵션
from selenium.webdriver.chrome.options import Options

# 조건을 설정하고 조건에 부합하는지 판단하는 라이브러리
from selenium.webdriver.support import expected_conditions as EC

# selenium으로 무엇인가 입력하기 위한 import (키보드)
from selenium.webdriver.common.keys import Keys

# 확인하려는 요소가 어떤 속성인지 정의해 확인할 수 있도록 하는 라이브러리
from selenium.webdriver.common.by import By

# 
from selenium.webdriver.common.action_chains import ActionChains

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

import re

from pprint import pprint

import json
import csv 


kinds={
    "모든가맹점":1,
    "교통":2,
    "주유":3,
    "통신":4,
    "마트/편의점":5,
    "쇼핑":6,
    "푸드":7,
    "카페/디저트":8,
    "뷰티/피트니스":9,
    "무실적":10,
    "공과금/렌탈":11,
    "병원/약국":12,
    "애완동물":13,
    "교육/육아":14,
    "자동차/하이패스":15,
    "레저/스포츠":16,
    "영화/문화":17,
    "간편결제":18,
    "항공마일리지":19,
    "공항라운지/PP":20,
    "프리미엄":21,
    "여행/숙박":22,
    "해외":23,
    "비지니스":24,
    "기타":25,
    '금융':26,
    '생활':27,
}

category_dict= {
    '편의점':kinds['마트/편의점'], 
    '여행사':kinds['여행/숙박'], 
    '쇼핑':kinds['쇼핑'],
    '경기관람':kinds['레저/스포츠'], 
    '대중교통':kinds['교통'],
    '홈쇼핑':kinds['쇼핑'],
    '적립':kinds['무실적'], 
    '카페/디저트':kinds['카페/디저트'],
    '항공권':kinds['여행/숙박'],
    '해외직구':kinds['해외'],
    '해피포인트':kinds['무실적'],
    '저녁':kinds['푸드'],
    '고속버스':kinds['교통'],
    '간편결제':kinds['간편결제'],
    '공연/전시':kinds['영화/문화'], 
    '온라인쇼핑':kinds['쇼핑'],
    '아시아나항공':kinds['항공마일리지'], 
    'KT':kinds['통신'], 
    '동물병원':kinds['애완동물'], 
    '라운지 키':kinds['공항라운지/PP'],
    '보험':kinds['금융'], 
    '네이버페이':kinds['간편결제'], 
    '무이자할부':kinds['무실적'], 
    '애완동물':kinds['애완동물'], 
    '소셜커머스':kinds['쇼핑'], 
    '기차':kinds['교통'],
    '대형마트':kinds['마트/편의점'],
    '온라인 여행사':kinds['여행/숙박'],
    '약국':kinds['병원/약국'], 
    '대한항공':kinds['항공마일리지'],
    '피트니스':kinds['뷰티/피트니스'],
    '골프':kinds['레저/스포츠'],
    '은행사':kinds['금융'],
    '렌탈':kinds['공과금/렌탈'], 
    '혜택 프로모션':kinds['무실적'],
    '일반음식점':kinds['푸드'],
    '베이커리':kinds['카페/디저트'],
    '무실적':kinds['무실적'], 
    '생활':kinds['생활'], 
    '멤버십포인트':kinds['무실적'],
    '교육/육아':kinds['교육/육아'], 
    '캐시백':kinds['무실적'],
    '하이브리드':kinds['자동차/하이패스'], 
    '화장품':kinds['뷰티/피트니스'], 
    '유의사항':kinds['무실적'], 
    'CJ ONE':kinds['무실적'], 
    '국내외가맹점':kinds['모든가맹점'], 
    '아울렛':kinds['쇼핑'], 
    '제주항공':kinds['항공마일리지'],
    '카카오페이':kinds['간편결제'], 
    '카드사':kinds['금융'], 
    '보험사':kinds['금융'], 
    '수수료우대':kinds['해외'], 
    '음원사이트':kinds['영화/문화'], 
    '도서':kinds['영화/문화'], 
    '병원':kinds['병원/약국'],
    '주유소':kinds['주유'],
    '드럭스토어':kinds['뷰티/피트니스'], 
    '영화':kinds['영화/문화'], 
    '지역':kinds['무실적'], 
    '비즈니스':kinds['비지니스'], 
    '여행/숙박':kinds['여행/숙박'], 
    '항공마일리지':kinds['항공마일리지'], 
    '병원/약국':kinds['병원/약국'], 
    '국민행복':kinds['교육/육아'], 
    '자동차/하이패스':kinds['자동차/하이패스'], 
    '렌터카':kinds['여행/숙박'], 
    '패스트푸드':kinds['푸드'], 
    '게임':kinds['레저/스포츠'], 
    '저가항공':kinds['항공마일리지'], 
    '공과금/렌탈':kinds['공과금/렌탈'], 
    '점심':kinds['푸드'], 
    '카페':kinds['카페/디저트'], 
    '공항라운지':kinds['공항라운지/PP'], 
    '바우처':kinds['프리미엄'], 
    '연회비지원':kinds['무실적'], 
    'SKT':kinds['통신'], 
    '자동차':kinds['자동차/하이패스'], 
    '해외이용':kinds['해외'], 
    '리조트':kinds['여행/숙박'], 
    '주유':kinds['주유'], 
    '학원':kinds['교육/육아'], 
    '레저/스포츠':kinds['레저/스포츠'], 
    '충전소':kinds['주유'],
    '헤어':kinds['뷰티/피트니스'],
    '기타':kinds['기타'],
    '공과금':kinds['공과금/렌탈'], 
    '영화/문화':kinds['영화/문화'], 
    '백화점':kinds['쇼핑'], 
    '선택형':kinds['기타'],
    '공항':kinds['여행/숙박'],
    '학습지':kinds['교육/육아'],
    'BC TOP':kinds['무실적'],
    '교통':kinds['교통'], 
    '삼성페이':kinds['간편결제'], 
    '테마파크':kinds['레저/스포츠'], 
    'SSM':kinds['마트/편의점'], 
    '어린이집':kinds['교육/육아'], 
    '모든가맹점':kinds['모든가맹점'], 
    'LGU+':kinds['통신'], 
    '문화센터':kinds['교육/육아'], 
    '패밀리레스토랑':kinds['푸드'], 
    '할인':kinds['무실적'], 
    '호텔':kinds['여행/숙박'], 
    '인테리어':kinds['쇼핑'],
    '하이패스':kinds['자동차/하이패스'], 
    '뷰티/피트니스':kinds['뷰티/피트니스'], 
    'SPA브랜드':kinds['쇼핑'], 
    '정비':kinds['자동차/하이패스'], 
    '해외':kinds['해외'], 
    '진에어':kinds['항공마일리지'],
    '프리미엄':kinds['프리미엄'], 
    '푸드':kinds['푸드'], 
    '금융':kinds['금융'], 
    '프리미엄 서비스':kinds['프리미엄'], 
    '제휴/PLCC':kinds['무실적'], 
    '유치원':kinds['교육/육아'], 
    '면세점':kinds['쇼핑'], 
    '택시':kinds['교통'], 
    'PP':kinds['공항라운지/PP'], 
    'OK캐쉬백':kinds['무실적'], 
    '배달앱':kinds['푸드'], 
    '디지털구독':kinds['생활'], 
    '공항라운지/PP':kinds['공항라운지/PP'], 
    '마트/편의점':kinds['마트/편의점'], 
    'APP':kinds['간편결제'], 
    '통신':kinds['통신']
    }
# 크롤링한 카드 데이터 들어갈 곳
card_ben_list = []
cnt=1

# 브라우저 자동 꺼짐 방지 옵션 객체 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 드라이버 객체 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# driver을 정해진 시간 동안 기다림
wait = WebDriverWait(driver,10)

# 테스트용 url
# https://card-gorilla.com/search/card?cate=CRD&search_benefit=11,5,21,9,23,16,22,24
try:
    driver.get('https://www.card-gorilla.com/search/card?cate=CHK') #카드고릴라 체크카드 조회 423개
    
    while True: # 더이상 더보기 버튼 없을떄 까지 더보기 버튼 누르면서 내려가기
        try:
            try:
                WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]")))
                close_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/button")
                driver.execute_script("arguments[0].click();", close_button)
                print("모달 창 닫힘")
                time.sleep(1)  # 모달 창이 닫힐 시간 기다림
            except:
                print("모달 창 없음")
            
            next_button = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, 
                    '//*[@id="q-app"]/section/div[1]/section/div/article[1]/article/a')
                )
            )
            # perform 저장된 모든 작업 수행
            ActionChains(driver).move_to_element(next_button).perform()
            time.sleep(1)
            next_button.click()
        except Exception as e:
            print(f'더보기 버튼 오류: {e}')
            break

    # 모든 카드 리스트가 있는 ul 태그 찾기
    ul_tag = driver.find_element(By.XPATH,'//*[@id="q-app"]/section/div[1]/section/div/article[1]/article/ul')
    # print(ul_tag)

    # 모든 카드 리스트 li 태그 찾기
    li_list=ul_tag.find_elements(By.TAG_NAME,'li')
    # print(li_list)

    #이제 자세히 보기 각 리스트마다 자세히 보기 버튼 찾고 눌러서 들어가기
    for idx, li in enumerate(li_list):
        #모달창 뜨나 확인하기
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]")))
            close_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/button")
            driver.execute_script("arguments[0].click();", close_button)
            print("모달 창 닫힘")
            time.sleep(1)  # 모달 창이 닫힐 시간 기다림
        except:
            print("모달 창 없음")
        detail_btn = li.find_element(By.CLASS_NAME,'b_view')

        while True:
            time.sleep(1)
            # Contorl 키 누르고 자세히 보기 버튼 눌러야 새창으로 열림
            ActionChains(driver).move_to_element(detail_btn).key_down(Keys.CONTROL).click(detail_btn).key_up(Keys.CONTROL).perform()
            
            time.sleep(1)
            # 두 번째 탭으로 제어를 이동
            driver.switch_to.window(driver.window_handles[1])
            if driver.current_url != "https://www.card-gorilla.com/home": # 재대로 이동했으면
                break
            else:
                driver.close() #현재 탭 닫고
                driver.switch_to.window(driver.window_handles[0]) #다시 원래 탭으로 돌아가기

        # 주요 혜택 추출하기
        try:
            bene_area_tag = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="lst bene_area"]')
                )
            )
            dl_list = bene_area_tag.find_elements(By.TAG_NAME, "dl")
            viewport_width = driver.execute_script("return window.innerWidth;")
            viewport_height = driver.execute_script("return window.innerHeight;")
        

            for dl in dl_list:

                # credit_card 랑 category 중계 테이블 데이터 수집
                card_to_category={}
                card_to_category['model']="cards.check_card_category"
                fields={}
                fields['check_card_category_id']=cnt
                cnt +=1 
                fields['check_card_id']=idx+1


                # 요소가 화면 중앙에 오도록 스크롤
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dl)
                time.sleep(0.1)  # 스크롤 후 약간 대기
        
                # ActionChains를 사용하여 요소 클릭
                ActionChains(driver).move_to_element(dl).click().perform()
                WebDriverWait(dl, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "dd"))
                )
        
                # 혜택 타이틀
                try:
                    title = dl.find_element(By.TAG_NAME,'p').text
                    fields['title']=title
                    fields['category_id']=category_dict[title]
                except:
                    title = "No"

                # 혜택 설명 
                try:
                    desc = dl.find_element(By.TAG_NAME,'i').text
                    fields['desc']=desc
                except:
                    fields['desc']='No'

                # 혜택 상세 설명 
                try:
                    detail_desc = dl.find_element(By.TAG_NAME,'dd').text
                    fields['desc_detail']=detail_desc
                except:
                    fields['desc_detail']='No'
        
                # 혜택 정보 저장
                # pprint(benefit)
                card_to_category['fields']=fields
                pprint(card_to_category)
                # 전체 카드 데이터에 주요 혜택 저장
                card_ben_list.append(card_to_category)
                # pprint(card_ben_list)

        
        except Exception as e:
            print(f"혜택 추출 오류: {e}")

        # 다 저장 했으면
        driver.close() # 디테일 페이지 탭 닫기
        driver.switch_to.window(driver.window_handles[0]) # 원래 탭으로 이동

    # Json 파일을 저장할 경로
    card_ben_list_file_path = './check_card_category.json'

    # Json 데이터를 파일로 쓰기
    with open(card_ben_list_file_path, 'w', encoding='utf-8') as file:
        json.dump(card_ben_list,file,ensure_ascii=False, indent=4)

    card_ben_list_file_csv_path = './check_card_category.csv'

    # CSV 파일로 쓰기
    with open(card_ben_list_file_csv_path, 'w', newline='', encoding='utf-8') as file:
        # CSV writer 생성
        csv_writer = csv.writer(file)
    
        # 헤더 쓰기 (예시: JSON 데이터의 키를 헤더로 사용)
        if card_ben_list:
            csv_writer.writerow(card_ben_list[0].keys())  # 첫 번째 딕셔너리의 키들을 헤더로 사용
    
        # 데이터 쓰기
        for benefit in card_ben_list:
            csv_writer.writerow(benefit.values())  # 각 딕셔너리의 값들을 한 줄씩 쓰기

except Exception as e:
    print(f'오류 발생: {e}')        