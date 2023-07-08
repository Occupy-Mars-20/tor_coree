from django.shortcuts import redirect, render
from .models import Companysignup, Company, Province, Trip, HomeIMG1, HomeIMG2, AboutIMG1, AboutIMG2, ExperienceCount, ExperienceIMG1, ExperienceIMG2, Video, Usersignup,Order,Feedback
import json
# Create your views here.


def home(request):
    pro = Province.objects.all()
    tr = Trip.objects.all()
    li = []
    for i in pro:
        count = 0
        for j in tr:
            if i.id == j.province.id and j.status == True:
                count += 1
        data = {
            "provincename": i.name,
            "nooftrips": count,
        }
        li.append(data)
    if request.session.get("user_uuid"):
        data = {
            'home1': HomeIMG1.objects.order_by("?").first(),
            'home2': HomeIMG2.objects.order_by("?").first(),
            'about1': AboutIMG1.objects.order_by("?").first(),
            'about2': AboutIMG2.objects.order_by("?").first(),
            'experiencecount': ExperienceCount.objects.order_by("?").first(),
            'experience1': ExperienceIMG1.objects.order_by("?").first(),
            'experience2': ExperienceIMG2.objects.order_by("?").first(),
            'video': Video.objects.order_by("?").first(),
            'discover': Province.objects.order_by('?').all(),
            "li": li,
            "user": True,
            'userloged': True,
        }
        return render(request, 'user/index.html', data)
    elif request.session.get("companyuser_id"):
        return redirect('company')
    else:
        dis = Province.objects.order_by('?').all()
        li_province = []
        li_province_names = []
        for i in dis:
            li_province.append(i.image.name[10:])
            li_province_names.append(i.name)
        li_province_json = json.dumps(li_province)
        li_province_names_json = json.dumps(li_province_names)
        data = {
            'home1': HomeIMG1.objects.order_by("?").first(),
            'home2': HomeIMG2.objects.order_by("?").first(),
            'about1': AboutIMG1.objects.order_by("?").first(),
            'about2': AboutIMG2.objects.order_by("?").first(),
            'experiencecount': ExperienceCount.objects.order_by("?").first(),
            'experience1': ExperienceIMG1.objects.order_by("?").first(),
            'experience2': ExperienceIMG2.objects.order_by("?").first(),
            'video': Video.objects.order_by("?").first(),
            'discover': dis,
            'li_province':li_province_json,
            'li_province_names':li_province_names_json,
            "li": li,
        }
        return render(request, 'user/index.html', data)


