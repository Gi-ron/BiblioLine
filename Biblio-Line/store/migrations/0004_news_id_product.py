# Generated by Django 4.2 on 2023-05-17 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='id_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.products'),
        ),
    ]
