

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0045_auto_20191010_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_list',
            name='custom_exta',
        ),
        migrations.RemoveField(
            model_name='item_list',
            name='custom_topping',
        ),
        migrations.AddField(
            model_name='category',
            name='custom_exta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='custom_topping',
            field=models.BooleanField(default=False),
        ),
    ]
