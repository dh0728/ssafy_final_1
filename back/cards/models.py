from django.db import models

# Create your models here.
class Credit_cards(models.Model):
    credit_card_id = models.IntegerField(primary_key=True)
    credit_card_name = models.CharField(max_length=255)
    domestic_fee = models.IntegerField(default=0)
    abroad_fee = models.IntegerField(default=0)
    pre_month_perform = models.CharField(max_length=255,default='없음')
    bank_url = models.URLField(max_length=200)
    img_path = models.URLField(max_length=200)
    brand = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

class Check_cards(models.Model):
    check_card_id = models.IntegerField(primary_key=True)
    check_card_name = models.CharField(max_length=255)
    domestic_fee = models.IntegerField(default=0)
    abroad_fee = models.IntegerField(default=0)
    pre_month_perform = models.CharField(max_length=255,default='없음')
    bank_url = models.URLField(max_length=200)
    img_path = models.URLField(max_length=200)
    brand = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

class Category(models.Model):
    category_id =models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=25)

class Credit_card_category(models.Model):
    credit_card_category_id= models.IntegerField(primary_key=True)
    credit_card_id=models.ForeignKey(Credit_cards, on_delete=models.CASCADE)
    category_id= models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    desc_detail= models.TextField(default='상세 없음')

class Check_card_category(models.Model):
    check_card_category_id= models.IntegerField(primary_key=True)
    check_card_id=models.ForeignKey(Check_cards, on_delete=models.CASCADE)
    category_id= models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    desc_detail= models.TextField(default='상세 없음')


