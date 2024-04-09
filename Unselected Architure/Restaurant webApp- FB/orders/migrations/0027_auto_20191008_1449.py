

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20191008_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping_qty',
            name='quantity',
            field=models.CharField(max_length=64),
        ),
    ]
