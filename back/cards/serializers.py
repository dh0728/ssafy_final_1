from rest_framework import serializers
from .models import Credit_cards, Check_cards, Check_card_category, Credit_card_category, MyCheckCard,MyCreditCard


## 신용카드 목록 조회
class CreditCardListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit_card_category
        fields = ('title','desc',)

class CreditCardListSerializer(serializers.ModelSerializer):
    benefits = CreditCardListCategorySerializer(source='credit_card_category_set', many=True)
    class Meta:
        model = Credit_cards
        fields = '__all__'

## 체크 목록 조회
class CheckCardListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_card_category
        fields = ('title','desc',)

class CheckCardListSerializer(serializers.ModelSerializer):
    benefits = CheckCardListCategorySerializer(source='check_card_category_set', many=True)
    class Meta:
        model = Check_cards
        fields = '__all__'


## CreditCard 상세조회
class CreditCardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit_card_category
        fields = ('title','desc','desc_detail')

class CreditCardSerializer(serializers.ModelSerializer):
    benefits = CreditCardCategorySerializer(source='credit_card_category_set', many=True)
    class Meta:
        model = Credit_cards
        fields = '__all__'



## CheckCard 상세조회
class CheckCardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_card_category
        fields = ('title','desc','desc_detail')

class CheckCardSerializer(serializers.ModelSerializer):
    benefits = CheckCardCategorySerializer(source='check_card_category_set', many=True)
    class Meta:
        model = Check_cards
        fields = '__all__'

class MyCreditCardSerializer(serializers.ModelSerializer):
    credit_card_name = serializers.CharField(source='credit_card_id.credit_card_name', read_only=True)  # Credit_cards 모델의 name 필드 가정
    img_path = serializers.URLField(source='credit_card_id.img_path', read_only=True)
    brand =serializers.CharField(source='credit_card_id.brand', read_only=True)
    card_type = serializers.IntegerField(default=1,read_only=True)
    class Meta:
        model = MyCreditCard
        fields = ['credit_card_id', 'credit_card_name','img_path','brand','card_type']

# 체크카드 Serializer
class MyCheckCardSerializer(serializers.ModelSerializer):
    check_card_name = serializers.CharField(source='check_card_id.check_card_name', read_only=True)  # Check_cards 모델의 name 필드 가정
    img_path = serializers.URLField(source='check_card_id.img_path', read_only=True)
    brand =serializers.CharField(source='check_card_id.brand', read_only=True)
    card_type = serializers.IntegerField(default=2,read_only=True)
    class Meta: 
        model = MyCheckCard
        fields = ['check_card_id', 'check_card_name', 'img_path', 'brand', 'card_type']

class RecommendCreditCard(serializers.ModelSerializer):
    card_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Credit_cards
        fields = ('credit_card_id', 'credit_card_name', 'img_path', 'brand', 'card_type')
    
    def get_card_type(self, obj):
        return 1

class RecommendCheckCard(serializers.ModelSerializer):
    card_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Check_cards
        fields = ('check_card_id', 'check_card_name', 'img_path', 'brand', 'card_type')
    
    def get_card_type(self, obj):
        return 2