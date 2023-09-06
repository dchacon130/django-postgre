from django.contrib import admin
from .models import User

# Register your models here.

# Show models in the Admin
class MyApp(admin.ModelAdmin):
    title = 'My User Model'
    list_display = ['number' , 'firstname', 'lastname', 'birtday', 'language', 'country','create_at', 'update_at']
    
admin.site.register(User, MyApp)