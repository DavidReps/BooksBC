# Generated by Django 3.2 on 2021-05-05 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210505_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookId',
            field=models.CharField(default='cjxVVFA9NmTn8cLj527kxw', editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]
