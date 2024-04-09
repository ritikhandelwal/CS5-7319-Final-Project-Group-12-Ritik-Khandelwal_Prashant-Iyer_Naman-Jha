

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0039_cart_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='menuprice',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menuprice',
            name='size',
        ),
        migrations.DeleteModel(
            name='Topping_qty',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='MenuPrice',
        ),
    ]
