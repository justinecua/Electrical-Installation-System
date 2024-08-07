from django.shortcuts import render
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def adminpanel(request):
    return render(request, 'adminpanel.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('pass')
        password2 = data.get('pass2')

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password1,
                    )
                    user = authenticate(username=username, password=password1)
                    if user is not None:
                        login(request, user)
                        return JsonResponse({"status": "success", "message": "Signup successfully", "redirect": "/dashboard"})
                    else:
                        return JsonResponse({"status": "error", "message": "Authentication failed"})
                else:
                    return JsonResponse({"status": "error", "message": "Email is already in use"})
            else:
                return JsonResponse({"status": "error", "message": "Username is already taken"})
        else:
            return JsonResponse({"status": "error", "message": "Passwords do not match. Please type again"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})


@csrf_exempt
def validatelogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Account does not exist"})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return JsonResponse({"status": "success", "message": "Login successfully", "redirect": "/adminpanel"})
            else:
                return JsonResponse({"status": "success", "message": "Login successfully", "redirect": "/dashboard"})
        else:
            return JsonResponse({"status": "error", "message": "Incorrect email or password"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

