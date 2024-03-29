# Generated by Django 3.2.8 on 2021-11-08 08:50

from django.db import migrations, models
import forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_forum_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='image',
            field=models.ImageField(upload_to='media/forum', validators=[forum.models.validate_image]),
        ),
    ]
