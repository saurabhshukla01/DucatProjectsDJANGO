from django.db import models
from django.urls import reverse

class Employee(models.Model):
    ename = models.CharField(max_length=30)
    eage = models.IntegerField()
    ecity = models.CharField(max_length=30)
    edsg = models.CharField(max_length=30)

    class Meta:
        db_table = 'emp'
		
    def get_absolute_url(self):
        return reverse('index')
		
class College(models.Model):
    college_code = models.IntegerField()
    college = models.CharField(max_length=50)

    def __str__(self):
        return self.college
		
    def get_absolute_url(self):
        return reverse('home')
	
    class Meta:
        verbose_name_plural = "College"	

class Student(models.Model):
    choices = (('M','Male'),('F','Female'))
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(choices=choices, max_length=50)
    college = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
	
    def get_absolute_url(self):
        return reverse('home')
	
		
class Book(models.Model):
    owner = models.OneToOneField(Student,on_delete=models.CASCADE)
    book_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.book_name
    def get_absolute_url(self):
        return reverse('home')
		
# Create your models here.
