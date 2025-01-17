from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.user_registration, name = "sign-up"),
    path('sign-in/', views.user_login, name = "sign-in"),
    path('logout/', views.user_logout, name = "logout"),
]