def places(request, province=None, company=None):
    string = request.GET.get('search','')
    if province:
        pro_id = Province.objects.get(name=province)
        if string == '':
            tr = Trip.objects.filter(province=pro_id, status=True).all()
        else:
            tr = Trip.objects.filter(province=pro_id, status=True,place__contains=string).all()
        li = []
        for i in tr:
            ord = Order.objects.filter(trip_id=i.id).all()
            sum = 0
            count = 0
            for j in ord:
                feed = Feedback.objects.filter(order_id=j.id).all()
                for k in feed:
                    sum = sum + k.stars
                    count = count + 1
            if count>0:
                data={
                "tr_id":i,
                "feed":sum/count,
                }
                li.append(data)
            else:
                data={
                "tr_id":i,
                "feed":0,
                }
                li.append(data)
        if tr:
            if request.session.get("user_uuid"):
                return render(request, 'user/places.html', {'companynav': True, 'userloged': True, "user": True, 'tr': tr,'li':li, 'province': province,'search':string})
            else:
                return render(request, 'user/places.html', {'companynav': True, 'tr': tr,'li':li, 'province': province,'search':string})
        else:
            if request.session.get("user_uuid"):
                return render(request, 'user/places.html', {'companynav': True, 'userloged': True, "user": True, 'msg': 'No Place Added yet!..', 'province': province,'search':string})
            else:
                return render(request, 'user/places.html', {'companynav': True, 'msg': 'No Place Added yet!..', 'province': province,'search':string})
    elif company:
        company_id = Company.objects.get(companyname=company)
        if string == '':
            tr = Trip.objects.filter(company_id=company_id, status=True).all()
        else:
            tr = Trip.objects.filter(company_id=company_id, status=True,place__contains=string).all()
        li = []
        for i in tr:
            ord = Order.objects.filter(trip_id=i.id).all()
            sum = 0
            count = 0
            for j in ord:
                feed = Feedback.objects.filter(order_id=j.id).all()
                for k in feed:
                    sum = sum + k.stars
                    count = count + 1
            if count>0:
                data={
                "tr_id":i,
                "feed":sum/count,
                }
                li.append(data)
            else:
                data={
                "tr_id":i,
                "feed":0,
                }
                li.append(data)
        if tr:
            if request.session.get("user_uuid"):
                return render(request, 'user/places.html', {'companynav': True, 'userloged': True, "user": True, 'tr': tr,'li':li, 'company': company,'search':string})
            else:
                return render(request, 'user/places.html', {'companynav': True, 'tr': tr,'li':li, 'company': company, 'search':string})
        else:
            if request.session.get("user_uuid"):
                return render(request, 'user/places.html', {'companynav': True, 'userloged': True, "user": True, 'msg': 'No Place Added yet!..', 'province': province, 'search':string})
            else:
                return render(request, 'user/places.html', {'companynav': True, 'msg': 'No Place Added yet!..', 'province': province, 'search':string})
    else:
        if request.session.get("user_uuid"):
            return render(request, 'user/places.html', {'companynav': True, 'userloged': True, "user": True,'search':string})
        else:
            return render(request, 'user/places.html', {'companynav': True,'search':string})


def trendingplaces(request):

    string = request.GET.get('search','')

    if string == '':
        tr = Trip.objects.filter(status=True).all()
    else:
        tr = Trip.objects.filter(status=True,place__contains=string).all()
    li = []
    for i in tr:
        ord = Order.objects.filter(trip_id=i.id).all()
        sum = 0
        count = 0
        for j in ord:
            feed = Feedback.objects.filter(order_id=j.id).all()
            for k in feed:
                sum = sum + k.stars
                count = count + 1
        if count>0:
            data={
                "tr_id":i,
                "feed":sum/count,
                }
            li.append(data)
        else:
            data={
                "tr_id":i,
                "feed":0,
                }
            li.append(data)
    li.sort(key=lambda x: x.get('feed'), reverse=True)
    if request.session.get("user_uuid"):
        return render(request, 'user/trending.html', {'companynav': True,'userloged': True, "user": True,'tr':tr,'li':li,'search':string})
    else:
        return render(request, 'user/trending.html', {'companynav': True,'tr':tr,'li':li,'search':string})



def form(request, company=None, place=None):
    if request.method == 'POST':
        user = Usersignup.objects.get(pk=request.session.get("user_uuid"))
        obj = request.POST
        name = obj.get('name')
        email = obj.get('email')
        contact = obj.get('contact')
        noofpersons = obj.get('noofpersons')
        company_id = Company.objects.get(companyname=company)
        trip_id = Trip.objects.get(company_id=company_id, place=place, status=True)
        message = obj.get('msg')

        import random

        order_id = "TOR-"+str(random.randint(100000,999999))
        o = Order(usersignup_id=user,trip_id=trip_id,order_id=order_id,name=name,email=email,contact=contact,persons=noofpersons,message=message)
        o.save()
        return render(request, 'user/message.html', {'companynav': True,'userloged': True})
    else:
        if request.session.get("user_uuid"):
            company_id = Company.objects.get(companyname=company)
            tr = Trip.objects.get(company_id=company_id, place=place, status=True)
            return render(request, 'user/form.html', {'companynav': True, 'userloged': True, "user": True, 'tr': tr})
        else:
            return render(request, 'user/loginrequired.html', {'companynav': True})

