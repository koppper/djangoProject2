# Generated by Django 3.2.5 on 2022-04-13 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Shop Name')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Product Name')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('update_counter', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shops.category')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
            options={
                'verbose_name': 'Goods',
                'verbose_name_plural': 'Goods',
                'ordering': ('id',),
            },
        ),
    ]
