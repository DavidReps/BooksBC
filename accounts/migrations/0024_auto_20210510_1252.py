# Generated by Django 3.1.7 on 2021-05-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20210510_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='buyer_rating',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='seller_rating',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='WZWP4C6eAr5rVXTpeQQ3o7', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]