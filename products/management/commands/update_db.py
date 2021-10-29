from django.core.management import BaseCommand

from users.models import UserProfile, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            UserProfile.objects.create(user=user)