from django.contrib import admin
from base.models import PhoneBook


@admin.register(PhoneBook)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number','description','create')
    list_filter = ['create']
    ordering = ['-create']