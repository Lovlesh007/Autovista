# Generated by Django 2.0.1 on 2020-05-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Crud', '0002_delete_leads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=12)),
                ('Email_address', models.EmailField(max_length=30)),
                ('Interested_in', models.CharField(choices=[('Buy New Car', 'Buy New Car'), ('Buy Second hand Car', 'Buy Second hand Car'), ('Sell Second hand Car', 'Sell Second hand Car'), ('Others', 'Others')], max_length=50)),
            ],
        ),
    ]
