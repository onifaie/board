# Generated by Django 3.2.4 on 2021-06-10 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0008_remove_board_topcreated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='topcreated_by',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='Board_User', to='auth.user'),
            preserve_default=False,
        ),
    ]
