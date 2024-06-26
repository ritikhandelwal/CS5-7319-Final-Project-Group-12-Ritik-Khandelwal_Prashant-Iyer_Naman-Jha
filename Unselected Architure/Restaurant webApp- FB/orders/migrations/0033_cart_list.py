

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0032_auto_20191009_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('large', models.BooleanField()),
                ('topping_qty', models.IntegerField(blank=True, null=True)),
                ('extra_qty', models.IntegerField(blank=True, null=True)),
                ('calculated_price', models.FloatField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Item_List')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
