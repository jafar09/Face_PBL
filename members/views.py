from django.shortcuts import render, redirect,HttpResponse
from .models import Member 
from .forms import ProjectForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , login, logout 
from django.contrib import messages
from .models import Member
# @login_required(login_url='login')

# home view
def home(request):
    return render(request, "home.html")
# home view tugadi

# signup view
def signup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Sizning tergan parolingiz  parolingizga bilan bir-xil emas!!")
        else:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return redirect("login")

    return render(request, 'signup.html')
# signup view

# custom_login view
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Foydalanuvchi nomi yoki parol noto`g`ri.')
            return render(request, 'login.html')  # Render login page with error message
    else:
        return render(request, 'login.html')  # Render login page for GET requests
# custom_login view tugadi

# LogoutPage view
def LogoutPage(request):
    logout(request)
    return redirect('login')
# LogoutPage view


# project_add View
def project_add(request):
    form=ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        form.save()
        form=ProjectForm()

    data=Member.objects.all()

    context = {
        'form': form,
        'data': data,
    }
    return render(request, "project_add.html", context)
# project_add View tugadi

    
#project show View 
def project_show(request):
    data=Member.objects.all()
    context = {
        'data':data,
    }
    return render(request, "projects.html", context)     
#project show View tugadi


# Delete View
def delete_record(request,id):
    a=Member.objects.get(pk=id)
    a.delete()
    return redirect('projects')
# Delete View tugadi
    

    # Update View 
def Update_Record(request,id):
    if request.method=='POST':
        data=Member.objects.get(pk=id)
        form = ProjectForm(instance=data)
        if form.is_valid():
            form.save()
    else:
        data=Member.objects.get(pk=id)
        form=ProjectForm(instance=data)
    context={
        'form':form,
    }
    return render(request,'update.html',context)
# update view tugadi