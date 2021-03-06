# Generated by Django 3.1.7 on 2021-04-04 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210404_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artykl',
            name='bed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artykl',
            name='bes',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artykl',
            name='note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='artykl',
            name='taf1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taf1s', to='api.tafsili'),
        ),
        migrations.AlterField(
            model_name='artykl',
            name='taf2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taf2s', to='api.tafsili'),
        ),
        migrations.AlterField(
            model_name='artykl',
            name='taf3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taf3s', to='api.tafsili'),
        ),
    ]
