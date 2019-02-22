from django.db import models

class Publisher(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)

    def __unicode__(self):
        return self.fname

class Book(models.Model):
    title = models.CharField(max_length=40)
   
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

   
    def __unicode__(self):
        return self.title
