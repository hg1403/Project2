# Generated by Django 3.2.9 on 2021-12-02 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0008_auto_20211202_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_offer_price',
            new_name='old_sale_price',
        ),
    ]
