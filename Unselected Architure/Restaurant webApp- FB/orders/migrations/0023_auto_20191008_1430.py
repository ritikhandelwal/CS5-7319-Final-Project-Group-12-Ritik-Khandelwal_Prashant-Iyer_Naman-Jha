

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20191008_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuprice',
            name='topping_qty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_qty'),
        ),
    ]
