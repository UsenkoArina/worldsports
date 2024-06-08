from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
    ]
