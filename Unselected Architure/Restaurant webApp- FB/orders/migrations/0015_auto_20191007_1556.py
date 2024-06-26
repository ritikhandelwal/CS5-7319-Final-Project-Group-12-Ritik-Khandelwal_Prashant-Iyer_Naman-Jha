

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20191007_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuprice',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='menuprice',
            name='topping_qty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_qty'),
        ),
    ]
