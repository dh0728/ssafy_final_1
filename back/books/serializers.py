from rest_framework import serializers
from .models import Account_book, Account_book_data, Budget, Schedule

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        exclude = ('created_at', 'updated_at')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        exclude = ('created_at', 'updated_at')

## 한달 가계부 정보 전부 조회
class AccountBookCalendar(serializers.ModelSerializer):
    class Meta:
        model = Account_book_data
        exclude = ('created_at', 'updated_at')


class AccountBookDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_book_data
        fields = '__all__'

class BudgetPostPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class AccountBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_book
        fields = '__all__'


class DayDataSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    income = serializers.IntegerField()
    expenditure = serializers.IntegerField()

class MonthlyDataSerializer(serializers.Serializer):
    total_income = serializers.IntegerField()
    total_expenditure = serializers.IntegerField()
    day_data = DayDataSerializer(many=True)