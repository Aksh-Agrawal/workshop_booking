import os
import django
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

def setup():
    
    group_name = 'instructor'
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"Group '{group_name}' created.")
        # Assign all permissions
        all_permissions = Permission.objects.all()
        group.permissions.set(all_permissions)
        print("Assigned all permissions to group 'instructor'.")
    else:
        print(f"Group '{group_name}' already exists.")

    
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created with password '{password}'.")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    setup()
