from django.db import models

class Abstract(models.Model):
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True