from django.contrib import admin
from models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# from .models import User
# admin.site.register(User)
class UserProfileInline(admin.StackedInline):  
    model=UserProfile  
    fk_name='user'  
    max_num=1  
      
class UserProfileAdmin(UserAdmin):  
    inlines = [UserProfileInline, ]  
      
admin.site.unregister(User)  
admin.site.register(User,UserProfileAdmin)  