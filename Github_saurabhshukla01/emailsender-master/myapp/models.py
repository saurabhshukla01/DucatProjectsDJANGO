from django.db import models
class Emp(models.Model):
	email=models.EmailField()
	message=models.CharField(max_length=30)
	class Meta:  
		db_table = "emp"  
class Empl(models.Model):
	mail=models.FileField(upload_to="csv_file")
	mes=models.CharField(max_length=30)
	class Meta:  
		db_table = "empl"  		