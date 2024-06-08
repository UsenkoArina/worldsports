from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customuser_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
