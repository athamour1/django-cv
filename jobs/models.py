from django.db import models

class Jobpos(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Candidates(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    interested = models.TextField()
    github = models.TextField()
    article = models.TextField()

    job = models.ForeignKey(Jobpos, on_delete = models.CASCADE)

    def __str__(self):
        return self.fullname
