# Generated by Django 3.2.9 on 2021-12-09 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productmanagement', '0017_products_category'),
        ('cart', '0013_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='buy_now',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('buy_now', models.BooleanField(default=True)),
                ('products_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanagement.products')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
