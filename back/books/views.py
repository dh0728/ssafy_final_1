from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404 , get_list_or_404
from rest_framework.response import Response
from .models import Account_book, Account_book_data, Budget, Schedule

from .serializers import AccountBookCalendar, AccountBookDataSerializer,BudgetPostPutSerializer, BudgetSerializer, ScheduleSerializer, AccountBookSerializer, MonthlyDataSerializer,AnalysisTimeSerialzer,CategoryExpenseSerializer
from django.db import transaction

from django.conf import settings
from django.core.files.storage import FileSystemStorage
import requests
import time
import uuid
import json
import os

import math

from django.db.models import Q, Sum

from datetime import datetime
from collections import defaultdict

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_calendar(request):  # 캘린더 페이지
    try:
        account_book = get_object_or_404(Account_book, user_id=request.user) 
    except:  # 가계부 인스턴스 없으면 생성
        account_book = Account_book.objects.create(user_id=request.user)
    
    serializer = AccountBookSerializer(account_book)
    return Response(serializer.data)

# 하루치 결제 데이터 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def day(request):
    account_book = get_object_or_404(Account_book, user_id=request.user) 
    if request.method == "GET":
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        day = request.query_params.get('day') 

        account_book_data = Account_book_data.objects.filter(
            account_book_id=account_book.pk,
            day = int(day),
            month = int(month),
            year = int(year)
            )
        serializer = AccountBookCalendar(account_book_data,many=True)
        return Response(serializer.data)

# 한달 내역 데이터 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def month(request):
    account_book = get_object_or_404(Account_book, user_id=request.user) 
    if request.method == "GET":
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        account_book =get_object_or_404(Account_book, user_id=request.user) 

        account_book_data = Account_book_data.objects.filter(
            account_book_id=account_book.pk,
            month = int(month),
            year = int(year)
            )
        serializer = AccountBookCalendar(account_book_data,many=True)
        return Response(serializer.data)


