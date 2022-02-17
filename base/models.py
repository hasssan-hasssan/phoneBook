from django.db import models



class PhoneBook(models.Model):
    phone_number = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    description = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.phone_number

    def __unicode__(self):
        return self.phone_number
