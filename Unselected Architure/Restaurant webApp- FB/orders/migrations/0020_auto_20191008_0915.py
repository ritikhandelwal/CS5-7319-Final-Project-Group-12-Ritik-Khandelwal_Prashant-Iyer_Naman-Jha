

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='size_id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='topping_qty_id',
        ),
        migrations.RemoveField(
            model_name='price',
            name='menu_id',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
