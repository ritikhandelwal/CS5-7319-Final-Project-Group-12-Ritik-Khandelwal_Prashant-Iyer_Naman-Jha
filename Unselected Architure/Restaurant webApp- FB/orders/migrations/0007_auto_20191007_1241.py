

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191007_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='size_id',
        ),
        migrations.RemoveField(
            model_name='price',
            name='topping_qty_id',
        ),
        migrations.AddField(
            model_name='menu',
            name='size_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='topping_qty_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_qty'),
            preserve_default=False,
        ),
    ]
