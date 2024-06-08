from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='registration_date',
        ),
    ]
