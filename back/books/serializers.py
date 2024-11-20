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