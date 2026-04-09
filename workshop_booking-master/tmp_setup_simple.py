from django.contrib.auth.models import User, Group, Permission

def setup():
   
    group_name = 'instructor'
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print(f"Group '{group_name}' created.")
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

setup()
