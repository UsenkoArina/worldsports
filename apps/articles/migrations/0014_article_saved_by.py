from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0013_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='saved_by',
            field=models.ManyToManyField(blank=True, related_name='saved_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
