from django.shortcuts import render
from base.models import *


def getPhones(request):
    phones = PhoneBook.objects.all().order_by('-create')
    
    context = {
        'phones':phones,
    }
    
    return render(request, 'index.html', context)