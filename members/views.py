from django.shortcuts import render, redirect,HttpResponse
from .models import Member 
from .forms import ProjectForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , login, logout 
from django.contrib import messages
from .models import Member
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from .utils import is_ajax, classify_face
import base64
# from logs.models import Log 
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
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
# signup view tugadi

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
            return render(request, 'home.html')  # Render login page with error message
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
        print("==============================")
        print(form.is_valid())
        print("==============================")
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

def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = User.objects.filter(username=res).exists()
            if user_exists:
                user = User.objects.get(username=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    