# Generated by Django 2.2 on 2022-02-04 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20220203_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcondition',
            old_name='Condition',
            new_name='ConditionName',
        ),
        migrations.RenameField(
            model_name='itemstatus',
            old_name='Status',
            new_name='StatusName',
        ),
    ]
