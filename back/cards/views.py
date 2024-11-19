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

credit_companies={
    '1': 'Sh수협은행',
    '2': '토스뱅크',
    '3': 'NH농협카드',
    '4': '우리카드',
    '5': 'BNK경남은행',
    '6': '현대카드',
    '7': 'Sc제일은행',
    '8': '롯데카드',
    '9': '전북은행',
    '10': '케이뱅크',
    '11': 'BC 바로카드',
    '12': '신한카드',
    '13': 'BNK부산은행',
    '14': '차이',
    '15': 'KB국민은행',
    '16': 'SSGPAY.CARD',
    '17': 'IBK기업은행',
    '18': '삼성카드',
    '19': '씨티카드',
    '20': 'DGB대구은행',
    '21': '하나카드',
    '22': '제주은행',
    '23': '현대백화점',
    '24': '광주은행',
    '25': '신협'
}

check_companies={
    '1': '케이뱅크',
    '2': 'KB국민카드',
    '3': '신한카드',
    '4': '하나카드',
    '5': '네이버페이',
    '6': '토스뱅크',
    '7': 'KG모빌리언스',
    '8': '우리카드',
    '9': '엔에이치엔페이코',
    '10': '카카오뱅크',
    '11': 'NH농협카드',
    '12': 'MG새마을금고',
    '13': '우체국',
    '14': '삼성카드',
    '15': '현대카드',
    '16': 'IBK기업은행',
    '17': 'KB증권',
    '18': '코나카드',
    '19': '롯데카드',
    '20': '트래블월렛',
    '21': '제주은행',
    '22': '미래에셋증권',
    '23': '한패스',
    '24': 'NH투자증권',
    '25': 'KDB산업은행',
    '26': 'DB금융투자',
    '27': 'BC 바로카드',
    '28': '전북은행',
    '29': '카카오페이',
    '30': '한국투자증권',
    '31': 'SBI저축은행',
    '32': 'SK증권',
    '33': 'DGB대구은행',
    '34': '토스',
    '35': 'BNK부산은행',
    '36': '신협',
    '37': '다날',
    '38': '유진투자증권',
    '39': 'Sh수협은행',
    '40': '유안타증권',
    '41': '광주은행',
    '42': '핀크카드',
    '43': '아이오로라',
    '44': '머니트리',
    '45': '핀트',
    '46': '교보증권',
    '47': 'SC제일은행',
    '48': '차이'
}

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
        
        categories_str = request.query_params.getlist('categories')
        companies= request.query_params.getlist('companies')
        categories=list(map(int,categories_str))

        print('companies',companies)
        print('categories',categories_str)

        if card_type == '1':
            brands=[]
            for company in companies:
                brands.append(credit_companies[company])

            # card_model = Credit_cards
            card_category_model = Credit_card_category
            card_category_field = 'credit_card_id'
        else:
            brands=[]
            for category in categories_str:
                brands.append(check_companies[category])
            # card_model = Check_cards
            card_category_model = Check_card_category
            card_category_field = 'check_card_id'
        
        print(brands)
        print(categories)
        if categories:
            sql_query = f"""
                SELECT {card_category_field}_id
                FROM {card_category_model._meta.db_table}
                WHERE category_id_id IN ({','.join([str(category) for category in categories])})
                GROUP BY {card_category_field}_id
                HAVING COUNT(DISTINCT category_id_id) = {len(categories)}
            """
    
            # raw SQL 쿼리 실행 및 카드 ID 추출
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql_query)
                    card_ids = [row[0] for row in cursor.fetchall()]
            except Exception as e:
                return Response({"error": f"데이터베이스 오류가 발생했습니다: {str(e)}"}, status=500)
            print(card_ids)

        # # 카드 ID와 brand를 이용하여 최종카드 정보 조회
        # if card_type == '1':
        #     cards = Credit_cards.objects.filter(
        #         credit_card_id__in=card_ids,
        #         brand__in=brands
        #     ).distinct()
        #     serializer = CreditCardListSerializer(cards, many=True)
        # else:
        #     cards = Check_cards.objects.filter(
        #         card_category_field__in=card_ids,
        #         brand__in=brands
        #     ).distinct()
        #     serializer = CheckCardListSerializer(cards, many=True)

        if card_type == '1':
            # 필터 조건에 따른 카드 쿼리셋 조회
            cards = Credit_cards.objects.all()
            if brands:
                cards = cards.filter(brand__in=brands)
            if categories:
                cards = cards.filter(
                    credit_card_id__in=card_ids,
                ).distinct()
                
            serializer = CreditCardListSerializer(cards.distinct(), many=True)

        else:
            # 필터 조건에 따른 체크카드 쿼리셋 조회
            cards = Check_cards.objects.all()
            if brands:
                cards = cards.filter(brand__in=brands)
            if categories:
                cards = cards.filter(
                    check_card_id__in=card_ids,
                ).distinct()
    
            serializer = CheckCardListSerializer(cards.distinct(), many=True)


        if not cards.exists():
            return Response({"message": "조건에 맞는 카드를 찾을 수 없습니다.", "data": []}, status=200)
        
        return Response(serializer.data)

def recommend(request):
    pass