from django.db import models

# Create your models here.


class University(models.Model):
    University_name = models.CharField(max_length=30)
    University_location = models.CharField(max_length=30)
    University_contacts = models.CharField(max_length=10,null=True,blank=True)
    University_image = models.ImageField(upload_to="University")

    def __str__(self):
        return self.University_name

class proff_of_university(models.Model):
    proff_of_university = models.ForeignKey(University,on_delete=models.CASCADE)
    proff_name = models.CharField(max_length=30)
    proff_salary = models.IntegerField()
    proff_image = models.ImageField(upload_to="proff_of_university")  

    def __str__(self):
        return self.proff_name 


class proff_details(models.Model):
    proff_details = models.ForeignKey(proff_of_university,on_delete=models.CASCADE)
    proff_name = models.CharField(max_length=30)
    proff_salary = models.IntegerField()
    proff_email = models.EmailField(max_length=30)
    proff_address = models.CharField(max_length=30)
    proff_lacture_fee = models.IntegerField(max_length=30)
    proff_image = models.ImageField(upload_to="proff_of_university") 


    def __str__(self):
        return self.proff_name + ',' +self.proff_email + ',' +self.proff_address