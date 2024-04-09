

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplate',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salad',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sub',
            name='price',
            field=models.FloatField(),
        ),
    ]
