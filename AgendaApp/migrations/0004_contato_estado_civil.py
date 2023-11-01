# Generated by Django 4.2.6 on 2023-10-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0003_alter_contato_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='estado_civil',
            field=models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=1, null=True),
        ),
    ]
