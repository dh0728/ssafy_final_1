from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404 , get_list_or_404
from rest_framework.response import Response
from .models import Account_book, Account_book_data, Budget, Schedule

from .serializers import AccountBookCalendar, AccountBookDataSerializer,BudgetPostPutSerializer



# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_calendar(request): #켈린더 페이지
    if request.method == 'GET':
        month = request.query_params.get('month')

        # 사용자가 본인 가계부 인스턴스가 있나 확인
        try:
            account_book =get_object_or_404(Account_book, user_id=request.user) 
        except: # 오류나면 가계부 인스턴스 하나 만들기
            account_book = Account_book.objects.create(user_id=request.user)

        # 현재 month의 예산 정보가 있는지 확인
        try:
            budget = Budget.objects.get(
                account_book_id = account_book,
                month = int(month)
            )
        except:
            budget = Budget.objects.create(
                account_book_id = account_book,
                month = int(month),
                value=0,
            )
        
        account_book_data = Account_book_data.objects.filter(
            account_book_id = account_book,
            month = int(month)
        )
        if not account_book_data.exists():
            print('이번달에 결제한 내역이 없습니다.')
        
        schedules = Schedule.objects.filter(
            account_book_id = account_book
        )

        if not schedules.exists():
            print('수입,지출 스케줄이 없습니다.')

        serializer= AccountBookCalendar(account_book_data, many=True)
        return Response(serializer.data)

@api_view(['POST','PUT'])
@permission_classes([IsAuthenticated])
def budget(request):
    if request.method == 'POST':
        try:
            account_book =get_object_or_404(Account_book, user_id=request.user) 
        except: # 오류나면 가계부 인스턴스 하나 만들기
            account_book = Account_book.objects.create(user_id=request.user)
        
        print(account_book.pk)
        month = request.data.get('month')
        value = request.data.get('value')

        budget = {
            'account_book_id': account_book.pk,
            'month': int(month),
            'value': int(value),
        }
        serializer =BudgetPostPutSerializer(data=budget)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        pass


@api_view(['POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def write_account_data(request): # 지출 내역 추가, 수정 삭제
    if request.method == 'POST':
        try:
            account_book =get_object_or_404(Account_book, user_id=request.user) 
        except: # 오류나면 가계부 인스턴스 하나 만들기
            account_book = Account_book.objects.create(user_id=request.user)
        
        category_id =request.data.get('category_id')
        year = request.data.get('year')
        month = request.data.get('month')
        day = request.data.get('day')
        account = request.data.get('account')
        is_income = request.data.get('is_income')
        payment = request.data.get('payment')
        store = request.data.get('store')

        account_book_data = {
            'account_book_id': account_book.pk,
            'category_id': category_id,
            'year': int(year),
            'month': int(month),
            'day': int(day),
            'account': int(account),
            'is_income': is_income,
            'payment': payment,
            'store': store
        }

        serializer = AccountBookDataSerializer(data=account_book_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def receipt(request): # 영수증 OCR
    if request.method == 'POST':
        pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_history(request): # 내역 페이지
    if request.method == 'POST':
        pass