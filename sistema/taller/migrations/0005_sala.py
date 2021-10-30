# Generated by Django 3.2.7 on 2021-09-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0004_cine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('numero', models.CharField(max_length=256)),
                ('cine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taller.cine')),
            ],
        ),
    ]
