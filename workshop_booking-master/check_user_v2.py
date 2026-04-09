from django.contrib.auth.models import User
import sys
try:
    user = User.objects.get(username='admin')
    res = f"User: {user.username}, Super: {user.is_superuser}, Staff: {user.is_staff}, PwdCorrect: {user.check_password('admin123')}"
except User.DoesNotExist:
    res = "User 'admin' does not exist."
with open('user_debug.txt', 'w') as f:
    f.write(res)
