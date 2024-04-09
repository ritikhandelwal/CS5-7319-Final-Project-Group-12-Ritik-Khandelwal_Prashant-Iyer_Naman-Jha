

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_auto_20191010_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='custom_size',
            field=models.BooleanField(default=False),
        ),
    ]
