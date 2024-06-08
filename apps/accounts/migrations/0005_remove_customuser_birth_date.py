from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birth_date',
        ),
    ]
