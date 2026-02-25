from django.db import models

# Create your models here.


class Confession(models.Model):
    content_title = models.CharField(max_length=100,default="Anonymous")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.content_title