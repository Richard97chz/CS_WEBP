from django.contrib import admin

# Register your models here.


from .models import User    #importamos la tabla
# Register your models here.
admin.site.register(User)   #para registrarlo en el admin