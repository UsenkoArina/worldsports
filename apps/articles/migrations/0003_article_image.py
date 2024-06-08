from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_sportcategory_article_unique_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
