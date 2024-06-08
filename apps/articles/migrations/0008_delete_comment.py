from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
