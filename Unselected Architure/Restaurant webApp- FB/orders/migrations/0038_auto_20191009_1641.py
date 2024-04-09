

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_cart_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_list',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='price_id',
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='size',
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Cart_List',
        ),
    ]
