
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speechfeature',
            old_name='intensity',
            new_name='pause',
        ),
        migrations.RenameField(
            model_name='speechfeature',
            old_name='pitch',
            new_name='speech_rate',
        ),
    ]
