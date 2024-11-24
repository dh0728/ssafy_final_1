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


class TimeDayDataSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    expenditure = serializers.IntegerField()

class TimeWeekDateSerializer(serializers.Serializer):
    week = serializers.IntegerField()
    expenditure = serializers.IntegerField()

class TimeScheduleSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    store = serializers.CharField()
    account = serializers.IntegerField()

class AnalysisTimeSerialzer(serializers.Serializer):
    total_expenditure = serializers.IntegerField()
    total_expenditure_age_1 = serializers.IntegerField()
    total_expenditure_age_2 = serializers.IntegerField()
    total_schedules = serializers.IntegerField()
    day_data = TimeDayDataSerializer(many=True)
    weekly_data = TimeWeekDateSerializer(many=True)    
    schedules = TimeScheduleSerializer(many=True)
    


class CategoryExpenseDetailSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    account = serializers.IntegerField()
    payment = serializers.CharField(max_length=100)
    store = serializers.CharField(max_length=100)
    memo = serializers.CharField(max_length=255)
    

class CategoryExpenseSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    details = CategoryExpenseDetailSerializer(many=True)

class EvaluationSerializer(serializers.Serializer):
    comment = serializers.CharField()