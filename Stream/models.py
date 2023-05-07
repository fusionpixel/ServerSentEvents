from django.db import models

# Create your models here.
class Transaction(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=10)
    punch_time = models.DateTimeField()

    def __str__(self):
        return f"{self.emp_name}- {self.punch_time.strftime('%Y-%m-%d %H:%M:%S')}"
