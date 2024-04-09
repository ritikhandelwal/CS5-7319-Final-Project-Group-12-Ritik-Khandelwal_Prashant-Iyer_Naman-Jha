

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0044_auto_20191010_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_list',
            name='custom_exta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item_list',
            name='custom_topping',
            field=models.BooleanField(default=False),
        ),
    ]
