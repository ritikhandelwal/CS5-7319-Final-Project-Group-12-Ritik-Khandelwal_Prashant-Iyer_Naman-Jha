

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_auto_20191009_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_list',
            old_name='large',
            new_name='size',
        ),
    ]