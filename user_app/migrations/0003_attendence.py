# Generated by Django 4.0.1 on 2022-04-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_delete_attendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_user_id', models.CharField(max_length=255, null=True)),
                ('Student_department', models.CharField(max_length=5, null=True)),
                ('section', models.CharField(max_length=1, null=True)),
                ('period', models.IntegerField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
