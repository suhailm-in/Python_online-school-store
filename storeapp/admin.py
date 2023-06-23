from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','mail_id','dob','materials_provided')

# Register your models here.
admin.site.register(Person,PersonAdmin)
