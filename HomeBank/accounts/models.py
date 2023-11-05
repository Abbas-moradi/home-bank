from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager
import uuid


class User(AbstractBaseUser):
    id = models.UUIDField(uuid.uuid4, editable=False, unique=True, primary_key=True)
    national_code = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    sex = models.CharField(max_length=10, choices=[
        ('M', 'men'),
        ('W', 'women')
    ])
    photo = models.ImageField(upload_to='media/%Y/%m/%d/')
    join_date = models.DateField(auto_now_add=True)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    directorship = models.BooleanField(default=False)
    is_inspector = models.BooleanField(default=False)

    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['full_name', 'phone', 'email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.national_code
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_madule_perms(self, app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

