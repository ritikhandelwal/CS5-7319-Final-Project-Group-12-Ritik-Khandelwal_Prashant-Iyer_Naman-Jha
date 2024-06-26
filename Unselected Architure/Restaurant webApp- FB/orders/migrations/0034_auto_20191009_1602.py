

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_cart_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='extra_qty',
        ),
        migrations.RemoveField(
            model_name='cart_list',
            name='topping_qty',
        ),
        migrations.AlterField(
            model_name='cart_list',
            name='large',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='cart_list',
            name='extra',
            field=models.ManyToManyField(blank=True, to='orders.Extra'),
        ),
    ]
