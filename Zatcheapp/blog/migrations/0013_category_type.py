# Generated by Django 4.1.3 on 2022-12-05 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_type_blog_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.type'),
        ),
    ]