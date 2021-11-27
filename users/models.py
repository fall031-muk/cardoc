from django.db                     import models
from django.contrib.auth.hashers   import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models    import UserManager

class CustomUserManagoer(UserManager):
    def _create_user(self, userid, password, **extra_field):
        if not userid:
            raise ValueError("input user_id")
        user          = self.model(userid=userid, **extra_field)
        user.password = make_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, userid, password=None, **extra_fields):
        return self._create_user(userid, password, **extra_fields)
        

class User(AbstractBaseUser):
    userid    = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    USERNAME_FIELD = 'userid'
    objects = CustomUserManagoer()