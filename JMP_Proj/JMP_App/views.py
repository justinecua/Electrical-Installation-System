from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Services, Account, Projects
from django.http import JsonResponse
from datetime import datetime
import pytz
from .helpers import ImagekitClient
from imagekitio import ImageKit
from dotenv import load_dotenv
import os
from django.contrib import messages
from django.shortcuts import get_object_or_404


load_dotenv()
imagekit = ImageKit(
    public_key=os.getenv('IMAGEKIT_PUBLIC_KEY'),
    private_key=os.getenv('IMAGEKIT_PRIVATE_KEY'),
    url_endpoint=os.getenv('IMAGEKIT_URL_ENDPOINT')
)

def home(request):
    services = Services.objects.values()
    projects = Projects.objects.values()
    context = {
        'services': services,
        'projects': projects,
    }
    return render(request, 'index.html', context)

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
    manila_timezone = pytz.timezone('Asia/Manila')
    current_datetime = datetime.now(manila_timezone)
    projects = Projects.objects.values()
    projects_count = Projects.objects.count()

    for project in projects:
        project['date'] = project['date'].strftime("%b %d, %Y")
        
    context = {
        'totalProjects': projects_count,
        'projects': projects,
        'project_date': current_datetime.strftime("%b %d, %Y"),    
        'messages': messages.get_messages(request), 
    }
    return render(request, 'admin_projects.html', context)

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

@csrf_exempt
def fetch4editService(request, serviceId):
    try:
        service = Services.objects.get(id=serviceId)

        context = {
            'name': service.name,
            'description': service.description,
            'icon': service.icon,
            'icon_file_id': service.icon_file_id,
            'price': service.price,
            'date': service.date,
        }
        return JsonResponse({"status": "success", "context": context})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


def accounts(request):
    all_accounts = Account.objects.values()
    print(all_accounts)
    return render(request, 'admin_accounts.html', {'accounts': all_accounts})

@csrf_exempt
def saveProject(request):
    if request.method == 'POST':
        project_caption = request.POST.get('caption')
        project_picture = request.FILES.get('project_picture')

        if not project_caption or not project_picture:
            messages.error(request, "Caption and photo are required.")
            return redirect('adminProjects')

        if project_picture.size > 5 * 1024 * 1024:
            messages.error(request, "Image size must not exceed 10MB.")
            return redirect('adminProjects')

        try:
            imgkit = ImagekitClient(project_picture)
            result = imgkit.upload_media_file()
            project_picture_url = result["url"]
            project_picture_id = result["fileId"]

            new_project = Projects.objects.create(
                caption=project_caption,
                project_picture=project_picture_url,
                project_picture_id=project_picture_id
            )

            messages.success(request, "Project added successfully!")
            return redirect('adminProjects')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('adminProjects')

    else:
        messages.error(request, "Only POST requests are allowed.")
        return redirect('adminProjects')

@csrf_exempt
def editProject(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project_caption = request.POST.get('caption')
        project_picture = request.FILES.get('project_picture')

        try:
            project = Projects.objects.get(id=project_id)

            if project_picture:
                imgkit = ImagekitClient(project_picture)
                result = imgkit.upload_media_file()
                project.project_picture = result["url"]
                project.project_picture_id = result["fileId"]

            project.caption = project_caption
            project.save()

            messages.success(request, "Project updated successfully!")
            return redirect('adminProjects')

        except Projects.DoesNotExist:
            messages.error(request, "Project not found.")
            return redirect('adminProjects')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('adminProjects')

    else:
        messages.error(request, "Only POST requests are allowed.")
        return redirect('adminProjects')


def deleteProject(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    try:
        if project.project_picture_id:
            imagekit.delete_file(file_id=project.project_picture_id)

        project.delete()
        messages.success(request, "Project deleted successfully.")
        
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the project: {str(e)}")

    return redirect('adminProjects')
