from django.db import models

class Jobpos(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title