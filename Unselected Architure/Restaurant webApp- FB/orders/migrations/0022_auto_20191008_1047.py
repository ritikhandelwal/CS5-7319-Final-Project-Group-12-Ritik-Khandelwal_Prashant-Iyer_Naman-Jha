

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_topping_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='pizza',
        ),
        migrations.AddField(
            model_name='cart',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.Topping'),
        ),
    ]
