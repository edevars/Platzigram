from posts.models import User

admin_platzi_users = User.objects.filter(
    email__endswith="@platzi.com").update(is_admin=True)

all_users = User.objects.filter(is_admin=True)

for user in all_users:
    print(user.pk, ':', user.email, ':', user.is_admin)
