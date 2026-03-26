
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_intensity_speechfeature_pause_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpeechFeature',
        ),
    ]
