from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text of the article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
    ]
