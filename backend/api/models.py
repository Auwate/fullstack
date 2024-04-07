from django.db import models

class Address (models.Model):

    body = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
