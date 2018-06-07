from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from members.models import Musician

# Register your models here.
'''Define an inline admin descriptor for Employee model which acts a bit like a singleton
https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model '''

class MusicianInline(admin.StackedInline):
    model = Musician
    can_delete = False
    verbose_name_plural = 'musician'
    
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (MusicianInline, )
    
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)    

