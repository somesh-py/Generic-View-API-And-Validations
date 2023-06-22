from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','contact','email','address']