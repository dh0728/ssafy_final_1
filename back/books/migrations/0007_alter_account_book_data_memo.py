# Generated by Django 4.2.16 on 2024-11-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_account_book_data_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_book_data',
            name='memo',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
