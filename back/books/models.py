from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class Account_book(models.Model):
    account_book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account_books')
    created_at = models.DateTimeField(auto_now_add=True)

class Account_book_data(models.Model):
    account_book_data_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_book_id = models.ForeignKey(Account_book, on_delete=models.CASCADE)
    category_id = models.ForeignKey('cards.Category',on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    account = models.IntegerField()
    is_income = models.BooleanField()
    payment = models.CharField(max_length=10)
    store = models.CharField(max_length=50)
    memo = models.CharField(max_length=255, null=True,blank=True)
    is_schedule = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Budget(models.Model):
    budget_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_book_id = models.ForeignKey(Account_book, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Schedule(models.Model):
    schedule_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_book_id = models.ForeignKey(Account_book, on_delete=models.CASCADE)
    category_id =models.ForeignKey('cards.Category',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    day= models.IntegerField()
    is_income = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






