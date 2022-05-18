from django.db import models

# Create your models here.
class stud(models.Model):
    ID =	models.IntegerField(primary_key=True)
    first_name	=	models.CharField(max_length=50)
    last_name	=	models.CharField(max_length=50)
    email	=	models.EmailField(max_length=50)
    gender	=	models.CharField(max_length=50)
    school	=	models.CharField(max_length=50)
    books=	models.CharField(max_length=50)

class school(models.Model):
    REGIONID =	models.IntegerField(primary_key=False)
    school	=	models.CharField(max_length=50)
    email	=	models.CharField(max_length=50)
    principal	=	models.EmailField(max_length=50)
    phone	=	models.CharField(max_length=50)
    address2	=	models.CharField(max_length=50)



class books(models.Model):
    Title =	models.CharField(max_length=50, default="")
    Author_Name	=	models.CharField(max_length=50)
    Date_of_Publication	=	models.CharField(max_length=50)
    Number_of_Pages	=	models.CharField(max_length=50)

