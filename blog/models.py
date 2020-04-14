from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField()
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):

        return self.title

