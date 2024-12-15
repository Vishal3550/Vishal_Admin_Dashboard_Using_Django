from django.db import models

# Create your models here.

# Creating Company Model
class Company(models.Model):
    Company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('Non IT','Non IT'),
                                                  ('Mobiles Phones','Mobiles Phones')
                                                  ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    # Method Overriding
    def __str__(self):
        return self.name +','+ self.location

#Employee Model   
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50,unique=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=50,unique=True)
    about=models.TextField(max_length=50)
    position=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl')
    ))

    Company=models.ForeignKey(Company, on_delete=models.CASCADE)
    