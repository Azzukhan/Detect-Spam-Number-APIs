from django.contrib import auth
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(auth.get_user_model(), on_delete=models.PROTECT)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return str(self.user)

class Contacts(models.Model):
    phone = models.CharField(max_length=13)
    user = models.ForeignKey(UserProfile,null=True, on_delete=models.PROTECT )
    name = models.CharField(max_length=255)
    spam = models.BooleanField(default=False)
