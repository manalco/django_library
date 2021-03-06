# Generated by Django 3.0.3 on 2020-02-16 21:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_starts', models.DateField(default=datetime.date.today)),
                ('loan_ends', models.DateField(default=datetime.date.today)),
                ('return_date', models.DateField(blank=True, editable=False, null=True)),
                ('status', models.BooleanField(default=True, help_text="If the loan is active, the book is in the student's custody.", verbose_name='Loan is active')),
                ('notes', models.TextField(blank=True, max_length=4000, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='books.Book')),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'Student'}, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='subjects.Subject')),
            ],
        ),
    ]
