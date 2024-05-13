# Generated by Django 4.2.6 on 2024-04-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(default='info@ise.uz', max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='no-image.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
