# Generated by Django 4.2.16 on 2024-11-19 17:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='task1.buyer')),
            ],
        ),
    ]