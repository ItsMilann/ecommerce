# Generated by Django 2.2 on 2020-01-17 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_order_reference_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('accepted', models.BooleanField()),
                ('rejected', models.BooleanField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Order')),
            ],
        ),
    ]
