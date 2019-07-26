# Generated by Django 2.2.3 on 2019-07-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190715_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('mobile', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=50)),
            ],
        ),
    ]