# Generated by Django 3.1.7 on 2021-02-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hull', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='category',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hull.category'),
        ),
    ]
