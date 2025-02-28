# Generated by Django 4.2.16 on 2024-11-19 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.IntegerField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Check_cards",
            fields=[
                (
                    "check_card_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("check_card_name", models.CharField(max_length=255)),
                ("domestic_fee", models.IntegerField(default=0)),
                ("abroad_fee", models.IntegerField(default=0)),
                ("pre_month_perform", models.CharField(default="없음", max_length=255)),
                ("bank_url", models.URLField()),
                ("img_path", models.URLField()),
                ("brand", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Credit_cards",
            fields=[
                (
                    "credit_card_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("credit_card_name", models.CharField(max_length=255)),
                ("domestic_fee", models.IntegerField(default=0)),
                ("abroad_fee", models.IntegerField(default=0)),
                ("pre_month_perform", models.CharField(default="없음", max_length=255)),
                ("bank_url", models.URLField()),
                ("img_path", models.URLField()),
                ("brand", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Credit_card_category",
            fields=[
                (
                    "credit_card_category_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=50)),
                ("desc", models.CharField(max_length=100)),
                ("desc_detail", models.TextField(default="상세 없음")),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.category"
                    ),
                ),
                (
                    "credit_card_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.credit_cards",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Check_card_category",
            fields=[
                (
                    "check_card_category_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=50)),
                ("desc", models.CharField(max_length=100)),
                ("desc_detail", models.TextField(default="상세 없음")),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cards.category"
                    ),
                ),
                (
                    "check_card_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cards.check_cards",
                    ),
                ),
            ],
        ),
    ]
