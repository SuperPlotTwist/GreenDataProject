# Generated by Django 3.2 on 2021-04-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_product_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='others', max_length=255),
        ),
    ]
