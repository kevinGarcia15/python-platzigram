from django.db import models
from django.contrib.auth.models import User

class Porfile(models.Model):
    """Porfile models
    Proxy model that extends the base data with other information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    pucture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #Retrun username
        return self.user.username