

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20191008_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Cart'),
        ),
    ]
