# Generated by Django 2.2 on 2019-06-04 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farma_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtable',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='consumption',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
    ]
