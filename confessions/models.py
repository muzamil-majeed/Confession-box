from django.db import models

# Create your models here.


class Confession(models.Model):
    content_title = models.CharField(max_length=100,default="Anonymous")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.content_title



class Comment(models.Model):
    confession = models.ForeignKey(Confession,on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment on confession {self.confession.id}"


    