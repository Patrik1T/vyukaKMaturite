# Generated by Django 5.0.6 on 2024-06-08 10:54

import django.core.validators
import django.db.models.deletion
import vyuka.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Zapiš o jaký předmět se jedná (PVY OS...)', max_length=50, unique=True, verbose_name='Název předmětu')),
            ],
            options={
                'verbose_name': 'Předmět',
                'verbose_name_plural': 'Předměty',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Název')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Obsah')),
                ('release_date', models.DateField(blank=True, help_text='Zadej datum vydání textu: <em>YYYYMM-DD</em>.', null=True, verbose_name='Vydání textu')),
                ('runtime', models.IntegerField(blank=True, help_text='Prosím zadej v hodinách', null=True, verbose_name='Jak dlouho bude trvat se naučit:')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='film/posters/%Y/%m/%d/', verbose_name='Logo')),
                ('rate', models.FloatField(default=5.0, help_text='Ohodnoť svůj výukový materiál (1 - 10)', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Ohodnoť')),
                ('genres', models.ManyToManyField(help_text='Vyber předmět pro tvůj výukový materiál.', to='vyuka.predmet')),
            ],
            options={
                'verbose_name': 'Výukový materiál',
                'verbose_name_plural': 'Výukový materiál',
                'ordering': ['-release_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Priloha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nazev')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to=vyuka.models.attachment_path, verbose_name='Soubor')),
                ('type', models.CharField(blank=True, choices=[('audio', 'Audio'), ('image', 'Image'), ('text', 'Text'), ('video', 'Video'), ('other', 'Other')], default='image', help_text='Zadej danou Přílohu.', max_length=10, verbose_name='Attachment type')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyuka.material')),
            ],
            options={
                'verbose_name': 'Příloha',
                'verbose_name_plural': 'Přílohy',
                'ordering': ['-last_update', 'type'],
            },
        ),
    ]