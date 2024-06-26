

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_pricelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('base_price', models.FloatField()),
                ('large_supp', models.FloatField()),
            ],
        ),
    ]
