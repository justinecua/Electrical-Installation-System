from django.shortcuts import render
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
import pytz

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
    context = {
        'date': current_datetime.strftime("%B %d, %Y %I:%M %p")
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
def handle_media(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        accID = data.get("accID")
        audience = data.get("audience")
        caption = data.get("caption")
        tag_list = data.get("tags", [])

        
        new_service = Post.objects.create(
            account=accFK,
            audience=AudienceFK,
            caption=caption,
        )

    
        for name, base64_data in zip(photo_names, photo_base64_data):
            image_data = base64.b64decode(base64_data)
            content_file = ContentFile(image_data, name=name)

            imgkit = ImagekitClient(content_file)
            Photoresult = imgkit.upload_media_file()
            photo_link = Photoresult["url"]

            Photo.objects.create(
                link=photo_link,
                post=new_post,
            )

        
        photos = list(Photo.objects.filter(post=new_post).values())

        currentTime = datetime.now()
        postDate = new_post.dateTime

        context = {
            'status': 'success',
            'message': 'Successfully posted!',
            'userId': request.user.id,
            'accId': account_id,
            'firstname': account_firstname,
            'username': account_username,
            'profile_photo': account_profile_photo,
            'post_id': new_post.id,
            'caption': caption,
            'time': post_time,
            'photos': photos,
            'tags': tags,
            'comment_count': comment_count,
            'glows_count': glows_count,
            'has_liked': has_liked,
        }

        return JsonResponse( context, encoder = DjangoJSONEncoder)
    return JsonResponse({"status": "error", "message": "Only POST method is accepted"})
