

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_price_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('base_price_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Price_List')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='pricelist',
            name='category',
        ),
        migrations.DeleteModel(
            name='PriceList',
        ),
    ]
