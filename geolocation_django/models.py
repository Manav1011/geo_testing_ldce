from django.db import models

class geo_cordinates(models.Model):
    branch = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.branch} - {self.class_name} - {self.latitude} - {self.longitude}"