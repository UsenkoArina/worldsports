from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_article_likes_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
    ]
