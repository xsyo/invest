# Generated by Django 3.1.6 on 2021-02-13 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='coefficient',
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('old_balance', models.DecimalField(decimal_places=2, max_digits=13)),
                ('coefficient', models.DecimalField(decimal_places=5, max_digits=6)),
                ('new_balance', models.DecimalField(decimal_places=2, max_digits=13)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journal', to='packages.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
