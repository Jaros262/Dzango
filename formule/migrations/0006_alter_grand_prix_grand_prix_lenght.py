# Generated by Django 4.0.3 on 2022-04-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formule', '0005_alter_grand_prix_grand_prix_lenght'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grand_prix',
            name='grand_prix_lenght',
            field=models.DecimalField(decimal_places=2, default=3100, help_text='Enter lenght in Km', max_digits=6, verbose_name='Track lenght'),
        ),
    ]