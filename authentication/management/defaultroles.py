from django.core.management.base import BaseCommand
from authentication.models import Role

class Command(BaseCommand):
    help = 'Set a default role for all users upon creation'

    def handle(self, *args, **options):
        # Define the default role name you want to assign to all users
        default_role_name = 'user'

        # Check if the default role already exists
        default_role, created = Role.objects.get_or_create(name=default_role_name)

        # Assign the default role to all existing users
        from django.contrib.auth.models import User
        users_without_role = User.objects.filter(role__isnull=True)

        for user in users_without_role:
            user.role.add(default_role)
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully assigned "{default_role_name}" to all users.'))
