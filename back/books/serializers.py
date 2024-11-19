from rest_framework import serializers
from .models import Account_book, Account_book_data, Budget, Schedule

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('month','value')

class ScheduleSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Schedule
        fields = ('name','value','category_id')

## 한달 가계부 정보 전부 조회
class AccountBookCalendar(serializers.ModelSerializer):
    budget = BudgetSerializer(read_only=True)
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Account_book_data
        fields = ('category_id','year','month','account','is_income','payment','store',)



class AccountBookDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_book_data
        fields = '__all__'

class BudgetPostPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'