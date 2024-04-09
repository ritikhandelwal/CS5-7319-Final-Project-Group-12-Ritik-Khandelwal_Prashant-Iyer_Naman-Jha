

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20191008_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping_qty',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
