from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    has_been_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
