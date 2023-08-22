# Generated by Django 4.2.4 on 2023-08-22 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_answer_creationtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]