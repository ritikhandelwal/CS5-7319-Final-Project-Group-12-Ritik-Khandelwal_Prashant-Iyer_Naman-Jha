

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_auto_20191009_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_list',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='item_id',
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
