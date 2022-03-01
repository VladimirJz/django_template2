# Generated by Django 2.2 on 2022-02-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0009_auto_20220215_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rotationrules',
            options={'ordering': ['Job', 'Order'], 'verbose_name_plural': 'Rotation rules'},
        ),
        migrations.AddField(
            model_name='backups',
            name='Updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated on'),
        ),
        migrations.AlterField(
            model_name='rotationrules',
            name='FileTag',
            field=models.CharField(blank=True, help_text='Add tag to filename ultil remains on this location', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rotationrules',
            name='RetentionDays',
            field=models.SmallIntegerField(help_text='Total age of backup file', verbose_name='Expire at'),
        ),
        migrations.AlterModelTable(
            name='jobs',
            table='backup_jobs',
        ),
        migrations.AlterModelTable(
            name='locations',
            table='backup_locations',
        ),
        migrations.AlterModelTable(
            name='rotationrules',
            table='backup_rotationrules',
        ),
        migrations.AlterModelTable(
            name='status',
            table='backup_status',
        ),
    ]
