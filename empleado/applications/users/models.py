from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin #Perm.. : creac de superusuarios dsd 
                                        #la consola,y q tmb trabje con este modelo q acabamos de implementar

from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):      #diremos q al trabajar con usuarios trabaje con esto y 
                                                    #no con el modelo interno que traía
    GENDER_CHOICES=(    
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    #
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)


    USERNAME_FIELD='username'

    REQUIRED_FIELDS=['email']

    objects=UserManager()

    def get_short_name(self):
        return self.username 

    def get_full_name(self):
        return self.nombres+' '+self.apellidos
        #return self.name+' '+self.lastname