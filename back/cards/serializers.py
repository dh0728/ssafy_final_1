from rest_framework import serializers
from .models import Credit_cards, Check_cards, Check_card_category, Credit_card_category


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