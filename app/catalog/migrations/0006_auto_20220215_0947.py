# Generated by Django 2.2 on 2022-02-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20220111_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='databases',
            options={'verbose_name_plural': 'Databases'},
        ),
        migrations.AlterModelOptions(
            name='servers',
            options={'verbose_name_plural': 'Servers'},
        ),
        migrations.AlterModelOptions(
            name='tables',
            options={'verbose_name_plural': 'Tables'},
        ),
    ]
