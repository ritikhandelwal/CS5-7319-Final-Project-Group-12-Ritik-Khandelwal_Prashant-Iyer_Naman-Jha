

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20191007_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('topping_qty', models.IntegerField(blank=True, null=True)),
                ('size', models.CharField(blank=True, max_length=64, null=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
