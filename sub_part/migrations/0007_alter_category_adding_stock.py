# Generated by Django 3.2.3 on 2021-06-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_auto_20210609_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_adding',
            name='stock',
            field=models.CharField(choices=[('green', 'Stock'), ('blue', 'out of stock')], default='green', max_length=6),
        ),
    ]
