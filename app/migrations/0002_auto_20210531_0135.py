# Generated by Django 3.2.3 on 2021-05-31 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='abc@def.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default=9846731777, max_length=200),
            preserve_default=False,
        ),
    ]
