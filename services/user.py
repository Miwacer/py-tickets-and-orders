from db.models import User

def create_user(
        username: str,
        first_name: str,
        last_name: str,
        password: str,
        email: str,
):
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    user.save()


def get_user(user_id: int) -> User:
        return User.objects.get(id=user_id)


def update_user(
        user_id: int,
        username: str = None,
        first_name: str = None,
        last_name: str = None,
        password: str = None,
        email: str = None,
) -> User:
    user = get_user(user_id)

    if username:
        user.username = username

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    if password:
        user.set_password(password)

    if email:
        user.email = email

    user.save()

    return user