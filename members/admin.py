from django.contrib import admin
from .models import Member
# Register your models here.

class Memberadmin(admin.ModelAdmin):
    list_display=['first_name','last_name','gender','email', 'joined_date','image','phone','description']
admin.site.register(Member, Memberadmin)