# Generated by Django 4.0.3 on 2022-04-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formule', '0004_alter_grand_prix_grand_prix_lenght_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grand_prix',
            name='grand_prix_lenght',
            field=models.IntegerField(default=3100, help_text='Enter lenght in Km', verbose_name='Track lenght'),
        ),
    ]