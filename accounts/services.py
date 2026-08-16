from .models import User

def authenticate_user(username, password):
    user = User.objects.filter(username=username).first()
    if not user or not user.check_password(password) or user.status != 'active':
        return None
    return user