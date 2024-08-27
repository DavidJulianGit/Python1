# Generated by Django 4.2.15 on 2024-08-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Unknown Author', max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('hardcover', 'Hard cover'), ('ebook', 'E-Book'), ('audiobook', 'Audiobook')], default='hc', max_length=12),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('classic', 'Classic'), ('romantic', 'Romantic'), ('comic', 'Comic'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('educational', 'Educational')], default='cl', max_length=12),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(help_text='in US dollars $'),
        ),
    ]
