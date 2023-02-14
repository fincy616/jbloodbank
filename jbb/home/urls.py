from django.conf import settings
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='home'),
    path('login/',views.loginView,name='login'),
    path('register/',views.requestView,name='register'),
    path('logout/', views.logoutView, name = 'logout'),
    path('booking/',views.register,name='booking'),
    path('userpage/',views.userpage,name='userpage'),
    path('brequest/',views.requestView,name='brequest'),
    path('invalid/',views.invalidView, name='invalid'),
    path('einvalid/',views.einvalidView, name='einvalid'),
]

# path('official/dashboard/', views.officialDashboardView, name = 'official_dashboard'),