def orderupdate(request,id=None):
    Order.objects.filter(pk=id).update(status=True)
    return redirect('orders')



def allcompanies(request, company=None):
    string = request.GET.get('search','')

    if string == '':
        obj = Company.objects.all()
    else:
        obj =  Company.objects.filter(companyname__contains=string)
    tr = Trip.objects.all()
    li = []
    for i in obj:
        count = 0
        for j in tr:
            if i.id == j.company_id.id and j.status == True:
                count += 1
        data = {
            "company_name": i.companyname,
            "nooftrips": count,
        }
        li.append(data)

    tr_stars = Trip.objects.filter(status=True).all()
    company = Company.objects.filter(status=True).all()
    li_stars = []
    for c in company:
        sum = 0
        count = 0
        for i in tr_stars:
            if i.company_id.id == c.id:
                ord = Order.objects.filter(trip_id=i.id).all()
                for j in ord:
                    feed = Feedback.objects.filter(order_id=j.id).all()
                    for k in feed:
                        sum = sum + k.stars
                        count = count + 1
        if count>0:
            data={
                "company_id":c,
                "feed":sum/count,
                }
            li_stars.append(data)
        else:
            data={
                "company_id":c,
                "feed":0,
                }
            li_stars.append(data)
    if request.session.get("user_uuid"):
        return render(request, 'user/allcompanies.html', {'companynav': True, 'userloged': True, "user": True, "data": obj, "li": li,'company_ratings':li_stars,"search":string})
    else:
        return render(request, 'user/allcompanies.html', {'companynav': True, "data": obj, "li": li,'company_ratings':li_stars,"search":string})


# Company
def companysignup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = Companysignup(username=uname, email=email, password=password)
        if obj.isExists():
            return render(request, 'company/companylogin.html', {'error_msg': "Username already exists"})
        else:
            obj.save()
            return render(request, 'company/companylogin.html', {'success': "Congratulations! User Registered Successfully."})
    else:
        if request.session.get("companyuser_id"):
            return redirect('company')
        else:
            return render(request, 'company/companylogin.html')


def companylogin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        try:
            dbuser = Companysignup.objects.get(username=uname)
            user = True
        except:
            user = False
        if user:
            if dbuser.username == uname and dbuser.password == password:
                request.session["companyuser_id"] = dbuser.id
                return redirect('company')
            else:
                return render(request, 'company/companylogin.html', {'error_msg': "Wrong Password"})
        else:
            return render(request, 'company/companylogin.html', {'error_msg': "Wrong Username"})
    else:
        if request.session.get("companyuser_id"):
            return redirect('company')
        else:
            return render(request, 'company/companylogin.html')


def company(request, id=None):
    if request.method == "POST":
        companyuser_id = request.session.get("companyuser_id")
        dbcompanyuser_id = Companysignup.objects.get(pk=companyuser_id)
        frm = request.POST
        fname = frm.get('fname')
        lname = frm.get('lname')
        email = frm.get('email')
        phone = frm.get('phone')
        company = frm.get('company')
        city = frm.get('city')
        desc = frm.get('desc')
        if id:
            Company.objects.filter(pk=id).update(companysignup_id=dbcompanyuser_id, fname=fname,
                                                 lname=lname, email=email, phone=phone, companyname=company, city=city, description=desc)
            obj = Company.objects.get(pk=id)
            return render(request, 'company/company.html', {'obj': obj})
        else:
            image = request.FILES['img']
            obj = Company(companysignup_id=dbcompanyuser_id, fname=fname, lname=lname, email=email,
                          phone=phone, companyname=company, city=city, image=image, description=desc)
            obj.save()
            try:
                obj = Company.objects.get(companysignup_id=companyuser_id)
                re = True
            except:
                re = False
            if re:
                return render(request, 'company/company.html', {'underprocess': 'Registeration is under Process...'})
    else:
        if id:
            obj = Company.objects.get(pk=id)
            return render(request, 'company/company.html', {'isyes': obj})
        else:
            print(request.user)
            if not request.session.get("companyuser_id"):
                return redirect('companysignup')
            else:
                companyuser_id = request.session.get("companyuser_id")
                try:
                    obj = Company.objects.get(companysignup_id=companyuser_id)
                    re = True
                except:
                    re = False
                if re:
                    if obj.status:
                        return render(request, 'company/company.html', {'obj': obj})
                    else:
                        return render(request, 'company/company.html', {'underprocess': 'Registeration is under Process...'})
                else:
                    return render(request, 'company/company.html', {'isnot': True})


