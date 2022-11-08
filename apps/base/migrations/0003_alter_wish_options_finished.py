# Generated by Django 4.0.4 on 2022-10-29 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_wish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'ordering': ['created']},
        ),
        migrations.CreateModel(
            name='Finished',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.library')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
