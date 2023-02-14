from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Runs a sample cron job'

    def handle(self, *args, **kwargs):
        # Your cron job logic here
        print('Cron job run at {}'.format(timezone.now()))