def addtrip(request, id=None):
    if request.method == "POST":
        companyuser_id = request.session.get("companyuser_id")
        dbcompany_id = Company.objects.get(companysignup_id=companyuser_id)
        frm = request.POST
        place = frm.get('place')
        price = frm.get('price')
        province = frm.get('province')
        pcity = frm.get('pcity')
        noofdays = frm.get('noofdays')
        date = frm.get('date')
        if frm.get('chck'):
            status = True
        else:
            status = False
        pro = Province.objects.get(pk=province)
        if id:
            Trip.objects.filter(pk=id).update(place=place, price=price, province=pro,
                                              city=pcity, noofdays=noofdays, departuredate=date, status=status)
            return redirect('alltrip')
        else:
            image = request.FILES['img']
            obj = Trip(company_id=dbcompany_id, place=place, price=price, province=pro,
                       city=pcity, noofdays=noofdays, departuredate=date, image=image)
            obj.save()
            return render(request, 'company/alltrip.html')
    else:
        if not request.session.get("companyuser_id"):
            return redirect('companysignup')
        else:
            if id:
                companyuser_id = request.session.get("companyuser_id")
                dbcompany_id = Company.objects.get(companysignup_id=companyuser_id)
                obj = Trip.objects.get(pk=id)
                pro = Province.objects.all()
                return render(request, 'company/addtrip.html', {"pro": pro, 'obj': obj,'company':dbcompany_id})
            else:
                pro = Province.objects.all()
                companyuser_id = request.session.get("companyuser_id")
                try:
                    dbcompany_id = Company.objects.get(companysignup_id=companyuser_id)
                    re = True
                except:
                    re = False
                if re:
                    return render(request, 'company/addtrip.html', {"pro": pro,'underprocess':'Wait for Company Registeration','company':dbcompany_id})
                else:
                    return render(request, 'company/addtrip.html', {"pro": pro,'underprocess':'Please Register Company First',})


def alltrip(request):
    if not request.session.get("companyuser_id"):
        return redirect('companysignup')
    else:
        companyuser_id = request.session.get("companyuser_id")
        try:
            dbcompany_id = Company.objects.get(companysignup_id=companyuser_id)
            trip = Trip.objects.filter(company_id=dbcompany_id.id).all()
            re = True
        except:
            re = False
        if re:
            li = []
            for i in trip:
                ord = Order.objects.filter(trip_id=i.id).all()
                sum = 0
                count = 0
                for j in ord:
                    feed = Feedback.objects.filter(order_id=j.id).all()
                    for k in feed:
                        sum = sum + k.stars
                        count = count + 1
                if count>0:
                    data={
                        "tr_id":i,
                        "feed":sum/count,
                    }
                    li.append(data)
                else:
                    data={
                        "tr_id":i,
                        "feed":0,
                    }
                    li.append(data)
                print(li)
            return render(request, 'company/alltrip.html', {'feed': li,'trip':trip})
        else:
            return render(request, 'company/alltrip.html', {'notadded': 'No Trips '})


