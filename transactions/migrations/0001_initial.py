# Generated by Django 3.1.6 on 2021-02-14 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('R', 'Refill'), ('W', 'Withdrawal')], max_length=2)),
                ('status', models.CharField(choices=[('S', 'Success'), ('P', 'Pending'), ('F', 'Failed')], default='P', max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('cart', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]