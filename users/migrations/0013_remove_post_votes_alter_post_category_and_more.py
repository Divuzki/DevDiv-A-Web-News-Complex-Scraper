# Generated by Django 4.0.2 on 2022-03-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('uncategorized', 'uncategorized'), ('world', 'world'), ('politics', 'politics'), ('technology', 'technology'), ('science', 'science'), ('finace', 'finace'), ('education', 'education'), ('how-To', 'how-to'), ('lifeStyle', 'lifeStyle'), ('gossip', 'gossip')], default='uncategorized', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.CharField(blank=True, max_length=3080, null=True),
        ),
    ]
