from posts.models import User

all_users = User.objects.all()

for user in all_users:
    print(user.pk, ':', user.email, ' deleted')
    user.delete()
