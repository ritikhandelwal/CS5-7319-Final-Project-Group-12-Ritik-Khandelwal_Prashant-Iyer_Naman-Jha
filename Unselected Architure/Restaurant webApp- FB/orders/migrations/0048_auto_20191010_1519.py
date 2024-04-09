

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0047_category_custom_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='custom_exta',
            new_name='custom_extra',
        ),
    ]
