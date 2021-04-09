from django.contrib import admin
from .models import coffee
from .models import tea
from .models import juice
from .models import contact
# Register your models here.
class displaycoffe(admin.ModelAdmin):
     list_display = ('name', 'price')

class displaytea (admin.ModelAdmin):
     list_display = ('name', 'price')
    
class displayjuice (admin.ModelAdmin):
     list_display = ('name', 'price')

class displaycontact (admin.ModelAdmin):
     list_display = ('Name', 'email')
     
admin.site.register(coffee, displaycoffe)
admin.site.register(tea, displaytea)
admin.site.register(juice, displayjuice)
admin.site.register(contact, displaycontact)