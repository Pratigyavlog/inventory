from django.contrib import admin
from .models import Box
# Register your models here.
class BoxAdmin(admin.ModelAdmin):
  list_display=["creator","length","breadth","height","area","volume"]
admin.site.register(Box,BoxAdmin)