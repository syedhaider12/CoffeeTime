from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import coffee
from .models import tea
from .models import juice
from .models import contact
from django.contrib import messages


def home(request):
    coff=coffee.objects.all()[:4]
    t=tea.objects.all()[:4]
    ju=juice.objects.all()[:4]
   
    return render(request,'home.html',{'coff':coff,'t':t , 'jui': ju})

def coffe(request):
    cofee = coffee.objects.all()
    return render(request,'coffee.html', {'cofee': cofee})

def ta(request):
    
    te=tea.objects.all()
    return render(request,'tea.html', {'te': te})

def juic(request):
    ju = juice.objects.all()
    return render(request,'juice.html',{'ju': ju})

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'incorrect user name or password')
            return redirect('/SignIn')
    else:
        return render(request,'signin.html')
        

def cont(request):
    if request.method == 'POST':
        email = request.POST['mail']
        Name = request.POST['nam']
        query = request.POST['text']
        d = contact(Name=Name,email=email,query=query)
        d.save();
        return redirect('/Contactus')
    else:
        return render(request,'contactus.html')

    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['user']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name Taken')
                return redirect('/Signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('/Signup')
            else:
                user = User.objects.Create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();

                return redirect('/SignIn')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('/Signup')
    else:
        
        return render(request,'signup.html')
def quick(request,myid,subid):
    if subid == 1 :
        va = coffee.objects.filter(id=myid)
    if subid == 2 :
        va = tea.objects.filter(id=myid)
    if subid == 3 :
        va = juice.objects.filter(id=myid)
    return render(request, 'quickview.html',{'product':va[0]})
def logt (request):
    auth.logout(request)
    return redirect('/')

    
        

        

    


