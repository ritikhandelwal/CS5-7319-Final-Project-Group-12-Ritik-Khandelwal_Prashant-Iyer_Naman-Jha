

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20191007_1258'),
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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='menu',
            name='topping_qty_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_qty'),
        ),
        migrations.AlterField(
            model_name='price',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Menu', unique=True),
        ),
    ]
