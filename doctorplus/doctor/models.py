from django.db import models

# Create your models here.

class DoctorInfo(models.Model):
    STATUS_CHOICES = [
            ('Active','Active'),
            ('Inactive','Inactive'),
    ]
    GENDER_CHOICES = (
                ('Male','Male'),
                ('Female','Female'),
                ('Other','Other'),
    )
    
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length =100)
    last_name=  models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10,choices = GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField  (max_length = 200, unique = True)
    phone_number = models.CharField(max_length = 10,unique=True)
    qualification = models.CharField(max_length=250)
    specialization = models.CharField(max_length = 100)
    year_of_experience = models.PositiveIntegerField()
    consultation_fees = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length = 10,choices = STATUS_CHOICES,default='Active')
    available_days = models.CharField(max_length=100)
    available_time = models.TimeField()

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"