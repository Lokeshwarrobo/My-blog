# Generated by Django 3.0.2 on 2020-04-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(default=1, upload_to='hero_headshots/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
