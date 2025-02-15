from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('study-materials/', views.study_materials, name='study_materials'),
    path('community-support/', views.community_support, name='community_support'),
    path('technical-resources/', views.technical_resources, name='technical_resources'),
    path('career-guidance/', views.career_guidance, name='career_guidance'),
    path('lab-manuals/', views.lab_manuals, name='lab_manuals'),
    path('events-hackathons/', views.events_hackathons, name='events_hackathons'),
    path('coding-challenges/', views.coding_challenges, name='coding_challenges'),
    path('contact/', views.contact, name='contact'),
]
