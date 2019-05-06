# Generated by Django 2.2 on 2019-04-16 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outmaterial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypeOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='outmaterial',
            old_name='id_material',
            new_name='input_quality',
        ),
        migrations.RemoveField(
            model_name='outmaterial',
            name='output_quality',
        ),
        migrations.RemoveField(
            model_name='outmaterial',
            name='received',
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outmaterial.ProductTypeOut'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='unit',
            field=models.IntegerField(max_length=100),
        ),
    ]
