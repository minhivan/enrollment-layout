# Generated by Django 3.0.5 on 2020-09-01 19:25

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=2)),
                ('pob', models.CharField(max_length=255)),
                ('nation', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('identity', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=100)),
                ('wards', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Majors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=10)),
                ('subject_id', djongo.models.fields.JSONField()),
                ('target_amount', models.IntegerField(null=True)),
                ('date_expired', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('subject', djongo.models.fields.JSONField()),
                ('label', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('meta_data', djongo.models.fields.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('details', djongo.models.fields.JSONField()),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Applicants')),
            ],
        ),
    ]
