from django.db import models
from django.contrib.auth.models import User
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
        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    photo = models.ImageField(blank=True, upload_to='photos')
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of {self.user.username}"



class Log(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