def orders(request):
    if not request.session.get("companyuser_id"):
        return redirect('companysignup')
    else:
        try:
            companyuser_id = Companysignup.objects.get(pk=request.session.get("companyuser_id"))
            company_id = Company.objects.get(companysignup_id=companyuser_id)
            trips = Trip.objects.filter(company_id=company_id).all()
            re = True
        except:
            re = False
        if re:
            li =[]
            for i in trips:
                orders = Order.objects.filter(trip_id=i.pk).all()
                li.append(orders)
            return render(request, 'company/orders.html',{'orders':li,})
        else:
            return render(request, 'company/orders.html',{'noorder':'No orders ',})



def clogout(request):
    if not request.session.get("companyuser_id"):
        return redirect('home')
    else:
        del request.session['companyuser_id']
        return redirect('home')


# user
def usersignup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = Usersignup(username=uname, email=email, password=password)
        if obj.isExists():
            return render(request, 'user/userlogin.html', {'error_msg': "Username already exists"})
        else:
            obj.save()
            return render(request, 'user/userlogin.html', {'success': "Congratulations! User Registered Successfully."})
    else:
        if request.session.get("user_uuid"):
            return redirect('home')
        else:
            return render(request, 'user/userlogin.html')


def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        try:
            dbuser = Usersignup.objects.get(username=uname)
            user = True
        except:
            user = False
        if user:
            if dbuser.username == uname and dbuser.password == password:
                request.session["user_uuid"] = dbuser.id
                return redirect('home')
            else:
                return render(request, 'user/userlogin.html', {'error_msg': "Wrong Password"})
        else:
            return render(request, 'user/userlogin.html', {'error_msg': "Wrong Username"})
    else:
        if request.session.get("user_uuid"):
            return redirect('home')
        else:
            return render(request, 'user/userlogin.html')


def myorders(request):
    if request.session.get("user_uuid"):
        user_id = Usersignup.objects.get(pk=request.session.get("user_uuid"))
        string = request.GET.get('search','')

        if string == '':
            orders = Order.objects.filter(usersignup_id=user_id).all()

        else:
            orders = Order.objects.filter(usersignup_id=user_id,order_id__contains=string).all()
        return render(request, 'user/orders.html',{'companynav': True, 'userloged': True, "user": True, 'orders':orders,'search':string})

def myreviews(request):
    if request.session.get("user_uuid"):
        user_id = Usersignup.objects.get(pk=request.session.get("user_uuid"))
        string = request.GET.get('search','')

        if string == '':
            reviews = Feedback.objects.filter(usersignup_id=user_id).all()

        else:
            reviews = Feedback.objects.filter(usersignup_id=user_id,feedback__contains=string).all()
        orders = Order.objects.filter(usersignup_id=user_id,review=True).all()
        return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'reviews':reviews,'orders':orders,'userreview':True,'search':string})
    
def allreviews(request):

    tr_stars = Trip.objects.filter(status=True).all()
    string = request.GET.get('search','')

    if string == '':
            company = Company.objects.filter(status=True).all()
    else:
        company = Company.objects.filter(status=True,companyname__contains=string).all()
    li_stars = []
    for c in company:
        sum = 0
        count = 0
        for i in tr_stars:
            if i.company_id.id == c.id:
                ord = Order.objects.filter(trip_id=i.id,status=True).all()
                for j in ord:
                    feed = Feedback.objects.filter(order_id=j.id).all()
                    for k in feed:
                        sum = sum + k.stars
                        count = count + 1
        if count==0:
            data={
                "company_id":c,
                "feed":sum/1,
                "count":count,
                }
            li_stars.append(data)
        else:
            data={
                "company_id":c,
                "feed":sum/count,
                "count":count,
                }
            li_stars.append(data)


    if request.session.get("user_uuid"):
        if id is not None:
            return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'li_stars':li_stars,'company':True,'search':string})
        else:
            return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'li_stars':li_stars,'company':True,'search':string})

    else:
        if id is not None:
            return render(request, 'user/reviews.html',{'companynav': True,'li_stars':li_stars,'company':True,'search':string})
        else:
            return render(request, 'user/reviews.html',{'companynav': True,'li_stars':li_stars,'company':True,'search':string})


