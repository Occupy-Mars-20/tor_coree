import datetime
from django.db.models.deletion import CASCADE
from django.db import models

# Create your models here.

# Company


class Companysignup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    def isExists(self):
        try:
            if Companysignup.objects.get(username=self.username):
                return True
        except:
            return False


class Company(models.Model):
    companysignup_id = models.ForeignKey(
        Companysignup, related_name='companysignup', on_delete=CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    companyname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='companyimage')
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Province(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='provinces')

    def __str__(self):
        return self.name


class Trip(models.Model):
    company_id = models.ForeignKey(
        Company, related_name='company', on_delete=CASCADE)
    place = models.CharField(max_length=100)
    price = models.IntegerField()
    province = models.ForeignKey(
        Province, related_name='province', on_delete=CASCADE)
    city = models.CharField(max_length=50)
    noofdays = models.IntegerField()
    departuredate = models.DateField()
    createddate = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='tripimage')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

# Main page


class HomeIMG1(models.Model):
    image = models.ImageField(upload_to='homeimg1')


class HomeIMG2(models.Model):
    image = models.ImageField(upload_to='homeimg2')


class AboutIMG1(models.Model):
    image = models.ImageField(upload_to='aboutimg2')


class AboutIMG2(models.Model):
    image = models.ImageField(upload_to='aboutimg2')


class ExperienceCount(models.Model):
    years = models.IntegerField()
    no_of_completed_tours = models.IntegerField()
    no_of_destinations = models.IntegerField()


class ExperienceIMG1(models.Model):
    image = models.ImageField(upload_to='experienceimg2')


class ExperienceIMG2(models.Model):
    image = models.ImageField(upload_to='experienceimg2')


class Video(models.Model):
    video = models.FileField(upload_to='video')

# User


class Usersignup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    def isExists(self):
        try:
            if Usersignup.objects.get(username=self.username):
                return True
        except:
            return False


# order
class Order(models.Model):
    usersignup_id = models.ForeignKey(Usersignup, related_name='usersignup_id', on_delete=CASCADE)
    trip_id = models.ForeignKey(Trip, related_name='trip', on_delete=CASCADE)
    order_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    persons = models.IntegerField()
    message = models.CharField(max_length=250)
    order_date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)
    review = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id

# order
class Feedback(models.Model):
    usersignup_id = models.ForeignKey(Usersignup, related_name='usignup_id', on_delete=CASCADE)
    order_id = models.ForeignKey(Order, related_name='orderid', on_delete=CASCADE)
    stars = models.FloatField()
    feedback = models.CharField(max_length=250)
    feedback_date = models.DateField(default=datetime.date.today)