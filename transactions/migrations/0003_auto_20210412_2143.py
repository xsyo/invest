# Generated by Django 3.1.7 on 2021-04-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20210411_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='cart',
            field=models.CharField(max_length=17),
        ),
    ]
