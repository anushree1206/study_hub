from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from study.models import CustomUser  
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from .models import StudyMaterial

@csrf_exempt  # This disables CSRF protection for this view

def index(request):
    return render(request, "index.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Redirecting to dashboard.")
            return redirect('dashboard')  # ✅ Make sure "dashboard" exists in urls.py
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")

# Register Page
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already taken!")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
            else:
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                user.save()

                # ✅ Auto-login and redirect to dashboard
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Registration successful! Welcome to the dashboard.")
                    return redirect('dashboard')  # ✅ Ensures redirection

        else:
            messages.error(request, "Passwords do not match!")

    return render(request, "register.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def custom_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html') 

def settings(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        theme = request.POST.get("theme")

        user = request.user
        user.username = username
        user.email = email

        if password:  # Only update password if a new one is entered
            user.set_password(password)

        user.save()

        messages.success(request, "Settings updated successfully!")
        return redirect("settings")  # Reloads the settings page

    return render(request, "settings.html")

def study_materials(request):
    materials = StudyMaterial.objects.all()
    return render(request, 'study_materials.html', {'materials': materials})

def community_support(request):
    return render(request, 'community_support.html')

def technical_resources(request):
    return render(request, 'technical_resources.html')

def career_guidance(request):
    return render(request, 'career_guidance.html')

def lab_manuals(request):
    return render(request, 'lab_manuals.html')

def events_hackathons(request):
    return render(request, 'events_hackathons.html')

def coding_challenges(request):
    return render(request, 'coding_challenges.html')

def contact(request):
    return render(request, 'contact.html')