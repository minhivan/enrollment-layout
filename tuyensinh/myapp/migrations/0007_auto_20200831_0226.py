# Generated by Django 3.0.5 on 2020-08-31 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200830_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Applicants'),
        ),
    ]