# 고정 스케줄 조회 삽입 수정 삭제
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def schedule(request):
    account_book = get_object_or_404(Account_book, user_id=request.user) 
    if request.method == 'GET':
        schedules = Schedule.objects.filter(
            account_book_id = account_book
        )
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        name = request.data.get('name')
        day = request.data.get('day')
        value = request.data.get('value')
        category_id = request.data.get('category_id')
        is_income = request.data.get('is_income')
        sehedule = {
            'account_book_id':account_book.pk,
            'name': name,
            'day': int(day),
            'value': int(value),
            'category_id': int(category_id),
            'is_income': is_income
        }
        serializer =ScheduleSerializer(data=sehedule)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        schedule_id = request.data.get('schedule_id')
        if not schedule_id:
            return Response({"error":"schedule_id is required for update."},status=status.HTTP_400_BAD_REQUEST)
        
        schedule = get_object_or_404(Schedule,account_book_id = account_book,schedule_id=schedule_id)

        serializer = ScheduleSerializer(schedule, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        schedule_id = request.data.get('schedule_id')
        if not schedule_id:
            return Response({"error": "schedule_id is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        schedule = get_object_or_404(Schedule,account_book_id = account_book,schedule_id=schedule_id)
        schedule.delete()
        return Response({"message": f"Schedule with id {schedule_id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)


# 예산 조회 삽입 및 수정 메서드
@api_view(['GET','POST','PUT'])
@permission_classes([IsAuthenticated])
def budget(request):
    account_book = get_object_or_404(Account_book, user_id=request.user) 
    if request.method == 'GET':
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        print(month)
        month=int(month)
        year=int(year)
        try:
            budget = get_object_or_404(Budget, account_book_id=account_book.pk)
        except:
            budget = Budget.objects.create(month=month,year=year,value=0,account_book_id=account_book)
        serializer = BudgetSerializer(budget)

        return Response(serializer.data)

    elif request.method == 'POST':
        # print(account_book.pk)
        year = request.data.get('year')
        month = request.data.get('month')
        value = request.data.get('value')

        budget = {
            'account_book_id': account_book.pk,
            'month': int(month),
            'value': int(value),
            'year' : int(year),
        }
        serializer =BudgetPostPutSerializer(data=budget)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        budget_id = request.data.get('budget_id')
        if not budget_id:
            return Response({"error":"budget_id is required for update."},status=status.HTTP_400_BAD_REQUEST)
        
        budget = get_object_or_404(Budget,account_book_id = account_book,budget_id=budget_id)

        serializer = BudgetSerializer(budget, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 여러 지출 내역 추가, 수정 삭제
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def write_account_data_list(request): 
    account_book = get_object_or_404(Account_book, user_id=request.user) 
    if request.method == 'POST':
        with transaction.atomic():
            data = request.data
            if isinstance(data, list):
                response = []
                for item in data:
                    serializer = AccountBookDataSerializer(data={**item, 'account_book_id':account_book.pk})
                    if serializer.is_valid():
                        serializer.save()
                        response.append(serializer.data)
                    else:
                        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Invalid data format, expected a list of items."}, status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'DELETE':
        with transaction.atomic():
            data = request.data
            print(data)
            if isinstance(data,list) and all(isinstance(id, str) for id in data):
                try:
                    account_book_data = Account_book_data.objects.filter(
                        account_book_data_id__in=data,
                        account_book_id=account_book
                    )
                    cnt = account_book_data.count()
                    if cnt == 0:
                        return Response({"message": "No matching records found to delete."}, status=status.HTTP_404_NOT_FOUND)
                    
                    account_book_data.delete()
                    return Response({'message': f'Deleted {cnt} items.'}, status=status.HTTP_204_NO_CONTENT)
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Invalid data format, expected a list of integer IDs."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def write_account_data(request): # 단일 지출
    account_book = get_object_or_404(Account_book, user_id=request.user) 
    
    if request.method == 'POST':
        year = request.data.get('year')
        month = request.data.get('month')
        account = request.data.get('account')
        day = request.data.get('day')
        is_income = request.data.get('is_income')
        payment = request.data.get('payment')
        store = request.data.get('store')
        category_id = request.data.get('category_id')
        memo = request.data.get('memo')

        data = {
            "year" : int(year),
            "month" : int(month),
            "account" : int(account),
            "day" : int(day),
            "is_income" : is_income,
            "payment" : payment,
            "store" : store,
            "category_id" : int(category_id),
            "memo": memo
        }
        # print(data)

        serializer = AccountBookDataSerializer(data={**data, 'account_book_id':account_book.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # PUT 요청 - 단일 지출 수정
    elif request.method == 'PUT':
        # year = request.data.get('year')
        # month = request.data.get('month')
        # account = request.data.get('account')
        # day = request.data.get('day')
        # is_income = request.data.get('is_income')
        # payment = request.data.get('payment')
        # store = request.data.get('store')
        # category_id = request.data.get('category_id')

        # data = {
        #     "year" : int(year),
        #     "month" : int(month),
        #     "account" : int(account),
        #     "day" : int(day),
        #     "is_income" : is_income,
        #     "payment" : payment,
        #     "store" : store,
        #     "category_id" : int(category_id)
        # }
        account_book_data_id = request.data.get('account_book_data_id')
        if not account_book_data_id:
            return Response({"error": "account_book_data_id is required for update."}, status=status.HTTP_400_BAD_REQUEST)

        # 수정할 인스턴스 조회
        account_book_data_instance = get_object_or_404(Account_book_data, account_book_data_id=account_book_data_id, account_book_id=account_book)

        # 수정 데이터 적용
        serializer = AccountBookDataSerializer(account_book_data_instance, data=request.data, partial=True)  # 일부 필드만 수정 가능
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE 요청 - 단일 지출 삭제
    elif request.method == 'DELETE':
        account_book_data_id = request.data.get('account_book_data_id')
        if not account_book_data_id:
            return Response({"error": "account_book_data_id is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        # 삭제할 인스턴스 조회
        account_book_data_instance = get_object_or_404(Account_book_data, account_book_data_id=account_book_data_id, account_book_id=account_book)
        account_book_data_instance.delete()
        return Response({"message": f"Account book data with id {account_book_data_id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def receipt(request): # 영수증 OCR
    if request.method == 'POST':
        # 요청의 헤더를 확인
        # print(f"Request Headers: {request.headers}")
        
        # 파일을 가져와서 확인
        file = request.FILES.get('image')
        if not file:
            print("No file uploaded.")
            return Response({'error': 'No file uploaded'}, status=400)

        # 파일 정보 출력
        # print(f"File name: {file.name}")
        # print(f"File size: {file.size}")
        # print(f"File content type: {file.content_type}")
        
        # FileSystemStorage를 사용하여 media 폴더에 파일 저장
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)

        headers = {
            'X-OCR-SECRET': settings.NAVER_OCR_API_KEY,
        }        
        message = {
            'version':'V2',
            'requestId':str(uuid.uuid4()),
            'timestamp':int(time.time()*1000),
            'images':[
                {
                    'format':file.name.split('.')[-1],
                    'name':'sample_image'
                }
            ]
        }

        try:
            # 요청 데이터 만들기
            with open(file_path, 'rb') as img_file:
                files = {
                    'message': (None, json.dumps(message), 'application/json'),
                    'file': (filename, img_file, file.content_type)
                }
                # 네이버 OCR API 요청
                response = requests.post(settings.NAVER_OCR_URL, headers=headers, files=files)
                response_data = response.json()  # JSON 응답 파싱

                # 응답 데이터를 JSON 파일로 저장
                json_filename = f"ocr_response_{uuid.uuid4().hex}.json"
                json_file_path = os.path.join(settings.MEDIA_ROOT, json_filename)
                with open(json_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(response_data, json_file, ensure_ascii=False, indent=4)

            # API 요청 성공 시 응답 반환
            if response.status_code == 200:
                if os.path.exists(file_path):
                    os.remove(file_path)
                
                try:
                    store =response_data['images'][0]['receipt']['result']['storeInfo']['name']['text']
                except:
                    store = ''
                
                try:
                    year =response_data['images'][0]['receipt']['result']['paymentInfo']['date']['formatted']['year']
                except:
                    year =0

                try:
                    month =response_data['images'][0]['receipt']['result']['paymentInfo']['date']['formatted']['month']
                except:
                    month = 0

                try:
                    day =response_data['images'][0]['receipt']['result']['paymentInfo']['date']['formatted']['day']
                except:
                    day = 0

                try:
                    account =response_data['images'][0]['receipt']['result']['totalPrice']['price']['formatted']['value']
                except:
                    account = 0

                try:
                    subResults =response_data['images'][0]['receipt']['result']['subResults'][0]['items']
                    memo=''
                    for item in subResults:
                        menu= item['name']['formatted']['value']
                        print(menu)
                        cnt = item['count']['formatted']['value']
                        print(cnt)
                        price = item['price']['price']['formatted']['value']
                        print(price)
                        unitPrice = item['price']['unitPrice']['formatted']['value']
                        print(unitPrice)
                        memo +=f'{menu}({cnt}개):{price}원 개당 {unitPrice}, '
                        print(memo)
                except:
                    memo=''

                data ={
                    "store":store,
                    "year":year,
                    "month":month,
                    "day":day,
                    "account":account,
                    "is_income":False,
                    "payment":'카드', 
                    "category_id":1, #이건 AI 써야함
                    "memo":memo

                }

                return Response({'message': 'File uploaded and OCR processed successfully', 'data': data}, status=200)
            else:
                # 에러 응답 시
                return Response({'error': 'Failed to process OCR', 'details': response_data}, status=response.status_code)

        except Exception as e:
            return Response({'error': 'Internal server error', 'details': str(e)}, status=500)
    return Response({'error': 'Invalid request method'}, status.HTTP_405_METHOD_NOT_ALLOWED )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calender_data(request): 
    account_book = get_object_or_404(Account_book, user_id=request.user)

    if request.method == 'GET':
        # 요청 파라미터 유효성 검사
        try:
            year = int(request.query_params.get('year'))
            month = int(request.query_params.get('month'))

            if not (1 <= month <= 12):
                return Response({'error': 'Month must be between 1 and 12.'}, status=status.HTTP_400_BAD_REQUEST)

        except (ValueError, TypeError):
            return Response({'error': 'Invalid year or month parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        # 한달 데이터 모으기
        month_data = Account_book_data.objects.filter(
            year=year,
            month=month,
            account_book_id=account_book.pk
        )

        # 한 달 전체 수익 및 지출 합산
        total_income = month_data.filter(is_income=True).aggregate(total=Sum('account'))['total'] or 0
        total_expenditure = month_data.filter(is_income=False).aggregate(total=Sum('account'))['total'] or 0

        # 날짜별 그룹화 후 수익 및 지출 합산
        day_data = []
        grouped_data = month_data.values('day').annotate(
            income=Sum('account', filter=Q(is_income=True)),
            expenditure=Sum('account', filter=Q(is_income=False))
        )

        for day_entry in grouped_data:
            day_data.append({
                'day': day_entry['day'],
                'income': day_entry['income'] or 0,
                'expenditure': day_entry['expenditure'] or 0,
            })

        # 오름차순 정렬 추가
        day_data = sorted(day_data, key=lambda x: x['day'])

        # 시리얼라이저 사용하여 데이터 응답
        monthly_data = {
            'total_income': total_income,
            'total_expenditure': total_expenditure,
            'day_data': day_data
        }

        serializer = MonthlyDataSerializer(monthly_data)
        return Response(serializer.data)

    return Response({'error': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analyze_category(request):
    account_book = get_object_or_404(Account_book, user_id=request.user)

    if request.method == 'GET':
        if request.method == 'GET':
            # 요청 파라미터 유효성 검사
            try:
                year = int(request.query_params.get('year'))
                month = int(request.query_params.get('month'))

                if not (1 <= month <= 12):
                    return Response({'error': 'Month must be between 1 and 12.'}, status=status.HTTP_400_BAD_REQUEST)

            except (ValueError, TypeError):
                return Response({'error': 'Invalid year or month parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        # 한달 데이터 모으기
        month_data = Account_book_data.objects.filter(
            year=year,
            month=month,
            account_book_id=account_book.pk,
            is_income = False
        )

        # 카테고리 id 별로 account 합쳐야함
        # 카테고리별 소비 금액 합계 계산
        category_expenses = month_data.values('category_id').annotate(total_amount=Sum('account'))

        category_summary = []
        for category in category_expenses:
            category_id = category['category_id']
            total_amount = category['total_amount']

            details = month_data.filter(category_id=category_id).values(
                'day', 'account', 'payment', 'store', 'memo'
            )

            # 요약 및 세부 내역 추가
            category_summary.append({
                'category_id': category_id,
                'total_amount': total_amount,
                'details': list(details)
            })
        serializer =CategoryExpenseSerializer(category_summary, many=True)

        return Response(serializer.data)
    return Response({'error': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analyze_time(request):
    account_book = get_object_or_404(Account_book, user_id=request.user)

    if request.method == 'GET':
        # 요청 파라미터 유효성 검사
        try:
            year = int(request.query_params.get('year'))
            month = int(request.query_params.get('month'))

            if not (1 <= month <= 12):
                return Response({'error': 'Month must be between 1 and 12.'}, status=status.HTTP_400_BAD_REQUEST)

        except (ValueError, TypeError):
            return Response({'error': 'Invalid year or month parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        month_age_1 = month-1
        month_age_2 = month-2

        # 1개월 전과 2개월 전의 month와 year 계산
        if month == 1:
            month_age_1 = 12
            year_age_1 = year - 1
            month_age_2 = 11
            year_age_2 = year - 1
        elif month == 2:
            month_age_1 = 1
            year_age_1 = year
            month_age_2 = 12
            year_age_2 = year - 1
        else:
            month_age_1 = month - 1
            year_age_1 = year
            month_age_2 = month - 2
            year_age_2 = year

        # 한달 데이터 모으기
        month_data = Account_book_data.objects.filter(
            year=year,
            month=month,
            is_income=False,
            account_book_id=account_book.pk,
        )

        # 11월 고정 지출 결제 내역
        schedules = month_data.filter(is_schedule=True)

        schedules = schedules.order_by('day')

        total_schedules= schedules.aggregate(total=Sum('account'))['total'] or 0

        # 1달 전 지출 
        total_expenditure_age_1 = Account_book_data.objects.filter(
            year=year_age_1,
            month=month_age_1,
            is_income=False,
            account_book_id=account_book.pk
        ).aggregate(total=Sum('account'))['total'] or 0

        # 2달전 지출
        total_expenditure_age_2 = Account_book_data.objects.filter(
            year=year_age_2,
            month=month_age_2,
            is_income=False,
            account_book_id=account_book.pk
        ).aggregate(total=Sum('account'))['total'] or 0

        # 현재 달 지출
        total_expenditure= month_data.filter(is_income=False).aggregate(total=Sum('account'))['total'] or 0
        
        # 현재달 하루 총 지출
        day_data = []
        grouped_data = month_data.values('day').annotate(
            expenditure=Sum('account', filter=Q(is_income=False))
        )

        for day_entry in grouped_data:
            day_data.append({
                'day': day_entry['day'],
                'expenditure': day_entry['expenditure'] or 0,
            })

        # 오름차순 정렬 추가
        day_data = sorted(day_data, key=lambda x: x['day'])



        # 주별 지출은 어떻게 구해야 할까?
        
        week_data = defaultdict(int)

        for day_entry in grouped_data:
            day = day_entry['day']
            expenditure = day_entry['expenditure'] or 0

            week_number = math.ceil(day/7) 

            # 주별 지출 합산
            week_data[week_number]  += expenditure

        # 주별 지출 리스트로 변환 및 정렬
        weekly_data = [{'week': week,'expenditure':expenditure} for week, expenditure in week_data.items()]
        weekly_data = sorted(weekly_data,key=lambda x: x['week'])

        # 응답 데이터 생성
        analysis_data = {
            'total_expenditure': total_expenditure,
            'total_expenditure_age_1': total_expenditure_age_1,
            'total_expenditure_age_2': total_expenditure_age_2,
            'total_schedules':total_schedules,
            'day_data': day_data,
            'weekly_data': weekly_data,
            'schedules':schedules,
        }

        # 시리얼라이저를 사용하여 응답 반환
        serializer = AnalysisTimeSerialzer(analysis_data)
        return Response(serializer.data)
    return Response({'error': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)