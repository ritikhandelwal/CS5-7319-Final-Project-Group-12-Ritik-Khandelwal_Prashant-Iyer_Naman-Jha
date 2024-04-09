

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20191007_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping_qty',
            name='quantity',
            field=models.CharField(max_length=64),
        ),
    ]