def reviewbycompany(request,id=None):
    orders = Order.objects.filter(review=True).all()
    
    string = request.GET.get('search','')

    if string == '':
        trip_id = Trip.objects.filter(company_id=id).all()
    else:
        trip_id = Trip.objects.filter(company_id=id,place__contains=string).all()

    company_review = []
    for t in trip_id:
        ord = Order.objects.filter(trip_id=t.id,review=True).all()
        for o in ord:
            fe = Feedback.objects.filter(order_id=o).all()
            for f in fe:
                company_review.append(f)

    if request.session.get("user_uuid"):
        if id is not None:
            return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'company_review':company_review,'trip_id':trip_id,'ord':orders,'reviewbycompany':True,'search':string})
        else:
            return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'search':string})

    else:
        if id is not None:
            return render(request, 'user/reviews.html',{'companynav': True,'company_review':company_review,'trip_id':trip_id,'ord':orders,'reviewbycompany':True,'search':string})
        else:
            return render(request, 'user/reviews.html',{'companynav': True,'search':string})
        
def placereviews(request,id=None):

    string = request.GET.get('search','')

    if string == '':
        trip_id = Trip.objects.filter(id=id).all()
    else:
        trip_id = Trip.objects.filter(id=id,place__contains=string).all()
    place_review = []
    if trip_id:
        for t in trip_id:
            ord = Order.objects.filter(trip_id=t.id,review=True).all()
            for o in ord:
                fe = Feedback.objects.filter(order_id=o ).all()
                for f in fe:
                    place_review.append(f)
    else:
        ord=""
    if request.session.get("user_uuid"):
        if id is not None:
            return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'place_review':place_review,'trip_id':trip_id,'ord':ord,'placereview':True,'search':string})
        else:
            return render(request, 'user/reviews.html',{'companynav': True, 'userloged': True, "user": True,'search':string})

    else:
        if id is not None:
            return render(request, 'user/reviews.html',{'companynav': True,'place_review':place_review,'trip_id':trip_id,'ord':ord,'placereview':True,'search':string})
        else:
            return render(request, 'user/reviews.html',{'companynav': True,'search':string})

def feedback(request,order_id=None,feedback_id=None):
    if request.method=='POST' and order_id:
        user_id = Usersignup.objects.get(pk=request.session.get("user_uuid"))
        ob = request.POST
        orderid = Order.objects.get(order_id=ob.get('order_id'))
        feedback = ob.get('feedback')
        stars = float(ob.get('rating'))
        obj = Feedback(usersignup_id=user_id,order_id=orderid,stars=stars,feedback=feedback,)
        obj.save()
        Order.objects.filter(pk=orderid.id).update(review=True)
        return render(request, 'user/message.html',{'companynav': True, 'userloged': True, 'user':True,'msg':'Your Review has been Submitted.Thank You ☺','feed':True})
    if request.method=='POST' and feedback_id:
        ob = request.POST
        feedback = ob.get('feedback')
        stars = float(ob.get('rating'))
        Feedback.objects.filter(pk=feedback_id).update(stars=stars,feedback=feedback,)
        return render(request, 'user/message.html',{'companynav': True, 'userloged': True, 'user':True,'msg':'Your Review has been Updated','feed':True})
    elif order_id:
        if request.session.get("user_uuid"):
            return render(request, 'user/feedback.html',{'companynav': True, 'userloged': True,'user':True,'order_id':order_id,})
        else:
            return redirect('userlogin')
    elif feedback_id:
        feed = Feedback.objects.get(pk=feedback_id)
        if request.session.get("user_uuid"):
            return render(request,'user/feedback.html',{'companynav': True, 'userloged': True,'user':True,'feed':feed,})
        else:
            return redirect('userlogin')


def ulogout(request):
    if not request.session.get("user_uuid"):
        return redirect('home')
    else:
        del request.session['user_uuid']
        return redirect('home')
