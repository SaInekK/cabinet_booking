# Generated by Django 4.0.1 on 2022-01-19 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='office',
        ),
        migrations.AddField(
            model_name='booking',
            name='workplace',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='workplaces', to='book_app.workplace', verbose_name='Workplace'),
            preserve_default=False,
        ),
    ]
