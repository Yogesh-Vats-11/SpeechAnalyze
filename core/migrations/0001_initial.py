
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeechFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jitter', models.FloatField()),
                ('shimmer', models.FloatField()),
                ('pitch', models.FloatField()),
                ('intensity', models.FloatField()),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
