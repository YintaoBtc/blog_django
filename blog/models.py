from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")

    def __str__(self):
        return self.title
