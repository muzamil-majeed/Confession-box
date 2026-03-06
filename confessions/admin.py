from django.contrib import admin
from .models import Confession,Comment

# Register your models here.
class ConfessionAdmin(admin.ModelAdmin):
    list_display = ("content_title","created_at","is_approved")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("confession","created_at")
    search_fields =("content",)
admin.site.register(Confession,ConfessionAdmin)

admin.site.register(Comment,CommentAdmin)