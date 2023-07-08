from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('', views.home,name="home"),

    
    path('places', views.places, name="places"),
    path('trendingplaces', views.trendingplaces, name="trending"),
    path('places/<province>', views.places, name="places"),
    path('places/<company>/<place>/form', views.form, name="form"),
    path('form', views.form, name="form"),
    path('allcompanies', views.allcompanies, name="allcompanies"),
    path('allcompanies/<company>', views.places,name="allcompanies"),


    path('usersignup', views.usersignup, name="usersignup"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('myorders', views.myorders, name="myorders"),
    path('myreviews', views.myreviews, name="myreviews"),
    path('allreviews', views.allreviews, name="allreviews"),
    path('placereviews/place=<int:id>', views.placereviews, name="placereviews"),
    path('reviewbycompany/company=<int:id>', views.reviewbycompany, name="reviewbycompany"),
    path('feedback/orderid=<order_id>', views.feedback, name="feedback"),
    path('feedback/edit=<feedback_id>', views.feedback, name="editfeedback"),
    path('ulogout', views.ulogout, name="ulogout"),


    path('companysignup', views.companysignup, name="companysignup"),
    path('companylogin', views.companylogin, name="companylogin"),
    path('company', views.company, name="company"),
    path('company/<int:id>', views.company, name="company"),
    path('addtrip', views.addtrip, name="addtrip"),
    path('addtrip/<int:id>', views.addtrip, name="addtrip"),
    path('alltrip', views.alltrip, name="alltrip"),
    path('orders', views.orders, name="orders"),
    path('orderupdate/<int:id>', views.orderupdate, name="orderupdate"),
    path('clogout', views.clogout, name="clogout"),
]
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)