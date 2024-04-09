

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191007_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='size_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='topping_qty_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Topping_qty'),
        ),
    ]
