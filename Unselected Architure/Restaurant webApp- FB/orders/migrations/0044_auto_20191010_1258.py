

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0043_auto_20191010_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_list',
            old_name='current',
            new_name='is_current',
        ),
    ]
