from django.contrib.auth.models import User
try:
    user = User.objects.get(username='admin')
    print(f"User: {user.username}")
    print(f"Is Superuser: {user.is_superuser}")
    print(f"Is Staff: {user.is_staff}")
    print(f"Password Check (admin123): {user.check_password('admin123')}")
except User.DoesNotExist:
    print("User 'admin' does not exist.")
