from django.db import models

# Create your models here.

class  Admin(models.Model):
    Facultyid = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField()
    
    
    