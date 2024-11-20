from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404 , get_list_or_404
from rest_framework.response import Response
from .models import Account_book, Account_book_data, Budget, Schedule

from .serializers import AccountBookCalendar, AccountBookDataSerializer,BudgetPostPutSerializer, BudgetSerializer, ScheduleSerializer
from django.db import transaction


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_calendar(request):  # 캘린더 페이지
    # 사용자의 가계부 인스턴스가 있는지 확인하고 없으면 생성
    account_book, created = Account_book.objects.get_or_create(user_id=request.user)

    if created:
        return Response({"message": "Account book was created for the user."}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Account book already exists."}, status=status.HTTP_200_OK)


# 하루치 결제 데이터 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def day(request):
    account_book, created = Account_book.objects.get_or_create(user_id=request.user)
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
    account_book, created = Account_book.objects.get_or_create(user_id=request.user)
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
    account_book, created = Account_book.objects.get_or_create(user_id=request.user) 

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
    account_book, created = Account_book.objects.get_or_create(user_id=request.user)

    if request.method == 'GET':
        year = request.query_params.get('year')
        month = request.query_params.get('month')
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
    account_book, created = Account_book.objects.get_or_create(user_id=request.user)
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
                return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    account_book, created = Account_book.objects.get_or_create(user_id=request.user)
    
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
        pass
