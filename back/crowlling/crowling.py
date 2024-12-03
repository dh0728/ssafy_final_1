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

# 카드 수수료 정보를 파싱하고, 숫자로 변환하는 함수
def parse_fee(text):
    fee_dict = {}
    # 정규 표현식을 사용하여 "국내전용", "해외겸용"과 금액을 추출
    matches = re.findall(r"(국내전용|해외겸용)\s*(\d+,*\d*원|없음)", text)
    for match in matches:
        key, value = match
        if value == "없음":
            fee_dict[key] = "없음"
        else:
            # "원" 제거 후 ","를 없애고 정수로 변환
            numeric_value = int(value.replace("원", "").replace(",", ""))
            fee_dict[key] = numeric_value
    return fee_dict


# 크롤링한 카드 데이터 들어갈 곳
card_data_list = []
card_ben_list = []

# 브라우저 자동 꺼짐 방지 옵션 객체 생성
chrome_options = Options()
# chrome_options.add_argument("headless")
chrome_options.add_experimental_option("detach",True)
# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 드라이버 객체 생성
driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

# driver을 정해진 시간 동안 기다림
wait = WebDriverWait(driver,10)

# 테스트용 url
# https://card-gorilla.com/search/card?cate=CRD&search_benefit=11,5,21,9,23,16,22,24
try:
    driver.get('https://card-gorilla.com/search/card?cate=CRD') #카드고릴라 신용카드 조회 976개
    
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

        # 이제 스크래핑 시작
        card_data={}
        card_data['model']="cards.Credit_cards"
        fields={}
        fields['credit_card_id']=idx+1

        # 카드 이름 추출
        card_name = wait.until(EC.presence_of_element_located((By.XPATH,'//strong[@class="card"]')))
        fields['credit_card_name']=card_name.text
        
        # 카드 브랜드 추출
        brand = wait.until(EC.presence_of_element_located((By.XPATH,'//p[@class="brand"]')))
        fields['brand']=brand.text

        # 카드 이미지 경로 추출
        card_img = driver.find_element(By.XPATH, '//div[@class="card_img"]')
        img_tag = card_img.find_element(By.TAG_NAME, "img")
        fields["img_path"] = img_tag.get_attribute("src")

        # 카드 연회비
        year_cost_tag= driver.find_element(By.XPATH,'//div[@class="bnf2"]')
        dl_tags=year_cost_tag.find_elements(By.TAG_NAME,'dl')
        for idx, dl in enumerate(dl_tags):
            dd_tag =dl.find_element(By.TAG_NAME,'dd')
            if idx ==0: # 첫번 째 dl 태그는 연회비 있음
                year_cost__dict = {} # 연회비 정보 담는 딕셔너리
                span_tags=dd_tag.find_elements(By.TAG_NAME,'span')
                for i, span in enumerate(span_tags):
                    fees = parse_fee(span.text)
                    # print(fees)
                    for key ,value in fees.items():
                        if key == '국내전용':
                            fields['domestic_fee']=value
                        elif key =='해외겸용':
                            fields['abroad_fee']=value
            elif idx==1: # 전월 실적
                fields['pre_month_perform']=dd_tag.text 
        
        card_url=driver.current_url
        print("Card URL:", card_url)
        fields["bank_url"] = card_url
        driver.close() #현재 탭 닫고
        driver.switch_to.window(driver.window_handles[0])

        # 카드사 url로 이동 페이지 
        # 현재 app_btn이 있는 경우 ,inactive 인 경우, 버튼 자체가 없는 경우 3가지로 나눠져 있음
        # try:
            # 데이터 영역 내의 app_btn 클래스를 가진 div 찾기
            #div_area = driver.find_element(By.XPATH, '//div[contains(@class,"data_area")]')
            #app_btn = div_area.find_element(By.XPATH, './/div[@class="app_btn"]')
            
            # # 클릭해보기
            # time.sleep(1)
            # # Contorl 키 누르고 자세히 보기 버튼 눌러야 새창으로 열림
            # ActionChains(driver).move_to_element(app_btn).key_down(Keys.CONTROL).click(app_btn).key_up(Keys.CONTROL).perform()

            # time.sleep(1)
            # # 두 번째 탭으로 제어를 이동
            # WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 2)
            # driver.switch_to.window(driver.window_handles[2])

            # WebDriverWait(driver, 10).until(
            #     lambda d: d.current_url if d.current_url != "about:blank" and 'bridge' not in d.current_url else False
            # )
            
            # card_url=driver.current_url
            # print("Card URL:", card_url)
            # fields["bank_url"] = card_url
            # driver.close() #현재 탭 닫고
            # driver.switch_to.window(driver.window_handles[1]) #다시 원래 탭으로 돌아가기

        # except Exception as e:
            # print(f'카드사 url 추출 오류: {e}')
            # fields["bank_url"] = driver.current_url
        

        # 다 저장 했으면
        # driver.close() # 디테일 페이지 탭 닫기
        # driver.switch_to.window(driver.window_handles[0]) # 원래 탭으로 이동
        card_data['fields']=fields
        card_data_list.append(card_data)
        print(len(card_data_list))
    pprint(card_data_list)

    # Json 파일을 저장할 경로
    file_path = './CardData.json'


    # Json 데이터를 파일로 쓰기
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(card_data_list,file,ensure_ascii=False, indent=4)

    

except Exception as e:
    print(f'오류 발생: {e}')        