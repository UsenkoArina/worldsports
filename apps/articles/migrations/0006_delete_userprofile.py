from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
