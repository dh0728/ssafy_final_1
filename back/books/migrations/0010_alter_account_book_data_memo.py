# Generated by Django 4.2.16 on 2024-11-22 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_account_book_data_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_book_data',
            name='memo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]