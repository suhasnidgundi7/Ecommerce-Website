# Generated by Django 3.2 on 2021-05-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(default='', max_length=300),
        ),
    ]
