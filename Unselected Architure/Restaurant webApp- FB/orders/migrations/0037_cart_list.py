

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0036_auto_20191009_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculated_price', models.FloatField()),
                ('extra', models.ManyToManyField(blank=True, to='orders.Extra')),
                ('price_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Price_List')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
