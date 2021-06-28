# Generated by Django 3.2.3 on 2021-06-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0004_categoryadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_adding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='picture/')),
                ('stock', models.CharField(choices=[('green', 'InStock'), ('blue', 'Out of Stock')], default='green', max_length=6)),
            ],
        ),
    ]
