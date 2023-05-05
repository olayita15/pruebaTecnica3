# Generated by Django 4.2 on 2023-05-03 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='api.office'),
        ),
        migrations.AlterField(
            model_name='office',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]