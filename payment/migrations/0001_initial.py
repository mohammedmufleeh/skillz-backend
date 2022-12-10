# Generated by Django 4.1.2 on 2022-11-10 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEntrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.CharField(blank=True, max_length=25)),
                ('order_payment_id', models.CharField(blank=True, max_length=100)),
                ('entrolled_time', models.DateField(auto_now_add=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrolled_courses', to='teacher_app.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrolled_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
