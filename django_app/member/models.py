from django.contrib.auth.models import UserManager, AbstractUser


class MyUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    pass
