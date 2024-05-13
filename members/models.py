from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70, null=True, blank=True)
    phone = models.IntegerField(null=True ,blank=True)
    email = models.EmailField(default="figma@gmail.com")
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    joined_date = models.DateField(null=True,blank=True )
    image = models.ImageField(default='image.jpg')
    description = models.TextField(null=True, blank=True, default="text")


    def __str__(self):
        if self.joined_date:
            return f"{self.first_name}; {self.last_name}; {self.joined_date.strftime('%Y-%m-%d')}; {self.email}; {self.phone}"
        else:
            return f"{self.first_name} {self.last_name}"