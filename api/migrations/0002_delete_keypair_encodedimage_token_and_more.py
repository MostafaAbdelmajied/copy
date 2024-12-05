# Generated by Django 5.1.3 on 2024-12-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KeyPair',
        ),
        migrations.AddField(
            model_name='encodedimage',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='encodedimage',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
