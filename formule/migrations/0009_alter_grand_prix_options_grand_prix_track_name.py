# Generated by Django 4.0.3 on 2022-04-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formule', '0008_alter_grand_prix_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grand_prix',
            options={'ordering': ['track_name']},
        ),
        migrations.AddField(
            model_name='grand_prix',
            name='track_name',
            field=models.CharField(default=1, max_length=20, verbose_name='Track name'),
            preserve_default=False,
        ),
    ]
