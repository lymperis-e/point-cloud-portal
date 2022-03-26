from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

crs_options = [
    ("GGRS87", "GGRS87")
]


class Cloud(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    file_name = models.CharField(max_length=100, blank=False, null=False)
    users = models.ManyToManyField(CustomUser, verbose_name="Users with access")
    description = models.CharField(max_length=250, default=" ")
    location = models.PointField(default="POINT(40.6254868487 22.9296330649)")
    crs = models.CharField(max_length=10, blank=True, default="", choices=crs_options)



    def __str__(self):
        return self.title


