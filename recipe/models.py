from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
