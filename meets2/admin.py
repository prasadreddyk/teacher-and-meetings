from django.contrib import admin
from. models import Teachers_list

class teacherdetailsadmin(admin.ModelAdmin):
    list_display=['id','teacher_name','email','qualification','subject']

admin.site.register(Teachers_list,teacherdetailsadmin)
