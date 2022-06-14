# Generated by Django 3.2.13 on 2022-06-14 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_support_tickets_tickets_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support_tickets',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SupportTickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tickets_messages',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tickets', to='accounts.support_tickets'),
        ),
    ]
