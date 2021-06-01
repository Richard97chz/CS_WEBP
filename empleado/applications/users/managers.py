from django.db import models
#
from django.contrib.auth.models import BaseUserManager  #para hacernos cargo de toda la admin de usuarios

class UserManager(BaseUserManager,models.Manager):
    def _create_user(self,username,email,password, is_staff,is_superuser,**extra_fields):
                                                                  #staff: pueda o no acceder al admin de DJ
        user=self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields 
        )
        user.set_password(password)  
        user.save(using=self.db)
        return user    

    def create_user(self,username,email,password=None,**extra_fields):  
                                #a esta funcion la llamará cuando se cree un usuario dentro de nuestro proyecto
        return self._create_user(username,email,password,False,False,**extra_fields)

    def create_superuser(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password,True,True,**extra_fields)  #para que se acceda a create_superuser cuando solo llamen a esta funcion


 