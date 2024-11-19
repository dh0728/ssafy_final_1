from .models import Credit_cards, Check_cards, Credit_card_category,Check_card_category
from rest_framework.permissions import AllowAny
from .serializers import CreditCardSerializer, CheckCardSerializer, CreditCardListSerializer, CheckCardListSerializer
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework import status
from django.shortcuts import get_object_or_404 , get_list_or_404
from rest_framework.response import Response

from django.db.models import Count
from django.db import connection

# Create your views here.
@api_view(['GET'])
@authentication_classes([])  # 인증 클래스 비활성화
@permission_classes([AllowAny])
def search(request,card_type,card_pk):
    '''
    카드목록 페이지 한요청당 카드 20개씩 전달 
    '''
    if request.method == 'GET':
        cnt= 20
        start_pk = int(card_pk)  

        if card_type=='1':
            cards = Credit_cards.objects.filter(pk__gte=start_pk)[:cnt]
            serializer = CreditCardListSerializer(cards,many=True)
        else:
            cards = Check_cards.objects.filter(pk__gt=start_pk)[:cnt]
            serializer = CheckCardListSerializer(cards,many=True)
        return Response(serializer.data)
        
    
@api_view(['GET'])
@authentication_classes([])  # 인증 클래스 비활성화
@permission_classes([AllowAny])
def detail(request,card_type,card_pk):
    '''
    카드 상세조회 함수 
    '''
    if request.method == 'GET':
        if card_type=='1':
            card = get_object_or_404(Credit_cards,pk=card_pk)
            serializer = CreditCardSerializer(card)
        else:
            card =get_object_or_404(Check_cards,pk=card_pk)
            serializer = CheckCardSerializer(card)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])  # 인증 클래스 비활성화
@permission_classes([AllowAny])
def searchCondition(request,card_type):
    '''
    brand: 은행사, 여러은행 올 수 있음
    cartegory: 카테고리 종류도 여러 개 올 수 있음 card_category테이블에서 역추적해서 카드들 찾아야함
    '''
    if request.method == 'GET':
        # 요청에서 brand와 category 추출
        brands = request.query_params.getlist('brand') 
        categories_str = request.query_params.getlist('category')
        categories=list(map(int,categories_str))

        print(brands)
        print(categories)
        if card_type == '1':
            card_model = Credit_cards
            card_category_model = Credit_card_category
            card_category_field = 'credit_card_id'
        else:
            card_model = Check_cards
            card_category_model = Check_card_category
            card_category_field = 'check_card_id'
        
        sql_query = f"""
            SELECT {card_category_field}_id
            FROM {card_category_model._meta.db_table}
            WHERE category_id_id IN ({','.join([str(category) for category in categories])})
            GROUP BY {card_category_field}_id
            HAVING COUNT(DISTINCT category_id_id) = {len(categories)}
        """

        # raw SQL 쿼리 실행 및 카드 ID 추출
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            card_ids = [row[0] for row in cursor.fetchall()]
        
        print(card_ids)
        # 카드 ID와 brand를 이용하여 최종카드 정보 조회
        cards = card_model.objects.filter(
            credit_card_id__in=card_ids,
            brand__in=brands
        ).distinct()

        if card_type == '1':
            serializer = CreditCardListSerializer(cards, many=True)
        else:
            serializer = CheckCardListSerializer(cards, many=True)

        return Response(serializer.data)

def recommend(request):
    pass