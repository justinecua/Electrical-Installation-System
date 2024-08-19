from django.shortcuts import render
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Services
from django.http import JsonResponse
from datetime import datetime
import pytz
from .helpers import ImagekitClient
from imagekitio import ImageKit
from dotenv import load_dotenv
import os

load_dotenv()
imagekit = ImageKit(
    public_key=os.getenv('IMAGEKIT_PUBLIC_KEY'),
    private_key=os.getenv('IMAGEKIT_PRIVATE_KEY'),
    url_endpoint=os.getenv('IMAGEKIT_URL_ENDPOINT')
)

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def adminpanel(request):
    manila_timezone = pytz.timezone('Asia/Manila')
    current_datetime = datetime.now(manila_timezone)
    context = {
        'date': current_datetime.strftime("%B %d, %Y %I:%M %p")
    }

    return render(request, 'adminpanel.html', context)

def adminAccounts(request):
    return render(request, 'admin_accounts.html')

def adminServices(request):
    manila_timezone = pytz.timezone('Asia/Manila')
    current_datetime = datetime.now(manila_timezone)
    services = Services.objects.values()
    totalServices = Services.objects.count()

    for service in services:
        service['date'] = service['date'].strftime("%b %d, %Y")

    context = {
        'date': current_datetime.strftime("%b %d, %Y %I:%M %p"),
        'services': services,
        'totalServices': totalServices
    }
    

    return render(request, 'admin_services.html', context)

def adminPayments(request):
    return render(request, 'admin_payments.html')

def adminProjects(request):
    return render(request, 'admin_projects.html')

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


@csrf_exempt
def saveService(request):
    if request.method == 'POST':
        form_data = json.loads(request.POST['data'])
        serviceIcon = request.FILES.get('serviceIcon')

        serviceName = form_data.get('serviceName')
        serviceDesc = form_data.get('serviceDesc')
        servicePrice = form_data.get('servicePrice')

        imgkit = ImagekitClient(serviceIcon)
        result = imgkit.upload_media_file()
        serviceIcon_url = result["url"]
        serviceIcon_id = result["fileId"]
        
        newService = Services.objects.create(
                name=serviceName,
                description=serviceDesc,
                icon=serviceIcon_url,
                icon_file_id = serviceIcon_id,
                price=servicePrice,
            )
        newService_date = newService.date.strftime("%b %d, %Y") 
        context = {
            'serviceId': newService.id,
            'serviceIcon': newService.icon,
            'serviceDesc': newService.description,
            'serviceName': newService.name,
            'servicePrice': newService.price,
            'serviceDate': newService_date,
        }

        return JsonResponse({"status": "success", "message": "Service added successfully!", 'service': context})
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed."})

@csrf_exempt
def deleteService(request, serviceId):
    try:
        service = Services.objects.get(id=serviceId)
        imagekit.delete_file(file_id=service.icon_file_id)
        service.delete()
        
        return JsonResponse({"status": "success", "message": "Deleted successfully!"})
    
    except Services.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Service does not exist."}, status=404)
    
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
