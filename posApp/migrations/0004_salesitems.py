# Generated by Django 3.2.5 on 2022-03-04 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0003_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('qty', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posApp.products')),
                ('sale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posApp.sales')),
            ],
        ),
    ]
