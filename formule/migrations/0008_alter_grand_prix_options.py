# Generated by Django 4.0.3 on 2022-04-13 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formule', '0007_alter_grand_prix_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grand_prix',
            options={'ordering': ['nationality_name']},
        ),
    ]
