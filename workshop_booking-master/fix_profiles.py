from django.contrib.auth.models import User
from workshop_app.models import Profile

def run():
    users_without_profiles = User.objects.filter(profile__isnull=True)
    count = 0
    for user in users_without_profiles:
        Profile.objects.create(
            user=user,
            institute="Default Institute",
            department="computer science",
            phone_number="0000000000",
            location="Default Location",
            state="IN-MH",
            is_email_verified=True # Auto-verify to allow access
        )
        count += 1
    print(f"Created {count} missing profiles.")

run()
