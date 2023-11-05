from typing import Any
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, national_code, full_name, phone, email, password):
        if not national_code and len(national_code) !=10:
            raise ValueError('user mist have National code, length eq 10')
        if not full_name:
            raise ValueError('user must have full name')
        if not phone:
            raise ValueError('user must have phone number')
        if not email:
            raise ValueError('user must have email')
        
        user = self.model(national_code=national_code,
                          full_name=full_name,phone=phone,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, national_code, full_name, phone, email, password):
        super_user = self.create_user(national_code, full_name, phone, email, password)
        super_user.is_admin = True
        super_user.save(using=self._db)
        return super_user