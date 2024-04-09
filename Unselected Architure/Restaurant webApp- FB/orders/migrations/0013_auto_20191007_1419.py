

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_menuprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuprice',
            name='topping_qty',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
