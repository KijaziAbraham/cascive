# Generated by Django 4.2.5 on 2023-12-16 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_of_semester', models.TextField(max_length=1000)),
                ('picture_of_semester', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('content', models.TextField(max_length=500)),
                ('theme_of_week', models.TextField(max_length=1000)),
                ('picture_of_week', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('malengo_title', models.CharField(max_length=255)),
                ('malengo_content', models.TextField(max_length=10000)),
                ('malengo_created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='home_models_related', to='home_app.category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='home_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_related', to='home_app.homemodel'),
        ),
    ]
