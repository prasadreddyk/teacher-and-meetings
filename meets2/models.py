from django.db import models
class Teachers_list(models.Model):
    teacher_name=models.CharField(max_length=255, unique=True)
    email=models.EmailField(max_length=255, unique=True )
    qualification=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)

    def __str__(self):
        return self.teacher_name
