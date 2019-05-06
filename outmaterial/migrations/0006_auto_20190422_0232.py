# Generated by Django 2.2 on 2019-04-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outmaterial', '0005_outmaterial_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outmaterial',
            name='input_quality',
        ),
        migrations.AddField(
            model_name='outmaterial',
            name='id_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outmaterial',
            name='output_quality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outmaterial',
            name='received',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='outmaterial',
            name='used_type',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='unit',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
