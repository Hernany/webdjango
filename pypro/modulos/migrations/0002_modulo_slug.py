# Generated by Django 3.0.2 on 2020-01-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('publico', models.TextField()),
                ('descricao', models.TextField()),
                ('slug', models.SlugField(null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]