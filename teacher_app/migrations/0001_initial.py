# Generated by Django 4.1.2 on 2022-11-10 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': '2. Course Category',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=20)),
                ('skills', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '1. Teachers',
            },
        ),
        migrations.CreateModel(
            name='TeacherToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_image', models.ImageField(blank=True, upload_to='photos/course_image/')),
                ('title', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('used_techs', models.CharField(blank=True, max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_app.coursecategory')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_app.teacher')),
            ],
            options={
                'verbose_name_plural': '3. Course',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('video', models.FileField(blank=True, upload_to='videos/chapter_videos/')),
                ('remark', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_chapters', to='teacher_app.course')),
            ],
            options={
                'verbose_name_plural': '4. Chapters',
            },
        ),
    ]
