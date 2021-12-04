# Generated by Django 3.2.6 on 2021-10-27 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(help_text='Enter the name of the course.', max_length=200)),
                ('course_id', models.CharField(blank=True, default='', help_text='Enter the course id code if applicable.', max_length=200)),
            ],
            options={
                'ordering': ['course_name'],
            },
        ),
        migrations.CreateModel(
            name='CourseProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(help_text='Enter the course provider name.', max_length=200)),
                ('provider_website', models.CharField(blank=True, default='', help_text='Enter the course providers website.', max_length=255)),
                ('lms', models.CharField(blank=True, default='', help_text='Enter the learning management systems web address', max_length=610)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Student first name.', max_length=50)),
                ('last_name', models.CharField(help_text='Student last name.', max_length=50)),
                ('id_number', models.CharField(help_text='Student ID number', max_length=10)),
                ('active', models.BooleanField(default=True, help_text='Uncheck box for inactive students')),
                ('course', models.ManyToManyField(blank=True, default='', help_text='Select courses student is enrolled in.', to='check_in.Course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('attended_meeting', models.BooleanField()),
                ('missing_work_amount', models.IntegerField(default=0)),
                ('narrative', models.TextField(blank=True, default='')),
                ('instructor', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(help_text='Student Name.', null=True, on_delete=django.db.models.deletion.CASCADE, to='check_in.student')),
            ],
        ),
        migrations.CreateModel(
            name='CourseEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course', models.ForeignKey(blank=True, default='', help_text='Select course student is enrolled in.', on_delete=django.db.models.deletion.PROTECT, to='check_in.course')),
                ('student', models.ForeignKey(help_text='Student Name.', null=True, on_delete=django.db.models.deletion.CASCADE, to='check_in.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_provider',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='check_in.courseprovider'),
        ),
    ]
