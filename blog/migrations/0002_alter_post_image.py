# Generated by Django 4.0.4 on 2022-06-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default='https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png', max_length=200),
        ),
    ]
