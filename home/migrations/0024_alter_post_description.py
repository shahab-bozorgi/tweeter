# Generated by Django 5.0.2 on 2024-04-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
