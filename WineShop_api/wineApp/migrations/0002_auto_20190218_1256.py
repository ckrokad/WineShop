# Generated by Django 2.1.5 on 2019-02-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='country',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='description',
            field=models.CharField(default='', max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='designation',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='province',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='region_1',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='region_2',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='variety',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='winery',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]