from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
