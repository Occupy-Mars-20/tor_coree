from django.contrib import admin
from . import models
admin.site.site_header = "Trip on Review Admin"
admin.site.site_title = "Trip on Review Admin Portal"
admin.site.index_title = "Welcome To Trip on Review Admin Portal"
# Register your models here.

# company
@admin.register(models.Companysignup)
class CompanysignupAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password']

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','companysignup_id','fname','lname','email','phone','companyname','city','image','description','status']

@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['id','name','image']

@admin.register(models.Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id','company_id','place','price','province','city','noofdays','departuredate','createddate','image','status']



# Main page 
@admin.register(models.HomeIMG1)
class HomeIMG1Admin(admin.ModelAdmin):
    list_display = ['id','image']
    
@admin.register(models.HomeIMG2)
class HomeIMG2Admin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(models.AboutIMG1)
class AboutIMG1Admin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(models.AboutIMG2)
class AboutIMG2Admin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(models.ExperienceCount)
class ExperienceCountAdmin(admin.ModelAdmin):
    list_display = ['id','years','no_of_completed_tours','no_of_destinations']

@admin.register(models.ExperienceIMG1)
class ExperienceIMG1Admin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(models.ExperienceIMG2)
class ExperienceIMG2Admin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id','video']


# User 
@admin.register(models.Usersignup)
class UsersignupAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password']

# order
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','order_id','usersignup_id','trip_id','name','email','contact','persons','message','order_date','status','review']


# order
@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','order_id','usersignup_id','stars','feedback','feedback_date']