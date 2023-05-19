from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
# Create your views here.

from .forms import SignUp, ProfileForm, budgetForm

from .models import Profile, Budget



def index(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user = None
    return render(request,"budgety/index.html",{'user':user})

def About(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user = None
    return render(request,"budgety/About.html",{'user':user})


def Contact(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user = None
    return render(request,"budgety/contact.html",{'user':user})

def Blog(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user = None
    return render(request,"budgety/blogg.html",{'user':user})







def mybudget(request):
    try:
        user = User.objects.get(id=request.user.id)
        try:
            user_profile = Profile.objects.get(user=user)
            return render(request,"budgety/mybudget.html")
        except Profile.DoesNotExist:
            return redirect("connect")
    except User.DoesNotExist:
        return redirect('login')

    # return render(request, "budgety/mybudget.html",{'form':form})

def budgety(request):
    if request.method == "POST":
         data = request.POST
         print(data)
         option = data['option']
         description = data['name']
         amount = float(data['money'])

         new = Budget()
         new.name = description
         new.amount = amount
         new.is_income = option == "inc"
         new.user = request.user
         new.save()
    # return redirect('mybudget')


def register_user(request):

    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()

            return redirect('login')

        else:
            return render(request, "budgety/signup.html",{'form':form})

        
    form = SignUp()
    return render(request, "budgety/signup.html",{'form':form})

def login_view(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        email    = data['email']

        user = authenticate (request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('connect')

        else:
            msg = "invalid username or password"

    return render(request,"budgety/login.html", {'msg':msg})

def logout_view(request):
    logout(request)
    return redirect('index')



def connect(request):
    try:
        user = User.objects.get(id=request.user.id)
        try:
            user_profile = Profile.objects.get(user=user)
            return redirect('mybudget')
        except Profile.DoesNotExist:
            pass
    except User.DoesNotExist:
        return redirect('login')

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            # user.set_password(request.POST['password'])
            user.save()

            return redirect('mybudget')

        else:
            return render(request, "budgety/connect.html",{'form':form})

        
    form = ProfileForm()
    return render(request, "budgety/connect.html",{'form':form})