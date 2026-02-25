from django.contrib import admin
from .models import Confession

# Register your models here.
class ConfessionAdmin(admin.ModelAdmin):
    list_display = ("content_title","created_at","is_approved")

admin.site.register(Confession,ConfessionAdmin)