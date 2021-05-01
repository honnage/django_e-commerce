# Generated by Django 3.1.6 on 2021-05-01 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'หมวดหมู่สินค้า', 'verbose_name_plural': 'ข้อมูลประเภทสินค้า'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'รายการสินค้า', 'verbose_name_plural': 'ข้อมูลสินค้า'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]
